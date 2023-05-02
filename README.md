# 📘 `yaml2bib`: Convert YAML to BibTeX with Correct Journal Abbreviations Using Only DOIs 🚀

[![license](https://img.shields.io/github/license/basnijholt/yaml2bib)](https://github.com/basnijholt/yaml2bib/blob/master/LICENSE)
[![tests](https://github.com/basnijholt/yaml2bib/workflows/tests/badge.svg)](https://github.com/basnijholt/yaml2bib/actions?query=workflow%3Atests)
[![codecov](https://img.shields.io/codecov/c/github/basnijholt/yaml2bib)](https://codecov.io/gh/basnijholt/yaml2bib)
[![docs](https://img.shields.io/readthedocs/yaml2bib)](https://yaml2bib.readthedocs.io)
[![version](https://img.shields.io/pypi/v/yaml2bib)](https://pypi.org/project/yaml2bib/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yaml2bib)](https://pypi.org/project/yaml2bib/)

Introducing 🌟 `yaml2bib`, an easy-to-use and powerful Python library and command-line tool that seamlessly converts YAML files to BibTeX format, all while maintaining the correct journal abbreviations using only DOIs! 🎉
Whether you're a researcher or a student, `yaml2bib` will simplify and streamline your bibliography management process. With an intuitive interface, customizable options, and compatibility as both a library and a command-line tool, it's never been more convenient to create and maintain your citation records.
Say goodbye to manual conversions and hello to `yaml2bib`! 🚀

### 🛠️ Installation

```bash
pip install yaml2bib
```

## 🚀 Usage

### Command Line Tool

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

Example invocation for Bas Nijholt's [thesis](https://github.com/basnijholt/thesis):

```bash
yaml2bib \
  --bib_fname "dissertation.bib" \
  --dois_yaml "*/*.yaml" \
  --replacements_yaml "replacements.yaml" \
  --static_bib "chapter_*/not_on_crossref.bib" \
  --email "bas@nijho.lt"
```

### Python Library

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

## 🌟 Full Example

Check out the [`examples`]([https://github.com/basnijholt/yaml](https://github.com/basnijholt/yaml)

Convert with:

```bash
yaml2bib \
  --bib_fname "example.bib" \
  --dois_yaml "example.yaml" \
  --replacements_yaml "replacements.yaml" \
  --static_bib "not_on_crossref.bib" \
  --email "bas@nijho.lt"
```
