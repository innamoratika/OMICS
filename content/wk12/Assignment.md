# Intro to Microbiome Analysis

## Introduction

Microbiome analysis is the study of the composition of microbial organisms that 
make up a community in some region. The region can be anything from lake beds, atmosphere,
soil, tap water, to oral swabs.  Microbiome analysis has become popular over the last decade
or so, however misunderstandings about the underlying data are common.

## Learning Objectives

### Microbiome Sequence Clustering

By the end of class today you should be able to comfortably answer these questions:
1.	Explain what a 'molecular diagnostic' is in the context of microbiome analysis and how does that differ from a traditional microbial presence assay?
2.	Define what gene is most commonly used to identify if an organism is present in some sample?
3.	Name three important characteristics about why this gene is used.
4.	Understand the basic laboratory process required to sequence a microbiome.
5.	Define PCR, and be able to describe the steps.
6.	Identify some potential pitfalls one could encounter because of the PCR step?
7.	Discuss how properties of the 16S gene can be problematic in DNA sequencing.
8.	Define an 'OTU' and why have people traditionally used it, rather than simply counting identical sequences?
9.	Classify the important filetypes to know and understand for OTU clustering?
10.	Understand how OTU clustering is performed, and execute on sequence data.
11.	Understand and perform taxonomic assignment.
12.	Define the steps required to create an OTU table.
13. Differentiate alpha, beta, and gamma diversity metrics and discuss what they attempt to measure? (maybe next week)

### Linux Skillz

Linux is great about making long commands shorter, and simple tasks easy. Lets learn/practice more
1. Soflinks! What are they? Why are they great and you should always use them? `man ln`
2. `grep` Do you know grep?  You should know grep.  Grep searches files for strings. A classic for a reason. `man grep`
3. `cut`  cut can slice columns out of a table. `man cut`
4. `column` column is a command in linux that formats tables 'nicely' `man column`
5. `alias` - tired of writing the same long command over and over? Let's alias it `man alias`
6. `id` What is your username?? (i.e. "What do I put when it says (YOUR USERNAME)?") plus more!


## Datasets and Binaries

* Data is located here:
	- `~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq`
	- `~/share/courses/OMICS/wk12_dataset/16sMicrobial_ncbi_lineage_reference_database.udb`
	- `~/share/courses/OMICS/wk12_dataset/rdp_gold.fa`

* Binary needed for this is located here:
	- `~/share/courses/OMICS/wk12_dataset/usearch8.1.1861_i86linux64`

# Walkthrough

Some of the data we are going to be using takes long paths, and it is a pain to write those over and over.
Let's fix that with a few steps.

1. Bin Directory
	- You can (and should) make a bin directory in your home folder.  This directory is automatically added to your path when you log in.
	- `mkdir ~/bin`
	- To reload your environment run this command (this is called 'sourcing' the profile file):
	- `. ~/.profile`
	- You should now see a bin directory in your home folder:
	- `ls ~`

2. Softlink
	- At this point you could copy the binary file ~/share/courses/OMICS/wk12_dataset/usearch8.1.1861_i86linux64 into your bin, but that is still a long command to write.  I'm lazy, so I like to create 'softlinks' (think of these like shortcuts) and name them something short and easy. Lets make the command just 'usearch':
	- `ln -s ~/share/courses/OMICS/wk12_dataset/usearch8.1.1861_i86linux64 ~/bin/usearch`
	- Test that by running this command:
	- `usearch --version`
	- How would you softlink the data file (~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq) to your sandbox directory?
	- Softlink the data file so that it is a link in your sandbox called `seqs.fq`

3. Sandbox
	- Make the directory using the make command from the wk12 directory:
	- `make mk_sandbox`

4. Alias
	- It's a pain changing directories with long path names.  Let's make an alias to shorten that up a little.
	- `alias sand='cd ~/share/omics_sandbox/wk12/(YOUR USERNAME)/'`
	- (hint: if you don't know your username, try the command `id`!)
	- Now you can just type `sand` and it will bring you to your sandbox location

5. Dereplicate
	- Dereplicate your sequences with this command:
	- `usearch -derep_fulllength seqs.fq -fastaout seqs_derep.fa -sizeout`
	- What is dereplicating??

6. Cluster OTUs
	- Cluster the sequences together so all sequences that are 97% identical are collapsed into one representative:
	- `usearch -cluster_otus seqs_derep.fa -otus otu.fa -uparseout uparse.up -relabel OTU_ -sizein -sizeout`

7. Chimeras AGAIN
	- Chimeras do get removed in the previous step, based on a voting majority/sequence similarity (remember it is matching against all OTU reps)
	- It is safer to perform another chimera removal step using a high quality database
	- Let's softlink the **~/share/courses/OMICS/wk12_dataset/rdp_gold.fa** file in the sandbox 
	- `usearch -uchime_ref otu.fa -db rdp_gold.fa -strand plus -nonchimeras no_chimeras.fa -chimeras chimeras.fa -uchimeout uchime_output.tsv`

8. Taxonomic classification
	- AKA "what the heck are these things?"
	- Oh god, my eyes! This path is way to long, softlink this file to your sandbox as '16S_db.udb': **~/share/courses/OMICS/wk12_dataset/16sMicrobial_ncbi_lineage_reference_database.udb**
	- `usearch -utax no_chimeras.fa -db 16S_db.fa -utaxout otu.utax -utax_cutoff 0.8 -strand both`

# Tests

1. What is the output of this command?
	- `usearch --version`

2. Softlink the datafile ~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq so that it is ~/share/omics_sandbox/wk12/user/seqs.fq
	- To test this run:
	- `ls -lh ~/share/omics_sandbox/wk12/(YOUR USERNAME)/`
	- How is 'seqs.fq' represented in the directory? (copy/paste on the next line)

3. How many sequences are in the seqs.fq file? (hint - what's that command that searches for things in files?)
	- write your command and the result

4. After running the dereplicate command (step 5 in the walkthrough), a 'size' variable is added to the fasta header in the file **seqs_derep.fa**
	- what does that represent?
	- what relevance does this have for the otu clustering step?

5. After running the dereplicate command (step 5 in the walkthrough), how many sequences exist in the output fasta file **seqs_derep.fa**?
	- what is the command you use to calculate this, and its result?

6. After clustering OTUs (step 6 in the walkthrough), how many sequences exist in the output fasta file **otu.fa**?

7. What is a 'chimera' and how many were found in this dataset after step 6?

8. After step 7 how many additional Chimeras were found?

9. After step 8, what are the top 20 organisms found in this dataset?


