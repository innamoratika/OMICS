# Introduction

This week we will look at different ways of counting reads in an alignemnt.
We'll look at both coverage estimates and how to use `samtools coverage`.

# Learning Objectives

* Estimate genomic coverage based on read-counts.
* Relate the major steps of a sequence alignment using `bwa`.
* Measure coverage using *samtools view* and *samtools coverage*.
* Extract coverage metrics for genes of interest.
* View pileups at specific genomic locations.
* Generate consensus sequences.

# Assignment

For the assignment you will repeat the excercise we performed in class on a new gene.

See [`assignment.md`](assignment.md) for details.

# Project

Align your reads, if they are not already.
Generate coverage estimates based on the number of reads and your genome size.
Then, use `samtools consensus` to observe the coverage across the different chromosomes.
Use the binned histogram, are there an notable "holes" in your alignments?

Update your project folder with the commands you used and the results you observed.
If your readme is getting long, try splitting the information across multiple files and using links to direct a person around.