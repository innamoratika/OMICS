# Introduction

Vim is a powerful editor.

According to stackoverflow's developer 2022 survey, vim is the 3rd most popular editor behind Microsoft's Visual Studio.

Vim is popular because it offers many advantages:
* All Linux machines have vi.
* The vim executable is compact, taking only 3.4M of disk compared to Microsoft Word at a whopping 2.11GB.
* Vim starts fast and loads files fast, even if the files are huge.
* Visualize your full document more easily by seeing more file text on the screen with vim than possible with JupyterLab, nano, or Microsoft Word.
* Edit your work with lightening speed once muscle-memory has been entrenched.

# Learning Objectives

* YOU WILL NOT BE A MEME: Learn how to quit out of the vim editor
* Explain editor modes: normal, insert, and visual
* Traverse a file using vim key-bindings in normal mode
* Edit a file in --INSERT-- mode

# Reading Material

* [Why, of WHY, do those #?@! nutheads use vi?](http://www.viemu.com/a-why-vi-vim.html)
* [vim documentation on-line](https://vimdoc.sourceforge.net/htmldoc/usr_toc.html)
* [Why and How to use vim as a text editor](https://mr-destructive.github.io/techstructive-blog/vim-text-editor-ide/)
* [vim keypresses on stackoverflow](https://stackoverflow.com/questions/5400806/what-are-the-most-used-vim-commands-keypresses)

# Assignment

|N|keys              | Description
|-|------------------|------------------------------------
|1|`:q`              | Quit vim
|2|`i j k l`         | Move cursor one character at a time
|3|`iTEXT<Esc>:wq'   | Insert text in --INSERT-- mode and save
|4|`gg` and `G`      | Move cursor to top and bottom of file:
|4|`ggoTOP<Esc>:wq`  | Go to the top of a file; open a new line; insert "TOP"; write and quit
|5|`gg` & `G` & `:wq`| Compare vim movements with movements in Linux  command, `less`
|6|`$`               | Move to the end of the line


Copyright (C) 2023-present, Drexel Medicine. All rights reserved.
