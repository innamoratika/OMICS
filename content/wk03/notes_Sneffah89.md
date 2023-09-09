Demultiplexing commands
seqkit grep --use-regexp -s -p '^CTGC.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803539.fastq
seqkit grep --use-regexp -s -p '^CTGC.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803539.fastq
seqkit grep --use-regexp -s -p '^CTGC.*CCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803538.fastq
seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803537.fastq
seqkit grep --use-regexp -s -p '^ACCT.*CCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803536.fastq

Triming the barcodes
seqkit subseq -r 5:-5 SRR23803537.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803537.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803536.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803536.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803538.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803538.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803539.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803539.trimmed.fastq.gz

Demultiplex and Trimmed statistics
seqkit stats -T solution/SRR23803537.* > ~/repos/OMICS/content/wk03/solution/demuxed.stats.tsv