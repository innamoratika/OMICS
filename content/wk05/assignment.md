# Alignments

## Datasets

Use the dataset `~/common/snowflake_yeast/aligned/SRR23803537.sorted.bam` for these questions.

You may also need the following files:
* `~/common/refs/SGD/annotations/genomic.gff`
* `~/common/snowflake_yeast/refs/SGD/bwaindex/R64.fasta`

# Walkthrough

Save your answers in `content/wk05/{userid}_notes.md`.

Get a random gene from the gff annotation file we used

```bash
shuf -n 1 ~/common/refs/SGD/annotations/genomic.gff
```

What gene did you get?
Put it in the notes.
Do a quick internet search. Is there anything interesting about it?


## Coverage

Measure the coverage of the gene using `samtools view` and `samtools coverage`.

In your notes include which commands you used and what output you saw.
Include the `--histogram` image in your markdown notes.

## Consensus

Calculate the consensus of your gene and save it as `content/wk05/{userid}_gene_cons.fasta`.

Extract the reference sequence and note any variants in your notes.