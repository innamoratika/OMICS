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
3.	Name three important characteristics that explain why this gene is used.
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
	- You can (and should) make a bin directory in your home folder.
	- what/where is your home folder? Find out with this command: 
		- `echo $HOME`
	- These change directory commands are equivalent and all bring you to your home: 
		- `cd $HOME` `cd ~` or just `cd` ('~' is a shortcut for 'home' - you will see this a lot) 
	- The ~/bin directory is automatically added to your path when you log in, once it is made with this command:
		- `mkdir ~/bin`
	- To reload your environment run this command (this is called 'sourcing' the profile file):
		- `. ~/.profile` or `source ~/.profile`
	- You should now see a bin directory in your home folder:
		- `ls ~`
	- The `/home/(YOUR USERNAME)/bin` should now be part of your path:
		- `echo $PATH`

2. Softlink
	- At this point you could copy the binary file ~/share/courses/OMICS/wk12_dataset/usearch8.1.1861_i86linux64 into your bin,
 but that is still a long command to write.  I'm lazy, so I like to create 'softlinks' (think of these like shortcuts) and name them
 something short and easy. Lets make the command just 'usearch':
		- `ln -s ~/share/courses/OMICS/wk12_dataset/usearch8.1.1861_i86linux64 ~/bin/usearch`
Ran `ln --help` first; symbolic links are the same thing as soft links  
	- Test that by running this command:
		- `usearch --version`
returns 8.1.1861_i86linux64

3. Sandbox
	- Make the directory using the make command from the wk12 directory:
		- `make mk_sandbox`
	- What path is your sandbox?
		- **~/share/omics_sandbox/wk12/(YOUR USERNAME)/**
	- How would you softlink the data file (~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq) to your sandbox directory?
	- Softlink the data file so that it is a link in your sandbox called `seqs.fq`
`ln -s ~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq ~/share/omics_sandbox/wk12/jupyter-jcp362/seqs.fq`

4. Alias
	- It's a pain changing directories with long path names.  Let's make an alias to shorten that up a little.
	- `alias sand='cd ~/share/omics_sandbox/wk12/(YOUR USERNAME)/'`
	- (hint: if you don't know your username, try the command `id` or `echo $USER`!)
	- Now you can just type `sand` and it will bring you to your sandbox location

5. Dereplicate
	- Dereplicate your sequences with this command:
	- `usearch -derep_fulllength seqs.fq -fastaout seqs_derep.fa -sizeout`
	- What is dereplicating?
 Collapsing multiple reads with the exact same sequence into one sequence with a count number. Lossless; compresses read data. 
Seqkit stats says this went from 168,255 num_seqs to 157,474.  

6. Cluster OTUs
	- Cluster the sequences together so all sequences that are 97% identical are collapsed into one representative:
		- `usearch -cluster_otus seqs_derep.fa -otus otu.fa -uparseout uparse.up -relabel OTU_ -sizein -sizeout`

7. Chimeras AGAIN
	- Chimeras do get removed in the previous step, based on a voting majority/sequence similarity (remember it is matching against
 all OTU reps)
	- It is safer to perform another chimera removal step using a high quality database
	- Let's softlink the **~/share/courses/OMICS/wk12_dataset/rdp_gold.fa** file in the sandbox 
		- `ln -s ~/share/courses/OMICS/wk12_dataset/rdp_gold.fa ~/share/omics_sandbox/wk12/jupyter-jcp362/rdp_gold.fa`
- `usearch -uchime_ref otu.fa -db rdp_gold.fa -strand plus -nonchimeras no_chimeras.fa -chimeras chimeras.fa -uchimeout uchime_output.tsv`

8. Taxonomic classification
	- AKA "what the heck are these things/sequences?"
	- Oh god, my eyes! This path is way to long, softlink this file to your sandbox as
 '16S_db.udb': **~/share/courses/OMICS/wk12_dataset/16sMicrobial_ncbi_lineage_reference_database.udb**
	- `usearch -utax no_chimeras.fa -db 16S_db.fa -utaxout otu.utax -utax_cutoff 0.8 -strand both`
File '16S_db.fa' doesn't exist but I was able to do this with
 `usearch -utax no_chimeras.fa -db 16S_db.udb -utaxout otu.utax -utax_cutoff 0.8 -strand both`
# Tests

1. What is the output of this command?
	- `usearch --version`
'usearch v8.1.1861_i86linux64'

2. Softlink the datafile ~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq so that it is ~/share/omics_sandbox/wk12/user/seqs.fq
	- To test this run:
	- `ls -lh ~/share/omics_sandbox/wk12/(YOUR USERNAME)/`
	- How is 'seqs.fq' represented in the directory? (copy/paste on the next line)
'lrwxrwxrwx 1 jupyter-jcp362 jupyterhub-users   81 Nov 14 10:38 seqs.fq -> /home/jupyter-jcp362/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq'

3. How many sequences are in the seqs.fq file? (hint - what's that command that searches for things in files?)
	- write your command and the result
Command: `~/share/omics_sandbox/wk12/jupyter-jcp362$ seqkit stats seqs.fq`
Result: 
file     format  type  num_seqs      sum_len  min_len  avg_len  max_len
seqs.fq  FASTQ   DNA    168,255  245,599,437      503  1,459.7    1,872
Answer: 168,255 sequences

4. After running the dereplicate command (step 5 in the walkthrough), a 'size' variable is added to the fasta header in 
the file **seqs_derep.fa**
	- what does that represent? 
Number of replicate counts
	- what relevance does this have for the otu clustering step?
Sequences with high size are more likely to be organisms that exist rather than sequencing errors. 
The usearch otu clustering algorithm starts with the highest-size (most replicates) unique sequences. 

5. After running the dereplicate command (step 5 in the walkthrough), how many sequences exist in the output fasta file **seqs_derep.fa**?
	- what is the command you use to calculate this, and its result?
Command:`~/share/omics_sandbox/wk12/jupyter-jcp362$ seqkit stats seqs_derep.fa`
Result:
file           format  type  num_seqs      sum_len  min_len  avg_len  max_len
seqs_derep.fa  FASTA   DNA    157,474  229,869,083      503  1,459.7    1,872 
Answer: 157,474

6. After clustering OTUs (step 6 in the walkthrough), how many sequences exist in the output fasta file **otu.fa**?
file    format  type  num_seqs  sum_len  min_len  avg_len  max_len
otu.fa  FASTA   DNA        310  449,652      771  1,450.5    1,872

7. What is a 'chimera' and how many were found in this dataset after step 6?
Type of sequencing error - part of sequence is from one organism and part of sequence is from another.
Step 6 identified 1170 chimeras (0.7% of sequences). 

8. After step 7 how many additional Chimeras were found?
Identified 5 chimeras (305 non-chimeras and unclassified; 310 otu clusters total)

9. After step 8, what are the top 20 organisms found in this dataset?
OTU_3;size=12189;       d:Bacteria(1.0000),p:Firmicutes(0.9991),c:Tissierellia(0.9913),o:Tissierellales(0.9858),f:Peptoniphilaceae(0.981>
OTU_8;size=5904;        d:Bacteria(1.0000),p:Firmicutes(0.9994),c:Tissierellia(0.9993),o:Tissierellales(0.9938),f:Peptoniphilaceae(0.992>
OTU_4;size=14940;       d:Bacteria(1.0000),p:Firmicutes(0.9994),c:Bacilli(0.9993),o:Lactobacillales(0.9993),f:Carnobacteriaceae(0.9925),>
OTU_6;size=2691;        d:Bacteria(1.0000),p:Actinobacteria(0.9968),c:Actinobacteria(0.9933),o:Propionibacteriales(0.9907),f:Propionibac>
OTU_1;size=36320;       d:Bacteria(1.0000),p:Actinobacteria(0.9979),c:Actinobacteria(0.9963),o:Propionibacteriales(0.9938),f:Propionibac>

OTU_5;size=3182;        d:Bacteria(1.0000),p:Actinobacteria(1.0000),c:Actinobacteria(1.0000),o:Corynebacteriales(0.9938),f:Corynebacteri>
OTU_7;size=2279;        d:Bacteria(1.0000),p:Actinobacteria(0.9600),c:Actinobacteria(0.9152),o:Corynebacteriales(0.5260),f:Dietziaceae(0>
OTU_2;size=41412;       d:Bacteria(1.0000),p:Firmicutes(1.0000),c:Bacilli(1.0000),o:Bacillales(0.9938),f:Staphylococcaceae(0.9842),g:Sta>
OTU_10;size=7032;       d:Bacteria(1.0000),p:Firmicutes(0.9991),c:Tissierellia(0.9987),o:Tissierellales(0.9937),f:Peptoniphilaceae(0.993>
OTU_11;size=2688;       d:Bacteria(1.0000),p:Firmicutes(0.9845),c:Tissierellia(0.9625),o:Tissierellales(0.9371),f:Peptoniphilaceae(0.943>

OTU_9;size=1897;        d:Bacteria(1.0000),p:Proteobacteria(0.9295),c:Betaproteobacteria(0.7453),o:Neisseriales(0.3906),f:Neisseriaceae(>
OTU_15;size=356;        d:Bacteria(1.0000),p:Proteobacteria(0.9295),c:Betaproteobacteria(0.7453),o:Neisseriales(0.3478),f:Neisseriaceae(>
OTU_16;size=432;        d:Bacteria(1.0000),p:Firmicutes(0.9845),c:Tissierellia(0.9693),o:Tissierellales(0.9481),f:Peptoniphilaceae(0.963>
OTU_14;size=727;        d:Bacteria(1.0000),p:Proteobacteria(0.9990),c:Epsilonproteobacteria(0.9987),o:Campylobacterales(0.9938),f:Campyl>
OTU_12;size=2138;       d:Bacteria(1.0000),p:Actinobacteria(0.9994),c:Actinobacteria(0.9993),o:Corynebacteriales(0.9938),f:Corynebacteri>

OTU_13;size=2293;       d:Bacteria(1.0000),p:Firmicutes(0.9994),c:Bacilli(0.9993),o:Lactobacillales(0.9938),f:Streptococcaceae(0.9898),g>
OTU_19;size=314;        d:Bacteria(1.0000),p:Firmicutes(0.9988),c:Negativicutes(0.9992),o:Veillonellales(0.9938),f:Veillonellaceae(0.990>
OTU_17;size=447;        d:Bacteria(1.0000),p:Proteobacteria(0.9979),c:Gammaproteobacteria(0.9963),o:Pasteurellales(0.9907),f:Pasteurella>
OTU_18;size=392;        d:Bacteria(1.0000),p:Firmicutes(0.9991),c:Bacilli(0.9987),o:Lactobacillales(0.9938),f:Streptococcaceae(0.9901),g>
OTU_23;size=199;        d:Bacteria(1.0000),p:Firmicutes(0.9479),c:Clostridia(0.9017),o:Clostridiales(0.7322),f:Clostridiaceae(0.7151),g:>

numbers in parentheses are confidence (not population fraction)
