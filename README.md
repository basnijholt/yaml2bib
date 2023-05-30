# 📘 `yaml2bib`: Convert YAML to BibTeX with Correct Journal Abbreviations Using Only DOIs 🚀

[![license](https://img.shields.io/github/license/basnijholt/yaml2bib)](https://github.com/basnijholt/yaml2bib/blob/main/LICENSE)
[![tests](https://github.com/basnijholt/yaml2bib/workflows/pytest/badge.svg)](https://github.com/basnijholt/yaml2bib/actions?query=workflow%3Apytest)
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

Check out the help message `yaml2bib --help`:

<!-- CODE:BASH:START -->
<!-- echo '```bash' -->
<!-- yaml2bib --help -->
<!-- echo '```' -->
<!-- CODE:END -->
<!-- OUTPUT:START -->

<!-- OUTPUT:END -->

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
