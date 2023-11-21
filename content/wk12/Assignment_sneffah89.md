## Question 1: 
What is the output of this command? `usearch --version`

`usearch v8.1.1861_i86linux64`

## Question 2:
How is 'seqs.fq' represented in the directory? (copy/paste on the next line)

`seqs.fq -> /home/jupyter-sneffah89/share/courses/OMICS/wk12_ataset/sequences_for_clustering.fq`

## Question 3:
How many sequences are in the seqs.fq file?

Using `grep -c '^@' seqs.fq` there are `168338` sequences

## Question 4: 
**i**. what does the variable 'size'represent in the header?

The "size" variable typically indicates the number of times a specific sequence was observed or the abundance of that sequence in the original dataset before dereplication

**ii**. what relevance does this have for the otu clustering step?

The dereplicating step enables you to have unique sequences after which you can know the number of or the abundances of each unique sequence

## Question 5:
**i**. what is the command you use to calculate the number of sequences after dereplicating

`grep -c '>m' seqs_derep.fa`

**ii**. How many sequences are there 

`157474`

## Question 6:
how many sequences exist in the output fasta file otu.fa?

`310`

## Question 7:
**i**. What is a 'chimera 

A chimera is a sequence that is a result of the artificial combination of two or more distinct biological sequences during the PCR amplification step. 

**ii**. how many were found in this dataset after step 6?

`1170` chimeras

## Question 8:
After step 7 how many additional Chimeras were found?

`5` additional chimeras

## Question 9: 
After step 8, what are the top 20 organisms found in this dataset?

1.`Staphylococcus`

2.`Peptoniphilus`

3.`Gordonia`

4.`Simonsiella`

5.`Anaerococcus`

6.`Streptococcus`

7.`Haemophilus`

8.`Neisseria`

9.`Clostridium`

10.`Granulicatella`

11.`Actinomyces`

12.`Halomonas`

13.`Exiguobacterium`

14.`Rikenella`

15.`Pseudomonas`

16.`Peptostreptococcaceae_incertae_sedis`

17.`Fusobacterium`

18.`Dialister`

19.`Prevotella`

20.`Propionibacterium`

