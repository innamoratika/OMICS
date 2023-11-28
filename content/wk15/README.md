
# Introduction

A large portion of all OMICS analysis boils down to performing different techniques on count tables.  But to get count tables, we usually have to do some kind of sequencing, and DNA sequence is rich with information.  This class we are going to be taking a step back and seeing the kinds of analysis that can be done using the sequences that were created in the process of doing our microbiome analysis. 

# Learning Objectives

### Microbiome Sequence Analysis

By the end of class today you should be able to comfortably discuss these topics/answer these questions:
1. _Apply_ linux commands to generate sequence alignments
1. _Define_ the steps required to create a phylogenetic tree
1. _Define_ alpha, beta, and gamma diversity metrics and discuss what they attempt to measure?
1. _Apply_ your knowledge of linux to _define_ sequences that belong to an OTU, then extract them from the main sequences file
1. _Apply_ usearch to extract sequences that belong to individual species, from our taxonomy database
1. _Construct_ a phylogenetic tree of all OTU sequences.
1. _Use_ usearch to calculate unifrac diversity metrics
1. _Interpret_ the output distance matrix by plotting

### Linux Skillz

We will continue to use *linux* to shorten commands, and look at data
1. Soflinks! What are they? Why are they great and you should always use them? `man ln`
1. `grep` search files for strings of characters, incredibly useful `man grep`
1. `cut`  cut can slice columns out of a table. `man cut`
1. `column` column is a command in linux that formats tables 'nicely' `man column`
1. `alias` Alias allows you to create your own custom commands (run alone to list all aliases) `man alias`
1. `id` id shows your current id, and the numerical value associated with it by the linux system `man id`
1. `type` Check if a command name you want to use is already taken by the system `man type`
1. `head` and `tail` get lines from the top and bottom of a file, respectively
1. `wc` Count characters, words, and lines in your files "word count"
1. `sort` Sort elements in a file

# Reading Material

If you would like to know more about problems with [euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) as an ecology metric check [this out](https://davidzeleny.net/blog/2022/03/17/euclidean-distance-is-sensitive-to-double-zero-problem-while-hellinger-is-not-visualization/) 

# Assignment

Todays assignment is as much about continuing to learn about usearch, and how we can use it to examine microbiome data. 
Additionally we are getting into the weeds and adding more functions to our linux toolbox! See the Assignment.md file for details.