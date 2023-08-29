# Week 2: Linux, push, & Pull Request (PR)

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Review Material](#reading-material)
5. **Assignments**
  * [Git Lab 1. Make small successful changes to your README.md & commit many times](Assignment_01_commits.md)
  * [Git Lab 2. README.md commit differences](Assignment_02_commit_diffs.md)
  * [Git Lab 3. Get an old README.md](Assignment_03_show.md)
  * [Git lab 4. Get an SSH key](Assignment_04_SSH_key.md)
6. [Project](#project)

## Introduction

Last week you made a project directory, `cd`ed to your new project directory and added a README.
Congratulations on learning about the command line on Linux,
the terminal window, and starting to work with GitHub

Millions of people use version control to build project togeter.
Version control can also be used manage and protect individual projects.
Today we will work together learning in the class by submitting our projects to GitHub.

Git and command-line skills will help you access and use amazing projects that other people have created,
build projects with people from all over the world.

This week we will continue our git flow training by doing a commit to origin and pull request (PR) to upstream.

Last week we signed up for GitHub account to store our project work
and a JupyterHub account on Dr. Dampier's private server on the drexelmed.edu network.
We learned to navigate the directory structure using
```
$ pwd              # present working directory
$ cd               # change directory to home (~)
$ cd ~/repos/OMICS # change directory 
$ ls               # list the files and directories in the current directory
$ ls -l -t -r      # list -l (long format), -t (sort by time) -r (reverse sort: newest last)
$ ls -ltr          # same as above: optional params can be stuck together
$ ls -lSrh         # list -l (long format), 
                   #      -S (sort by file size),
                   #      -r (reverse sort: biggest last)
                   #      -h (human readable)
$ ls --help        # Get help for the ls command
$ man ls           # Get help for the ls command
```
We will add to this by learning some bash args which will help you 
work faster on the command line.

## Learning Objectives

 - get a SSH key, which is needed to do a commit`to `origin`
 - Explain and do: fork, git clone, git status, git add, git commit, git push, and pull request
 - Use the bash arg, !$, to make typing on the command line faster
 - Practice basic terminal commands like `pwd`, `cd`, `less`, `head`.
 - Practice getting help with terminal commands with `--help`, and `man` (manual, as in documetation)

## Reading Material

 - [Link: How to read git diff output](https://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-dif)

## Project

For your project.
 - Make numerous changes to your project README.md and commit them
 - Get a list of the changes you have made to your README.md
 - Find the changes in the README.md file between various commit versions

Copyright (C) 2023-present, Drexel Medicine. All rights reserved
