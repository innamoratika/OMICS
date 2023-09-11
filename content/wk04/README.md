# Week 4 - Alignment

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Review Material](#review-material)
4. [Lecture Material](lecture.md)
4. [Assignment](assignment.md)
5. [Project](#project)

## Introduction

This week, we will focus on aligning reads to a reference.
This is a crucial first step in almost all OMICS procedures.
Upon completion, we will have an alignment file that indicates where each read aligns to a reference genome and how it does so.

We will continue to use the [Snowflake Yeast Datset](/datasets/PRJNA943273-snowflake-yeast.md).

## Learning Objectives

By the end of this week, students should be able to:

* Understand the Burroughs-Wheeler Alignment (BWA) algorithm and its applications.
* Differentiate between BWA and other alignment algorithms (like BLAST).
* Understand why we **should not** put large result-files into git repos.
* Understand the purpose of generating alignment indexes.
* Use `samtools` to view and count the number of aligned reads.
* Use `samtools flagstat` to summarize an alignment result.
* Understand the important fields of a `SAM` format.

## Reading Material

## Assignment

For this assignment, you will use BWA to align Illumina reads from a sequencing of multi-cellular snowflake yeast.
In future weeks these results will be identify variants that may be associated with multicellularity.
Finally, you will interpret the results of the alignment.

## Project

This week is data week.

Work with Will and Deb to get sequence data onto Mistake-Not.
* `sra-utils` if available there.
* `wget` from the web.
* Or work with data on _CAMP_ server.

Also, get the appropriate geneome for mapping.

Remember, these files **should not** be in this `git` repo. 
They should be at another path on your `~`.
Perhaps:

* `~/data/references/{name}.fasta` - for your reference file.
* `~/data/{project-name}/reads/{sample_name}-R1/R2.fq.gz` - for your read files.

When you are done.
In your project directory write a new markdown file `data.md`.
In it, describe your data.

* What is it?
* Where did you get it?
* Add relevant references.
* Describe the organization of the files.
* Etc.

Make it a nicely formatted markdown file.

Add a brief description of your data and file organization to your project `README.md` and then create a link to the `data.md` file.