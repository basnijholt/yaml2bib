# `yaml2bib` example

This example is from the Introduction of "Towards realistic numerical simulations of Majorana devices" [(source)](https://github.com/basnijholt/thesis).

Run the example with
```bash
yaml2bib \
    --bib_fname example.bib \
    --dois_yaml example.yaml \
    --replacements_yaml replacements.yaml \
    --static_bib not_on_crossref.bib \
    --email basnijholt-yaml2bib@github.com
```

The input file is [`example.yaml`](example.yaml) and [`example.bib`](example.bib) is the output.
