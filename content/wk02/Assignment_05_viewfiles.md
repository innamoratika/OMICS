# Assignment 5

## Introduction

View a dataset that has been uploaded to a shared directory.

## Goals

Find and review the size and contents of a dataset.

## Datasets

`~/share/courses/OMICS/wk02_dataset`

# Walkthrough

## Find your dataset

```
$ cd ~/share/courses/OMICS/wk02_dataset
```

Q1: What does the `cd` command mean here?

## Look at the files in your dataset

Q2: How many files are in the directory?    

Q3: How do you find the full path to the directory they are stored in?    

```
Possible commands:
$ ls
$ mkdir
$ pwd
$ ls -lh 
```

## Create a nano file in your OMICS/projects/yourgitusername directory

```
$ nano answers_week02_yourgitusername.txt
```
Answer Q1, Q2, and Q3 and save them to this new document.

## Look at the files
 Pick a file within wk02_dataset and look at it with the following three commands:   

```
$ head
$ less
$ cat
$ tail
```
Q4: Which one do you like the best for viewing these files? Why?   

Answer Q4 in your answers_week02 document.

## Practice with commands and flags
Q5: Which file is the largest and which file is the smallest in wk02_dataset?   

```
Possible commands:
$ ls
$ ls -l
$ ls -lh
$ ls -l -h
$ ls -lS
$ less
```

Q6: What unit is the file size when using `ls -l`?    

Type the following command: `man ls`    

Q7: What do the `-l` and `-h` flags stand for?    

## Submit your assignment
* Push to origin    
* Create a pull request to upstream with your answers    
