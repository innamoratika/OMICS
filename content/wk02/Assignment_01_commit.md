# Git commit assignment

## Introduction

Change your project README.md and commit your changes.
Do this several times.

## Goals

We will have a number of versions of your README.md
as you build it.


# Walkthrough
### Go to your project README.md
```
$ cd ~/repos/OMICS/projects/mygitlogin
```

### Change your README.md and commit it
```
$ nano README.md
$ git commit README.md -m '1. First draft, Added title'
```

### Change and commit yoru README.md several times
```
$ nano README.md
$ git commit README.md -m '2. Added description'

$ nano README.md
$ git commit README.md -m '3. Added abstract'

$ nano README.md
$ git commit README.md -m '4. Added copyright'
```

### Look at your commit messages
```
$ git log --oneline -- README.md
b95796e (HEAD -> main) 4. Added copyright
67c1380 3. Added abstract
b034503 2. Added description
23fa03a 1. First draft: Added title
```

Copyright (C) 2023-present, Drexel Medicine. All rights reserved
