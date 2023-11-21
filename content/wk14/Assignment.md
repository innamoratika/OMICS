# Intro to Microbiome Analysis

## Introduction

Microbiome analysis is the study of the composition of microbial organisms that 
make up a community in some region. The region can be anything from lake beds, atmosphere,
soil, tap water, to oral swabs.  There are many organisms that can be measured in a microbiome
however we will be focusing on bacteria.  This requires us to identify a 'marker gene', in 
our case we will be using the whole 16S subunit of the Ribosome

## Learning Objectives

### Microbiome Sequence Clustering

By the end of class today you should be able to comfortably answer these questions:
1. _Apply_ linux to create even more shortcuts
1. _Define_ the steps required to create an OTU table.
1. _Differentiate_ alpha, beta, and gamma diversity metrics and discuss what they attempt to measure?
1. _Apply_ your knowledge of linux to calculate gamma diversity
1. _Apply_ usearch to calculate two alpha diversity metrics
1. _Apply_ usearch to calculate two beta diversity metrics

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

1. Moar linux!
	- Last class we learned about aliases and softlinks, which are incredibly handy.
	- Sometimes it is necessary to have something similar to a softlink, but more flexible.
	- Lets learn about _bash variables_
	- But first, create our new workspace (pull down the most recent OMICS github, then go to the wk14 directory)
		- `make mk_sandbox`
	- Next lets again make it easy to get to our sandbox (the working directory for this week) with an alias
		- `alias sand='cd ~/share/omics_sandbox/wk14/(YOUR USERNAME)/'`
		- remember `id` if you've forgotten your username!
	- We can store arbitrary strings in variables in our bash environment. Aliases and softlinks are great, 
	- but what if we don't even want to remember the path to where we put our softlink? Let's make a bash variable
	- that corresponds to last week's assignment, so it is easy for us to access the files we made last week.
		- `wk12=~/share/omics_sandbox/wk12/(YOUR USERNAME)`
	- Linux variables are accessed by prefixing the variable name with a '$', so try this command:
		- `ls $wk12`
	- Last week we ended our analysis when we had calculated (hopefully) chimera-free OTU sequences.
	- a la Voltron, let's combine our linux powers and softlink last week's chimera-free OTU file in the wk14 directory:
		- `ln -s $wk12/no_chimeras.fa no_chimera_otu.fa` (while in the wk14 sandbox directory)
		- even less typing. cool, eh?
		- link the seqs file to this directory as well:
		- `ln -s $wk12/seqs.fq` 
		- hey, but that already WAS a softlink? yes you can soflink softlinks.  Just don't delete any in the chain or they will break ;-)

1. Calculate OTU table
	- We have our OTU candidates, but we don't know the counts per sample. Let's calculate a table!
	- In order to do that, we need to realign each sequence to each OTU.  Let's do that.
		- `usearch -usearch_global seqs.fq -db no_chimera_otu.fa -otutabout otutab.tsv -strand plus -id 0.97`
	- NOTE: This command is different in later versions of usearch

1. Examine Results
	- open the file with less
		- `less -S otutab.tsv`
		- Even with the `-S` parameter, it is still really hard to read.  This is because the size of the sample headers
		is much larger than the size of the numbers of each OTU.  Let's fix that so we can read what numbers go with what
		samples. Enter `column`, an extremely handy command to know when looking at variable separated files
		- `column -t otutab.tsv|less -S`
		- much better!  Except... the first column is labelled '#OTU ID' which is a horrific column name. It has special 
		characters (the '#') and includes a space. **NEVER** name you columns like that - linux hates those.  But we an 
		accommodate them with a special flag:
		- `column -ts $'\t' otutab.tsv |less -S`
		- This is getting a little beyond the scope of what we can cover here, but basically it is forcing column to split
		on tabs, not on just whitespace.  Now you can read the table more clearly!

1. Basic Stats
	- Lets use a linux command to calculate the number of OTUs in the file.  **TIMTOWTDI**
	- Use grep!
		- `grep -c '>' no_chimera_otu.fa` This will count the number of times '>' is found, 
		which is the record separator for fasta files
		**WARNING** the '>' character is problematic here, we have to quote it: why?
	- Use a combo of `head` (or tail) and `wc`
		- `head -n -1 otutab.tsv |wc -l` This counts every line in a file, except the first one

1. Alpha Diversity
	- What is it?  
	- In order to do the rest of this class we'll need a more recent version of usearch. 
		- `ln -s ~/share/courses/OMICS/wk14_dataset/usearch11.0.667_i86linux32 ~/bin/usearch11`
		- `usearch11 --version` (make sure this works, else your softlink is wrong)
	- Calculate a boatload of alpha diversity metrics:
		- `usearch11 -alpha_div otutab.tsv -output alpha.tsv` 
	- Examine the file with `less`
		- `less -S alpha.tsv` This looks terrible! How can we view it as a nicely formatted table?
	- Pull out just the Sample label, and 'richness' columns
		- `cut -f1,10 alpha.tsv |column -ts $'\t'|less -S`
	- Sort the table by richness:
		- `cut -f1,10 alpha.txt|sort -k2 |column -ts $'\t'|less -S` uh-oh, somethings wrong, it isn't 
		ordering correctly!  Try to fix in the exercises below


1. Beta Diversity:
	- What is it??
	- Let's calculate it on our samples:
		- `usearch -beta_div otutab.tsv -metrics euclidean,bray_curtis`


# Tests
1. I often use '.tsv' as the extension for many of the above files. Linux doesn't care what extensions files have, unlike windows
and other operating systems.  Why do you think I add '.tsv' instead of just '.txt' to my input/output files? (or even leave it off?)

1. Calculate the number of samples in your otu table
	- i.e. how many columns are there? (minus the first OTU ID column)

1. Alpha Diversity
	- Fix this command so it orders the table correctly:
		- `cut -f1,10 alpha.txt|sort -k2 |column -ts $'\t'|less -S` (Don't worry about the column header for this)
		- hint: `man sort`
	- Sort the whole table by the 'reads' column (the number of reads belonging to that sample)
	- Examine the 'richness' - is there any correlation between the number of reads ('observations') a sample has
	and the species richness?  What is it and why?  What test might you perform to see if there is a significant correlation?
	Why might a correlation be a problem in this kind of analysis? 

1. Gamma Diversity
	- Calculate the gamma diversity (richness) for this dataset

1. Beta Diversity
	- Examine the 'pretty' version of the sorted euclidean distance file - what is striking about the diagonal values?
	Explain why this phenomenon exists.
	(diagonal == starting in the top left and moving down-one, over-one)
	- What are two ways to present this data graphically?
	- Make a graph!  import either the euclidean or bray-curtis matrix into your favorite spreadsheet editor and calculate
	some representation of that measure.
	- Do the samples create separate groups? Do they not?  What does it say about the underlying sample data?