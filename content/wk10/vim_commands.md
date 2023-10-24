# vim keys in assignments

## Quitting vim
```
:q   Quit vim (works if you have no edits)
:q!  Quit vim and discard edits
:wq  Write, then quit
```

## Moving one character at a time
hjkl    
```
          ^(UP)
          |
          |
   <- h j k l ->(EOL)
        |
        |
        V(DOWN)
```

## Insertion (i)
```
iHello<Esc>:wq  Begin --INSERT-- (i); Type "Hello"; write and quit
iWorld<Esc>:q!  Begin --INSERT-- (i); Type "Workd"; quit without writing
```

## Going to the top of the file (gg) and the bottom of the file (G)
```
:set nu        Display line numbers
:set nonu      Don't display line numbers
gg             Go to the top of the file
G              Go to the bottom of the file
ggoTop<Esc>    Open a new line and insert "Top" at the top of the file
GoBotton<Esc>  Open a new line and insert "Bottom" at the bottom of the file
oAAAA<Esc>     Open (o) a new line below the cursor and insert "AAAA"
OBBBB<Esc>     Open (O) a new line above the cursor and insert "BBBB"
:wq            Write and quit file
```

## Traversing the the end of line (EOL)
```
$ vim abc.txt
fp             find the letter `p` in the current line
$              Move the cursor to the end of the current line
```

