Week 3 Assignment

Mux statistics command
seqkit stats -T data/multiplexed.fq > solution/muxed.stats.tsv
file    format  type    num_seqs        sum_len min_len avg_len max_len
data/multiplexed.fq     FASTQ   DNA     1900    264787  43      139.4   159
**The file is a FASTQ file containing 1900 DNA sequences and about 264787 bases in total. The minimal, average and maximal sequence length is 43, 139.4 and 159 respectively**

Demultiplexing commands
seqkit grep --use-regexp -s -p '^CTGC.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803539.fastq
seqkit grep --use-regexp -s -p '^CTGC.*CCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803538.fastq
seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803537.fastq
seqkit grep --use-regexp -s -p '^ACCT.*CCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803536.fastq
  **I used seqkit grep --help to know all the sub commands under it. so --use-regexp fit the purpose of this section of the assignment.Then i channeled this into the path stated in the question** 

Triming barcode commands
seqkit subseq -r 5:-5 SRR23803537.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803537.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803536.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803536.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803538.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803538.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803539.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803539.trimmed.fastq.gz
  **I used seqkit subseq --help to know all the sub commands under it. so -r was appropriate. and since the barcode bases we want removed at the begining and at the end are four bases, the range of sequence required are from the 5th base to the 5th base from the last base.**
  
Demux statistics commands
seqkit stats SRR23803536.fastq SRR23803536.trimmed.fastq.gz SRR23803537.fastq SRR23803537.trimmed.fastq.gz SRR23803538.fastq SRR23803538.trimmed.fastq.gz SRR23803539.fastq SRR23803539.trimmed.fastq.gz > ~/repos/OMICS/content/wk03/solution/demuxed.stats.tsv
file                          format  type  num_seqs  sum_len  min_len  avg_len  max_len
SRR23803536.fastq             FASTQ   DNA      1,234  163,200       43    132.3      159
SRR23803536.trimmed.fastq.gz  FASTQ   DNA      1,234  153,328       35    124.3      151
SRR23803537.fastq             FASTQ   DNA        567   87,433       43    154.2      159
SRR23803537.trimmed.fastq.gz  FASTQ   DNA        567   82,897       35    146.2      151
SRR23803538.fastq             FASTQ   DNA         89   12,751       72    143.3      159
SRR23803538.trimmed.fastq.gz  FASTQ   DNA         89   12,039       64    135.3      151
SRR23803539.fastq             FASTQ   DNA         10    1,403      104    140.3      159
SRR23803539.trimmed.fastq.gz  FASTQ   DNA         10    1,323       96    132.3      151

The number of reads is the same for fastq and trimmed.fastq.gz files for each sample. However read length differs and it smaller for trimmed.fastq.gz files compared to the fastq files. Again the number of reads for fastq and trimmed.fastq.gz files for each sample decrease in the order SRR23803536 > SRR23803537 > SRR23803538 > SRR23803539. The read length also differ between samples.