# Variant Calling

## Lay of the land

There are a number of variant callers regularly used today.
Each has advantages and disadvantages based on data source and application.

| Tool                            | Input Data  | Detectable Variants          |  Description 
|---------------------------------|-------------|------------------------------|------------
| bcftools                        | Illumina    | Small variants _some_ CNV    | The OG tool for variant calling. If there's nothing specific for your usecase, this is the default.
| Genome Analysis Toolkit (GATK)  | Illumina    | Small variants               | High quality filtering and data preparation tools, clinical labs
| Deep varaint                    | Illumina    | Small variants               | Google's deep-learning enabled variant caller. Highly accurate as long as it's human
| claire3                         | Ont/PacBio  | Small variants, large indels | Deep learning enhanced error profiles (Human only unless you bring your own gold-standard)
| CuteSV & Sniffles               | Ont/PacBio  | Large structural varaints    | New tools for detecting large structural variants from long-read data

And then there are a number of specialized tools for narrow usecases.
There are also hundreds of poorly supported tools released and not maintained.

## Variant Calling

The base command we'll work with:

```bash
cd ~/common

bcftools mpileup -r NC_001134.8 -Ou -f refs/SGD/bwaindex/R64.fasta snowflake_yeast/aligned/SRR23803536.sorted.bam | bcftools call -mv -Ob -o calls.bcf
```

Breaking it down:
* `bcftools mpileup -r NC_001134.8 -Ou -f ...R64.fasta ...SRR23803536.sorted.bam | ` - Create a _pileup_ file for the alignment against the refence.
* `bcftools call -mv -Ob -o calls.bcf` - Call using the multi-allelic model `-m` and write the variants to `calls.bcf`

This is a binary file much like `sam` -> `bam` there is a `vcf` -> `bcf`.

Let's look inside the file.

```bash
bcftools view calls.bcf | less -S
```

Notable things:
* It has a header similar to SAM file.
* That header contains information about the contents of the file. `##INFO=<ID=DP,Number=1,Type=Integer,Description="Raw read depth">`
* The data after the header is tab-delimited.
* Has fields for the location, an `ID`, the reference and alternate allele, quality scores, whether is passes `FILTER`, etc.
* The `INFO` field is a list like `{var}={value};{var}={value};`, the abbreviations come from the header.
* The final field is the call for this sample.

```
Allele-A  / Allele-B 
       0  /    1 :   
```

These variant files are a lot like SAM/BAM files (because they're from the same standards committee).

In general, all good variant callers export their data as `VCF` files.
You can also combine the outputs of multiple samples, and multiple tools into a single vcf file using `bcftools merge`.
Merging results from multiple tools is useful because different tools see different kinds of variants and have different error profiles.
Merging results from multiple samples is useful because many of the downstream GWAS tools can take advatange of information across multiple tools.
Lastly, storing, sharing, and visualizing variants is MUCH cheaper than storing bam files.

## Variant Stats

Finding some basic information about the file is easy once you understand the file.

```bash
 bcftools stats calls.bcf | less -S
```

This is a custom formatted file designed for easy `grep`ing.

The most common, is to ask for the _**S**ummary **N**umbers_

```bash
bcftools stats calls.bcf | grep '^SN'
```

## Variant Filtering

After you've done all of your calling and merging, you need to filter the variants.

In general, you want to filter on at least two things.
* Read-depth
* Quality score

Here is a link to the expression mini-language. https://samtools.github.io/bcftools/bcftools.html#expressions


```bash
bcftools filter -i "DP>=10&&QUAL>20" calls.bcf | less -S
```


```bash
bcftools filter -i "DP>=10&&QUAL>20" calls.bcf | bcftools stats | grep '^SN'
```

These final variants are what will go on for functional analysis.
Next, next week.


## Your first pipeline

We're going to take a detour into _basic_ script writing.
But even **basic** script writing can be powerful.

```bash
cd ~/repos/OMICS/content/wk06/

# Create a new script
touch variant_pipeline_{user_id}.sh

# make it executable
chmod +x variant_pipeline_{user_id}.sh
```

Next we can edit it.
Either with the terminal or the IDE.

In the file add:
```bash
#!/bin/bash

# Script for aligning and variant calling yeast sequence data
# variant_call path/to/reads_1 path/to/reads_2 path/to/variants.bcf

# Define some constants
REF=/data/share/courses/OMICS/SGD/bwaindex/R64.fasta
FILTER='DP>=10&&QUAL>20'

(bwa mem $REF $1 $2 |       
  samtools view --bam |    
  samtools sort |          
  bcftools mpileup -Ou -f $REF - |
  bcftools call -m |         
  bcftools filter -Ob -i $FILTER > $3)
```

Before we run, let's make a small test dataset for the pipeline.
The above command could take a while, and might have errors.
It is always useful to have a tiny version of your dataset for quick pipeline runs.

```bash
seqkit head -n 10000 /data/share/courses/OMICS/PRJNA943273/reads/SRR23803538_1.fastq > ~/common/test_r1.fq
seqkit head -n 10000 /data/share/courses/OMICS/PRJNA943273/reads/SRR23803538_2.fastq > ~/common/test_r2.fq
```

Running the pipeline.

```bash
./variant_pipeline_{user_id}.sh ~/common/test_r1.fq ~/common/test_r2.fq ~/common/test_calls.bcf
```

How do we view the results?