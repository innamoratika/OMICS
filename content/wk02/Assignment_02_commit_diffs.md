# View the README.md differences between commits

## Introduction

Now that you have commited multiple times, 
review the README.md file differences between commits


## Goals

Learn how to use `git log` and `git diff` to see the differences between file versions


# Walkthrough
### Get a list of your commit logs and hashes (ids)
#### Command
```
$ git log --oneline -- README.md
```

#### Command and output
```
$ git log --oneline -- README.md
b95796e 4. Added copyright
67c1380 3. Added abstract
b034503 2. Added description
23fa03a 1. First draft: Added title
```

### Use `git diff olderhash newerhash' to see README.md differences
https://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-diff

### Find the difference between commit 3 and 4 (Added copyright)
#### Command
```
# b95796e 4. Added copyright
# 67c1380 3. Added abstract

$ git  diff 67c1380 b95796e -- README.md
```

#### Command and output
```
$ git  diff 67c1380 b95796e -- README.md
diff --git a/projects/dvklopfenstein/README.md b/projects/dvklopfenstein/README.md
index 8b673af..ea28128 100644
--- a/projects/dvklopfenstein/README.md
+++ b/projects/dvklopfenstein/README.md
@@ -9,3 +9,4 @@ Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
 fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
 culpa qui officia deserunt mollit anim id est laborum.

+Copyright (C) 2023-present, DV Klopfenstein. All rights reserved
```


### Find the difference between commit 2 and 3 (Added abstract)
#### Command
```
# 67c1380 3. Added abstract
# b034503 2. Added description

$ git  diff b034503 67c1380 -- README.md
```

#### Command and output
```
$ git  diff b034503 67c1380 -- README.md
diff --git a/projects/dvklopfenstein/README.md b/projects/dvklopfenstein/README.md
index 063a8ca..8b673af 100644
--- a/projects/dvklopfenstein/README.md
+++ b/projects/dvklopfenstein/README.md
@@ -1,2 +1,11 @@
 # DVK's Project
 My description ...
+
+# Abstract
+Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
+incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
+nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
+Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
+fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
+culpa qui officia deserunt mollit anim id est laborum.
+
```

### Find the difference between commit 1 and 2 (Added description)
#### Command
```
# b034503 2. Added description
# 23fa03a 1. First draft: Added title

$ git diff 23fa03a b034503 -- README.md
```
#### Command and output
```
$ git diff 23fa03a b034503 -- README.md
diff --git a/projects/dvklopfenstein/README.md b/projects/dvklopfenstein/README.md
index ccf46b7..063a8ca 100644
--- a/projects/dvklopfenstein/README.md
+++ b/projects/dvklopfenstein/README.md
@@ -1 +1,2 @@
 # DVK's Project
+My description ...
```

Copyright (C) 2023-present, Drexel Medicine. All rights reserved
