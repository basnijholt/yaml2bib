# `yaml2bib`: Convert a `yaml` file to `bib` file with the correct journal abbreviations using only `DOI`s

[![license](https://img.shields.io/github/license/basnijholt/yaml2bib)](https://github.com/basnijholt/yaml2bib/blob/master/LICENSE)
[![tests](https://github.com/basnijholt/yaml2bib/workflows/tests/badge.svg)](https://github.com/basnijholt/yaml2bib/actions?query=workflow%3Atests)
[![codecov](https://img.shields.io/codecov/c/github/basnijholt/yaml2bib)](https://codecov.io/gh/basnijholt/yaml2bib)
[![docs](https://img.shields.io/readthedocs/yaml2bib)](https://yaml2bib.readthedocs.io)
[![version](https://img.shields.io/pypi/v/yaml2bib)](https://pypi.org/project/yaml2bib/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yaml2bib)](https://pypi.org/project/yaml2bib/)

### Install
```bash
pip install yaml2bib
```

## Usage
Use as command line tool
```bash
Usage: yaml2bib [OPTIONS]

Options:
  --bib_fname TEXT          Output file. (default: 'dissertation.bib')
  --dois_yaml TEXT          The `key: doi` YAML file, may contain wildcards
                            (*). (default: 'bib.yaml' ,example: '*/*.yaml')
  --replacements_yaml TEXT  Replacements to perform, might be None. (default:
                            None, example: 'replacements.yaml')
  --static_bib TEXT         Static bib entries, might be None, may contain
                            wildcards (*). (default: None, example:
                            'chapter_*/not_on_crossref.bib')
  --doi2bib_database TEXT   The doi2bib database folder 📁 to not query doi.org
                            more than needed. (default: 'yaml2bib-doi2bib.db')
  --crossref_database TEXT  The Crossref database folder 📁 to not query
                            crossref.org more than needed. (default:
                            'yaml2bib-doi2bib.db')
  --email TEXT              E-mail 📧 for crossref.org, such that one can make
                            more API calls without getting blocked. (default:
                            'anonymous', example: 'bas@nijho.lt')
  --help                    Show this message and exit.
```

Example invocation for my [thesis](https://gitlab.kwant-project.org/qt/basnijholt/thesis-bas-nijholt):
```bash
yaml2bib \
  --bib_fname "dissertation.bib" \
  --dois_yaml "*/*.yaml" \
  --replacements_yaml "replacements.yaml" \
  --static_bib "chapter_*/not_on_crossref.bib" \
  --email "bas@nijho.lt"
```

or as a library:
```python
from yaml2bib import yaml2bib

yaml2bib(
    bib_fname="dissertation.bib",
    dois_yaml="*/*.yaml",
    replacements_yaml="replacements.yaml",
    static_bib="chapter_*/not_on_crossref.bib",
    email="bas@nijho.lt",
)
```

## License
MIT License

## Contributions
- Bas Nijholt
