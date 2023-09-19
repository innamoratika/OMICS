# Week 4: The Counting

## Preamble

### Links

Links between two branches of the file tree.
They're the linux equivellent of "shortcuts".

There are two main types: _hard_ and _soft_.

**Hard Links**
A hard link is essentially a mirror copy of the original file.
Both the original and the hard link share the same inode and data blocks.
Any changes made to the original file or the hard link are reflected in the other.
Deleting one does not affect the other because they share the same content.
However, hard links cannot span different file systems or volumes and cannot link to directories.

**Soft Links**
A soft link (also known as a symbolic link or symlink) is a special kind of file that points to another file or directory.
It is essentially a shortcut.
Unlike a hard link, a soft link does not share the same inode as the original file.
If the original file is deleted, the soft link becomes a broken link.
Soft links can span different file systems and can link to directories.

Which one you use depends a bit on your setup and your intent.
We want to make it so we don't have to type long system paths like `/data/share/courses/OMICS/SGD`.
And we want to link to directories, not files.
So, we want soft-links.

Create a set of soft links in your `~/common/` directory to avoid duplication across the system.

```bash
mkdir -p ~/common/refs  # Make a directory, ignore if its already there.
cd ~/common/refs

# Create a link between my index and a place in your home path
ln -s /data/share/courses/OMICS/SGD SGD

# What does that look like?
ll .

```

We can also create a link to the snowflake dataset.

```bash
cd ~/common/
ln -s /data/share/courses/OMICS/PRJNA943273 snowflake_yeast

ll snowflake_yeast/
```

Now that we have our linked files we can all us the same files without duplication.

## Coverage Estimation

We can estimate the genomic coverage based on the genome size and the number of sequenced bases.

Genome size: 12,157,105 bp
```bash
seqkit stats ~/common/refs/SGD/bwaindex/R64.fasta

file                format  type  num_seqs     sum_len  min_len    avg_len    max_len
bwaindex/R64.fasta  FASTA   DNA         17  12,157,105   85,779  715,123.8  1,531,933
```

Reads: 1,108,796,340 + 1,108,001,476 
```bash
seqkit stats ~/common/snowflake_yeast/reads/SRR23803536_*.fastq 
file                                                                 format  type   num_seqs        sum_len  min_len  avg_len  max_len
/home/jupyter-will/common/snowflake_yeast/reads/SRR23803536_1.fastq  FASTQ   DNA   9,104,386  1,108,796,340       35    121.8      151
/home/jupyter-will/common/snowflake_yeast/reads/SRR23803536_2.fastq  FASTQ   DNA   9,104,386  1,108,001,476       35    121.7      151
```

Mean coverage ~= sequenced-bases/genome-size.

Mean coverage ~= 184X

This has a lot of assumptions baked in:
* All bases of all reads map and have good quality scores
* 184X is the _average_. Some will have much more, some will have much less.


The number of times each base is sequenced is governed by the _Poisson_ distribution.

As a demontration I've included a small python script for estimating the coverage rate for different conditions.

```bash
cd ~/repos/OMICS/content/wk05/
python cov_estimate.py -h

# Using our estimate from above
python cov_estimate.py --estimated_coverage 180
With 180.00X coverage.
X>0 100.00%
X>5 100.00%
X>10 100.00%
X>50 100.00%
```

### Activity

This means that 100% of bases will be covered more than zero times.
Even 100% of sites will have >50X coverage.

Let's pick a more typical range.
Let's say we wanted to run 4 replicates of our 12M yeast genome different Illumina platforms.

| Platform | Yield |
|----------|-------|
| iSeq     | 1.2G  |
| MiniSeq  | 7.5G  |
| MiSeq    | 15G   |
| NextSeq  | 120G  |

Let's use the tool to decide which sequencer to use.

## Alignments

Now, to actually align.

Magic command to break down.

```bash
bwa mem index.fasta reads/run_1.fastq reads/run_2.fastq | samtools view -b | samtools sort > aligned/run.sorted.bam
samtools index aligned/run.sorted.bam
```

This command does a number of things:

1. `bwa mem index.fasta reads/run_1.fastq reads/run_2.fastq`: Aligned the paired end reads of `run` to the `index.fasta`. This generates a `SAM` formatted stream of data.
2. `samtools view -b`: While SAM is useful for reading it is incredibly ineffecient in both space and time. This command converts the incoming stream in `SAM` format into an outgoing stream in `BAM` format, its binary equivellent. This drastically compresses it.
3. `samtools sort`: This takes an incoming **`BAM`** stream and creates a stream of the data sorted by genomic position (by default).
4. `> aligned/run.sorted.bam`: Writes the final sorted bam stream into a file for later use.
5. `samtools index aligned/run.sorted.bam`: Create an index file `aligned/run.sorted.bam.bai` that allows rapid position-based lookup of reads.


This is how we often "park" our data for later use.
Because it is indexed, it is easy (for other programs) to lookup reads by location and perform calculations.
The binary format drastically reduces the size and allows for even more compression.
If we _wanted_ the fastq files, we can always regenerate them from _these_ files.

Running this across all of the snowflake yeast data took Mistake-Not ~4 hours.

## Measuring Coverage

`samtools coverage` is a command for inspecting coverage across the genome.
When you add `--histogram` it will show you visual breakdown.

```bash
samtools coverage --histogram ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam
```

```raw
NC_001133.9 (230.2Kbp)
>  90.00% │██   ▄██████████████████████████▇████▆█    ██ │ Number of reads: 281262
>  80.00% │██   ██████████████████████████████████   ▄██ │     (456 filtered)
>  70.00% │██▂  ██████████████████████████████████▄  ███ │ Covered bases:   213.4Kbp
>  60.00% │███  ███████████████████████████████████ ████▆│ Percent covered: 92.68%
>  50.00% │███  ███████████████████████████████████ █████│ Mean coverage:   140x
>  40.00% │███ ▁███████████████████████████████████▇█████│ Mean baseQ:      37.9
>  30.00% │███ ██████████████████████████████████████████│ Mean mapQ:       49.8
>  20.00% │███ ██████████████████████████████████████████│ 
>  10.00% │███▃██████████████████████████████████████████│ Histo bin width: 5.0Kbp
>   0.00% │██████████████████████████████████████████████│ Histo max bin:   100%
          1       50.0K     100.1K    150.1K          230.2K 

```

### Activity

How can we inpsect a particular gene of interest?
For this, let's look for the Calmodulin gene `CMD1`.

How could we find where `CMD1` is in the SGD genome?

```bash
ll ~/common/refs/SGD/annotations/

less ~/common/refs/SGD/annotations/genomic.gff
```

These files contain the gene & transcript information for the genome.
We can use `grep` to search it.

```bash
grep -i "gene=CMD1" ~/common/refs/SGD/annotations/genomic.gff
```

Using `samtools view`
```bash
# Inspect reads
samtools view ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001134.8:457919-458362 | head
...

# Count reads
samtools view -c ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001134.8:457919-458362
786
```

Using `samtools coverage`

```bash
samtools coverage -r NC_001134.8:457919-458362  ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam 
```

|rname       | startpos | endpos | numreads | covbases | coverage | meandepth   | meanbaseq | meanmapq
|------------|----------|--------|----------|----------|----------|-------------|-----------|---------
|NC_001134.8 | 457919   | 458362 | 786      | 444      |  100     | **173.142** | 38.2      | 60

That 173X coverage is very close to our 180X estimate.

I can *look* at these sequences a few ways.

```bash
samtools view ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001134.8:457919-458362 | less
```

This will let me flip through reads, but it is hard to see how each base corresponds.
What if we wanted to see the bases as they align to the reference.
This is called a `pileup`

```bash
samtools consensus -r NC_001134.8:457919-458362 -f pileup ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam | less

NC_001134.8     457919  0       158     C       503     CCCCccCCccccCcCCCcCcCcCCccCcCcCCccCCccCcCCccCCcccCccCCcCcCccCCCccCcCCcCcCCCcccCCccccCCCCccCCCccCCcCccCCccccCcCcCcCcCCCCcCcCCCcCcCCCCCCcccCcCCcCCCccCCcccCCcCcc      GGIIIAGIGGGGIIG.IAIGIIIIGAAGIGGIAGGG<II<IGIIIIGGIGIAIGAIGIIGIIGIIGGIGIIGIIGGGIGGGIIIIIIIIIGIIGIIIGGGGIGIIGGIGGIIIGAIIIAGIGIIIGIGIGGGII<GIIGIIIGIGGGIGIAGIGIAGG
NC_001134.8     457920  0       158     T       503     TTTTttTTttttTtTTTtTtTtTTttTtTtTTttTTttTtTTttTTtttTttTTtTtTttTTTttTtTTtTtTTTtttTTttttTTTTttTTTttTTtTttTTttttTtTtTtTtTTTTtTtTTTtTtTTTTTTtttTtTTtTTTttTTtttTTtTtt      GGGIGGGGGGGAIIGAGAIGIIGG.GGGIIIIGAGG.GGGIIGIGIGGIGIGIAGIIIIGIIIIIGIGIGIAGIGGIGGIIGIGIGIIGGIIIGGIGGGGGIGIIIGIGGGIIGGIIIGIIIIGIIIGIAGGGI.GGIIGIGGIGGGIAIGGIGIGII
NC_001134.8     457921  0       161     A       512     AAAAaaAAaaaaAaAAAaAaAaAAaaAaAaAAaaAAaaAaAAaaAAaaaAaaAAaAaAaaAAAaaAaAAaAaAAAaaaAAaaaaAAAAaaAAAaaAAaAaaAAaaaaAaAaAaAaAAAAaAaAAAaAaAAAAAAaaaAaAAaAAAaaAAaaaAAaAaaAAa   GGIIGAGIIGIIGGGGGGIGIIGGGGGGIIGIGGGGAIGGIIIGGIGIIIIAGGIIIIIGIIIIIGIIGGIGIGGGIGIIIGIGIGGGIGIIIIIIIG.GIIGIIGGIGGGGGIGIIGIGIGIIGIIGIAIIIIGGIIIGIIGGIGGIGIGGIIIAIGA.G
```

We can also ask for the consesus sequence as either fasta or fastq.

```bash
samtools consensus -r NC_001134.8:457919-458362 -f fasta ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam
```

We can also grab that sequence from the reference with `samtools faidx`.

```bash
samtools faidx ~/common/snowflake_yeast/refs/SGD/bwaindex/R64.fasta NC_001134.8:457919-458362
```
