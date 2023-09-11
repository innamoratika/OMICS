# Basic Alignment

Read alignment serves as the foundation for nearly all OMICS techniques.

In our current task of variant-calling, it lines each read up with the most likely genomic origin.
Then, we can compare the sequence of the read with the reference to find variants.

In transcriptomics, which we'll cover later, reads are generated only from expressed mRNAs, alignment allows us to _count_ the number of expressed transcripts.
In ChIP pull-down experiments, only DNA attached to the protein of interest is sequenced, alignment gives us the binding map the the protein.
In ATAC-seq a TN5 only cuts exposed DNA, aligment of the reads tells us where the genome is open.

Everything starts with an alignment.

## Indexing

Searching a giant genome for a short inexact match is a computational complex problem.

Modern techniques employ an _indexing_ step in which computationally efficient _lookup-table_ is created.
This step is often computationally expensive in both time and space.
However, it only needs to be performed _once_ per genome (per search setting).
Then, it is loaded and rapidly searched in subsequent runs.

Each alignment tool has a different indexing strategy, but they all use it.

There are two alignment tools installed on this server.
 - `minimap2`
 - `bwa`
 
### Activity
 * Use the `--help` and `man` pages to learn how to create indexes for bwa and minimap2.
 * Make a directory _outside of your repo_, ie. `~/common/refs/` to put your indexes in.
 * Create a `bwa` index for `/data/share/courses/OMICS/SGD/chr1.fsa` in your `~/common/refs/` directory.


## Alignment

Now that we have an index, we need to align our sequences to that reference.

Magic command to try:
```bash
bwa mem ~/common/refs/SGD_chr1/chr1 /data/share/courses/OMICS/PRJNA943273/SRR23803536_1.fastq /data/share/courses/OMICS/PRJNA943273/SRR23803536_2.fastq | samtools view -q 20 | head -n 20
```

Breaking that down:

* `bwa mem {index} {stem}_1.fastq {stem}_2.fastq` - Align paired reads at `{stem}` to an `{index}`.
* `| samtools view -q 20` - Pipe the result into a program called `samtools` and `view` all those with a mapping quality over 20.
* `| head -n 20` - Only take the first 20 lines.

What we see on the terminal are the _alignments_ in a Sequence Alignment Maping `SAM` format.

In brief, it is a TSV file with the following columns:

1. `QNAME` - Query template NAME
2. `FLAG` - bitwise FLAG
3. `RNAME` - Reference sequence NAME
4. `POS` - 1-based leftmost mapping POSition
5. `MAPQ` - MAPping Quality
6. `CIGAR` - CIGAR string
7. `RNEXT` - Reference name of the mate/next read
8. `PNEXT` - Position of the mate/next read
9. `TLEN` - observed Template LENgth
10. `SEQ` - segment SEQuence
11. `QUAL` - ASCII of Phred-scaled base QUALity+33
12. `INFO` - A tab-split list of additional information.

The detailed specifications about the file can be found at [ht_specs](https://samtools.github.io/hts-specs/).
We'll cover relevant sections as needed.

`samtools` is a command-line program for performing various operations on sam/bam files.
Much like `seqkit`, it is a cli that has numerous sub commands for doing different things with sam files.

Type: `samtools` in your terminal to get a list of all of the operations.

Check out: `samtools view` and `samtools flagstat`

Let's align reads from our dataset.

### Activity

For time-considerations, we'll downsample our dataset before starting.

Each student should pick a different sample in `/data/share/courses/OMICS/PRJNA943273/`.

* Downsample the dataset using `seqkit`. Create pair of scratch files that are only the first 50,000 sequences.
* Align the downsampled reads to the chr1 index, save the result to a scratch `sam` file.
* Use `samtools flagstat` to describe the alignment result. How does the % aligned reads correspond with the size of chr1?


### Activity

Work with Will and Deb to get sequence data onto Mistake-Not.