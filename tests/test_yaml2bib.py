"""Tests for yaml2bib."""

import yaml2bib


def test_yaml2bib() -> None:
    """Test yaml2bib on examples."""
    yaml2bib.yaml2bib(
        bib_fname="examples/example.bib",
        dois_yaml="examples/example.yaml",
        replacements_yaml="examples/replacements.yaml",
        static_bib="examples/not_on_crossref.bib",
        doi2bib_database="examples/yaml2bib-doi2bib.db",
        crossref_database="examples/yaml2bib-crossref.db",
        email="basnijholt-yaml2bib@github.com",  # fake email
    )
