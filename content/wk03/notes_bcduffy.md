#De-multiplexing muxed reads
## 1) To run stats on muxed files
> `seqkit stats -T data/multiplexed.fq >  solution/muxed.stats.tsv`
*  this line uses seqkit stats command to run stats, specifies tabular output with the -T flag,<br> specifies the multiplexed FastQ file, then stores the output to the muxed.stats.tsv file in the solution directory
### Muxed Stats Output
|file | format | type | num_seqs | sum_len | min_len | avg_len | max_len|
|:-:  |:-:     |:-:   |:-:       | :-:     | :-:     | :-:     | :-:    |
|data/multiplexed.fq | FASTQ | DNA | 1900 | 264787 | 43 | 139.4 | 159|

> The stats results tell us that there are 1900 sequences with an everage length of 13 nts

## 2) To de-multiplex the muxed reads, used seqkit grep
>```seqkit grep --use-regexp -s -r -p '^CTGC.*TCAG$' data/multiplexed.fq > solution/SRR23803539.fastq```

*  specific FWD and REV primers were altered for each respective sample to demux into its own file. 
* '>' to store the resulting data in fastq file named for each respective sample ID, according to the matched primer pair from sample_sheet.csv
## 3) To trim each sample read fastq file, I searched the seqkit commands and selected **amplicon**
*  The function of amplicon is to return the amplicon (sequence) that is flanked by user provided primers
>```seqkit amplicon solution/SRR23803536.fastq -F ACCT -R CCAG -r 5:-5 > solution/SRR23803536.trimmed.fastq```

> Flags in this code:
*  '-F' is the flag for the fwd primer, -R for the reverse primer
*  '-r' enabled me to indicate the index positions of the string to be returned; to ensure that the 4 nucleotides are entirely trimmed, I indicated the index positions to be 1 place inset from the primer nucleotides.
*  after the seqkit amplicon command was complete, I used > to write the results to the new trimmed.fastq file
* In a subsequent step, I used gzip to zip the trimmed fastq file
###for the remaining samples (...3537, 3538, 3539) I used a single line of code using > and the file extension .gz to zip the resulting trimmed file: 
>```seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -r 5:-5 > solution/SRR23803537.trimmed.fastq.gz```
* this command was modified to specify the sample ID and primer set for each respective sample, to generate individual trimmed.fastq.gz files.
* the indication of the output file as sampleID.fastq.gz indicates to gzip the resulting file
> Note: My only concern is that it looks like seqkit amplicon is finding the first occurrence of REV primer, when reading left to right; so I've potentially lost some nucleotides based on this trimming

##4) Demux stats
>`seqkit stats -T solution/*.gz > solution/demuxed.stats.tsv` 
### Demux stats output
|file | format | type | num_seqs | sum_len | min_len | avg_len | max_len|
|:---:|:------:|:----:|:--------:|:-------:|:-------:|:-------:|:------:|
|solution/SRR23803536.trimmed.fastq.gz | FASTQ | DNA | 382 | 24771 | 1 | 64.8 | 147|
|solution/SRR23803537.trimmed.fastq.gz | FASTQ | DNA | 257 | 17497 | 1 | 68.1 | 147|
|solution/SRR23803538.trimmed.fastq.gz | FASTQ | DNA | 29  | 2261 | 21 | 78.0 | 144|
|solution/SRR23803539.trimmed.fastq.gz | FASTQ | DNA | 3 | 139 | 16 | 46.3 | 64|

> These results suggest that sequencing depth was not equally distributed across all samples, as SRR23803538 and 3539 contain far fewer sequences than 3536 and 3537.
> There are also very wide ranges of read lengths in the trimmed files - sample -3539 has a much lower average read length compared to the other samples. This could indicate a difference in biological condition, or an error in the demux or trimming of this sample, potentially based on sequence differences or repeats in the sequence causing excessive trimming.





History 5Sep2023 -

 
 261  nano notes_bcduffy.md
  262  pytest
  263  ll
  264  ls
  265  ls data
  266  seqkit stats data/multiplexed.fq
  267  seqkit stats -T data/multiplexed.fq | solution/muxed.stats.tsv
  268  seqkit stats -T data/multiplexed.fq >  solution/muxed.stats.tsv
  269  pytest
  270  nano notes_bcduffy.md 
  271  seqkit grep --use-regexp -s -r -p '^ACCT.*CCAG$'> solution/SRR23803536.fastq
  272  seqkit grep --use-regexp -s -r -p '^ACCT.*CCAG$' data/multiplexed.fq > solution/SRR23803536.fastq
  273  ls solution
  274  seqkit grep --use-regexp -s -r -p '^ACCT.*TCAG$' data/multiplexed.fq > solution/SRR23803537.fastq
  275  ls solution
  276  seqkit grep --use-regexp -s -r -p '^CTGC.*CCAG$' data/multiplexed.fq > solution/SRR23803538.fastq
  277  ls solution
  278  seqkit grep --use-regexp -s -r -p '^CTGC.*TCAG$' data/multiplexed.fq > solution/SRR23803539.fastq
  279  ls solution
  280  pytest
  281  seqkit
  282  seqkit amplicon
  283  seqkit man
  284  man seqkit
  285  seqkit help
  286  seqkit --help
  287  seqkit amplicon --help
  288  cd data
  289  ls
  290  cd ..
  291  ls solution
  292  seqkit amplicon solution/SRR23803536.fastq -F ACCT -R CCAG -o solution/SRR23803536.trimmed.fastq.gz
  293  ls solution
  294  nano notes_bcduffy.md 
  295  seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -o solution/SRR23803537.trimmed.fastq.gz
  296  seqkit amplicon solution/SRR23803538.fastq -F CTGC -R CCAG -o solution/SRR23803537.trimmed.fastq
  297  nano notes_bcduffy.md 
  298  seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -o solution/SRR23803537.trimmed.fastq
  299  seqkit amplicon solution/SRR23803537.fastq -F ^ACCT -R TCAG$ -o solution/SRR23803537.trimmed.fastq
  300  seqkit amplicon --use-regexp solution/SRR23803537.fastq -F ACCT -R TCAG -o solution/SRR23803537.trimmed.fastq.gz
  301  seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -f -o solution/SRR23803537.trimmed.fastq.gz
  302  seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -f -o solution/SRR23803537.trimmed.fastq
  303  pwd
  304  cd repos/OMICS/content/wek03
  305  cd repos/OMICS/content/wk03
  306  ls
  307  cd data
  308  ls
  309  cd ..
  310  cd solution
  311  ls
  312  cd ..
  313  seqkit amplicon solution/SRR23803536.fastq -F ACCT -R CCAG -r 4:-4 > SRR23803536.trimmed.fastq
  314  ls
  315  rm SRR23803536.trimmed.fastq 
  316  ls
  317  seqkit amplicon solution/SRR23803536.fastq -F ACCT -R CCAG -r 4:-4 > solution/SRR23803536.trimmed.fastq
  318  seqkit amplicon solution/SRR23803536.fastq -F ACCT -R CCAG -r 5:-5 > solution/SRR23803536.trimmed.fastq
  319  gzip solution/SRR23803536.trimmed.fastq
  320  ls solution
  321  nano
  322  nano notes_bcduffy.md 
  323* seqkit amplicon solution/SRR238035
  324  seqkit amplicon solution/SRR23803537.fastq -F ACCT -R TCAG -r 5:-5 > solution/SRR23803537.trimmed.fastq.gz
  325  seqkit amplicon solution/SRR23803538.fastq -F CTGC -R CCAG -r 5:-5 > solution/SRR23803538.trimmed.fastq.gz
  326  seqkit amplicon solution/SRR23803539.fastq -F CTGC -R TCAG -r 5:-5 > solution/SRR23803539.trimmed.fastq.gz
  327  seqkit amplicon solution/SRR23803539.fastq -F CTGC -R TCAG$ -r 5:-5 > solution/SRR23803539.trimmed.fastq
  328  seqkit amplicon -h
  329  seqkit amplicon solution/SRR23803539.fastq 5:-5 >SRR23803539.trimmed.fastq
  330  nano notes_bcduffy.md 
  331  seqkit stats solution/*.gz
  332  nano notes_bcduffy.md 
  333  history
