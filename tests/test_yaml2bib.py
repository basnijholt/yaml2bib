import yaml2bib


def test_import():

    yaml2bib.yaml2bib(
        bib_fname="tests/example.bib",
        dois_yaml="tests/example.yaml",
        replacements_yaml="tests/replacements.yaml",
        static_bib="tests/not_on_crossref.bib",
        doi2bib_database="tests/yaml2bib-doi2bib.db",
        crossref_database="tests/yaml2bib-crossref.db",
        email="basnijholt-yaml2bib@github.com",  # fake email
    )
