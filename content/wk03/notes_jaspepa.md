multiplexed stats: 
seqkit stats data/multiplexed.fq -T > solution/muxed.stats.tsv
file    format  type    num_seqs        sum_len min_len avg_len max_len
data/multiplexed.fq     FASTQ   DNA     1900    264787  43      139.4   159
There are 1900 sequences totaling 264787 reads; the shortest sequence is 43 and the longest is 159 bases. 

Sorting multiplexed reads by barcode: used seqkit grep with one statement. .* are unknown length middle part of reads
eg seqkit grep --use-regexp -s -p '^ACCT.*CCAG$' data/multiplexed.fq > solution/SRR23803536.fastq

Removing barcodes: used subseq -range given that the barcodes are all four bases long 
eg seqkit subseq -r  5:-5 SRR23803539.fastq > SRR23803539.trimmed.fastq.gz
documentation: https://bioinf.shenwei.me/seqkit/usage/#subseq 
this also trimmed quality scores (checked by looking at fastq.gz files with nano editor) 

demuxed states: 
~/repos/OMICS/content/wk03$ seqkit stats solution/SRR23803536.trimmed.fastq.gz solution/SRR23803537.trimmed.fastq.gz solution/SRR23803538.trimmed.fastq.gz solution/SRR23803539.trimmed.fastq.gz -T > solution/demuxed.stats.tsv
file    format  type    num_seqs        sum_len min_len avg_len max_len
solution/SRR23803536.trimmed.fastq.gz   FASTQ   DNA     1234    153328  35      124.3   151
solution/SRR23803537.trimmed.fastq.gz   FASTQ   DNA     567     82897   35      146.2   151
solution/SRR23803538.trimmed.fastq.gz   FASTQ   DNA     89      12039   64      135.3   151
solution/SRR23803539.trimmed.fastq.gz   FASTQ   DNA     10      1323    96      132.3   151
Results: Sample 3536 had far more reads and sample 3539 had far fewer. Min and Max length are integers but mean isn't necessarily,
which makes sense. Maximum length 151 after trimming is consistent with maximum length 159 before trimming.

Reflection: The read lengths were about the same for each sample. Each sample had a maximum of 151 bases (159 bases before trimming)
and the averages were about the same; small minimum lengths correlated with large numbers of reads. Sample 36 had the most reads,
followed by sample 37 and then sample 38. Sample 39 had only 10 reads. 

