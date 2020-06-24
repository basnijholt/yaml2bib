#!/usr/bin/env python3
"""Convert a yaml file to bib file with the correct journal abbreviations."""

import contextlib
import glob
import os
from typing import Dict, List, Optional, Tuple

import click
import crossref.restful
import diskcache
import requests
import yaml
from pylatexenc.latexencode import unicode_to_latex
from tqdm import tqdm


def pages_from_crossref(data, works: crossref.restful.Works) -> str:
    try:
        page = data["article-number"]
    except KeyError:
        if "page" in data:
            page = data["page"].split("-")[0]
        else:
            raise Exception("No page number found!")
    return page


def journal_from_crossref(data, works: crossref.restful.Works) -> Tuple[str, str]:
    return data["container-title"][0], data["short-container-title"][0]


def cached_crossref(doi: str, works: crossref.restful.Works, database: str) -> str:
    """Look up if this has previously been called."""
    with diskcache.Cache(database) as cache:
        info = cache.get(doi)
        if info is not None:
            return info
        info = works.doi(doi)
        cache[doi] = info
        return info


def replace_key(
    key: str,
    data,
    bib_entry: str,
    replacements: List[Tuple[str, str]],
    works: crossref.restful.Works,
) -> str:
    bib_type = bib_entry.split("{")[0]
    bib_context = bib_entry.split(",", maxsplit=1)[1]
    # Now only modify `bib_context` because we don't want to touch the key.

    # Replace non-ascii characters by LaTeX equivalent
    bib_context = unicode_to_latex(bib_context, non_ascii_only=True)

    to_replace = replacements.copy()

    with contextlib.suppress(Exception):
        # Use the journal abbrv. from crossref, not used if hard coded.
        to_replace.append(journal_from_crossref(data, works))

    for old, new in to_replace:
        bib_context = bib_context.replace(old, new)

    result = bib_type + "{" + key + "," + bib_context

    if "pages = {" not in result:
        # Add the page number if it's missing
        with contextlib.suppress(Exception):
            pages = pages_from_crossref(data, works)
            lines = result.split("\n")
            lines.insert(2, f"\tpages = {{{pages}}},")
            result = "\n".join(lines)

    return result


def doi2bib(doi: str) -> str:
    """Return a bibTeX string of metadata for a given DOI."""
    print(f"Requesting {doi}")
    url = "http://dx.doi.org/" + doi
    headers = {"accept": "application/x-bibtex"}
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    return r.text


def cached_doi2bib(doi: str, database: str) -> str:
    """Look up if this has previously been called."""
    with diskcache.Cache(database) as cache:
        text = cache.get(doi)
        if text is not None:
            return text
        text = doi2bib(doi)
        if text != "" and "<html>" not in text:
            print(f"Succesfully got '{doi}' 🎉")
            cache[doi] = text
        else:
            print(f"Failed on '{doi}' 😢")
        return text


def combine_yamls(pathname: str) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for fname in glob.glob(pathname):
        with open(fname) as f:
            for k, v in yaml.safe_load(f).items():
                # Check that there are no duplicate keys with different DOIs.
                if k in mapping:
                    if v.lower() != mapping[k].lower():
                        msg = f"{k} exists for multiple DOIs: {v} and {mapping[k]}."
                        raise KeyError(msg)
                else:
                    mapping[k] = v

    dois = dict(sorted(mapping.items()))
    return dois


def parse_doi_yaml(fname: str) -> Dict[str, str]:
    if os.path.isfile(fname):
        with open(fname) as f:
            return yaml.safe_load(f)
    else:
        return combine_yamls(fname)


def parse_replacements_yaml(fname: Optional[str]) -> List[Tuple[str, str]]:
    if fname is None:
        return []

    with open(fname) as f:
        d = yaml.safe_load(f)
    all_replacements = []
    for replacements in d.values():
        for k, v in replacements.items():
            all_replacements.append((k, v))
    return all_replacements


def write_output(entries: List[str], bib_files: List[str], bib_fname: str) -> None:
    with open(bib_fname, "w") as outfile:
        outfile.write("@preamble{ {\\providecommand{\\BIBYu}{Yu} } }\n\n")
        for fname in bib_files:
            outfile.write(f"\n% Below is from `{fname}`.\n\n")
            with open(fname) as infile:
                outfile.write(infile.read())
        outfile.write("\n% Below is from all `yaml` files.\n\n")
        for e in entries:
            for line in e.split("\n"):
                # Remove the url line because LaTeX creates it from the DOI
                if "url = {" not in line:
                    outfile.write(f"{line}\n")
            outfile.write("\n")


def static_bib_entries(pathname: Optional[str]) -> List[str]:
    if pathname is None:
        return []
    elif os.path.isfile(pathname):
        return [pathname]
    else:
        return glob.glob(pathname)


def get_bib_entries(
    dois: Dict[str, str],
    replacements: List[Tuple[str, str]],
    doi2bib_database: str,
    crossref_database: str,
    works: crossref.restful.Works,
) -> List[str]:
    return [
        replace_key(
            key,
            data=cached_crossref(doi, works, crossref_database),
            bib_entry=cached_doi2bib(doi, doi2bib_database),
            replacements=replacements,
            works=works,
        )
        for key, doi in tqdm(dois.items())
    ]


def yaml2bib(
    bib_fname: str,
    dois_yaml: str,
    replacements_yaml: Optional[str],
    static_bib: Optional[str],
    doi2bib_database: str,
    crossref_database: str,
    email: str,
) -> None:
    """Convert a yaml file to bib file with the correct journal abbreviations.

    Parameters
    ----------
    bib_fname: str
        Output file. (default: ``'dissertation.bib'``)
    dois_yaml: str
        The ``key: doi`` YAML file, may contain wildcards (``*``).
        (default: ``'bib.yaml'``, example: ``'*/*.yaml'``)
    replacements_yaml: str
        Replacements to perform, might be ``None``.
        (default: ``None``, example: ``'replacements.yaml'``)
    static_bib: str
        Static bib entries, might be ``None``, may contain wildcards (``*``).
        (default: ``None``, example: ``'chapter_*/not_on_crossref.bib'``)
    doi2bib_database: str
        The doi2bib database folder 📁 to not query doi.org more than needed.
        (default: ``'yaml2bib-doi2bib.db'``)
    crossref_database: str
        The Crossref database folder 📁 to not query crossref.org more than needed.
        (default: ``'yaml2bib-doi2bib.db'``)
    email: str
        E-mail 📧 for crossref.org, such that one can make faster API.
        (default: ``'anonymous'``, example: ``'bas@nijho.lt'``)

    Returns
    -------
    None

    Examples
    --------
    Example invocation for my `thesis <https://gitlab.kwant-project.org/qt/basnijholt/thesis-bas-nijholt>`_.

    .. code-block:: bash

        yaml2bib \\
          --bib_fname "dissertation.bib" \\
          --dois_yaml "*/*.yaml" \\
          --replacements_yaml "replacements.yaml" \\
          --static_bib "chapter_*/not_on_crossref.bib" \\
          --email "bas@nijho.lt"

    """
    etiquette = crossref.restful.Etiquette("publist", contact_email=email)
    works = crossref.restful.Works(etiquette=etiquette)
    dois = parse_doi_yaml(dois_yaml)
    replacements = parse_replacements_yaml(replacements_yaml)
    entries = get_bib_entries(
        dois, replacements, doi2bib_database, crossref_database, works
    )
    bib_files = static_bib_entries(static_bib)
    write_output(entries, bib_files, bib_fname)


@click.command()
@click.option(
    "--bib_fname",
    default="dissertation.bib",
    help="Output file. (default: 'dissertation.bib')",
)
@click.option(
    "--dois_yaml",
    default="bib.yaml",
    help=(
        "The `key: doi` YAML file, may contain wildcards (*). "
        "(default: 'bib.yaml', example: '*/*.yaml')"
    ),
)
@click.option(
    "--replacements_yaml",
    default=None,
    help=(
        "Replacements to perform, might be None. "
        "(default: None, example: 'replacements.yaml')"
    ),
)
@click.option(
    "--static_bib",
    default=None,
    help=(
        "Static bib entries, might be None, may contain wildcards (*). "
        "(default: None, example: 'chapter_*/not_on_crossref.bib')"
    ),
)
@click.option(
    "--doi2bib_database",
    default="yaml2bib-doi2bib.db",
    help=(
        "The doi2bib database folder 📁 to not query doi.org more than needed. "
        "(default: 'yaml2bib-doi2bib.db')"
    ),
)
@click.option(
    "--crossref_database",
    default="yaml2bib-crossref.db",
    help=(
        "The Crossref database folder 📁 to not query crossref.org more than needed. "
        "(default: 'yaml2bib-doi2bib.db')"
    ),
)
@click.option(
    "--email",
    default="anonymous",
    help=(
        "E-mail 📧 for crossref.org, such that one can make more API calls "
        "without getting blocked. (default: 'anonymous', example: 'bas@nijho.lt')"
    ),
)
def cli(
    bib_fname,
    dois_yaml,
    replacements_yaml,
    static_bib,
    doi2bib_database,
    crossref_database,
    email,
):
    click.echo(
        "Convert a yaml file to bib file with the correct journal abbreviations."
    )

    yaml2bib(
        bib_fname=bib_fname,
        dois_yaml=dois_yaml,
        replacements_yaml=replacements_yaml,
        static_bib=static_bib,
        doi2bib_database=doi2bib_database,
        crossref_database=crossref_database,
        email=email,
    )


if __name__ == "__main__":

    cli()
