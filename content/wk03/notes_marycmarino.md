# Mary Marino Week 3 Assignment Notes

1. **Mux statistics:**
* to save the seqkit statistics summary as a tsv file: seqkit stats -T data/multiplexed.fq > solution/muxed.stats.tsv
* tried to run pytest, but an error message occurred... instructed to ignore for now

2. **Demultiplex the samples:**
* to filter for samples using their barcodes and save it to a new fastq file:
	* sample 1: seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803536.fastq
	* sample 2: seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803537.fastq
	* sample 3: seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803537.fastq
	* sample 4: seqkit grep --use-regexp -s -p '^ACCT.*TCAG$' multiplexed.fq > ~/repos/OMICS/content/wk03/solution/SRR23803537.fastq
* checked that the files were created in "solution" by changing working directories (cd) and listing (ls) everything in it... files were created successfully

3. **Trim the barcodes:**
* source: https://bioinf.shenwei.me/seqkit/usage/#subseq
* to trim the samples so that only the fifth base pair to the fifth from last base pair remain:
	* sample 1: seqkit subseq -r 5:-5 SRR23803536.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803536.trimmed.fastq.gz
	* sample 2: seqkit subseq -r 5:-5 SRR23803537.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803537.trimmed.fastq.gz
	* sample 3: seqkit subseq -r 5:-5 SRR23803538.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803538.trimmed.fastq.gz
	* sample 4: seqkit subseq -r 5:-5 SRR23803539.fastq > ~/repos/OMICS/content/wk03/solution/SRR23803539.trimmed.fastq.gz

4. **Demux statistics:**
* to generate statistics for all files (demultiplexed and trimmed) and save them to a .tsv file:
seqkit stats SRR23803536.fastq SRR23803536.trimmed.fastq.gz SRR23803537.fastq SRR23803537.trimmed.fastq.gz SRR23803538.fastq SRR23803538.trimmed.fastq.gz SRR23803539.fastq SRR23803539.trimmed.fastq.gz > ~/repos/OMICS/content/wk03/solution/demuxed.stats.tsv
* results:
	* the min/max length of each trimmed file is 8 bp shorter than the demultiplexed file, indicating that the barcodes were trimmed
	* the number of reads between the demultiplexed and trimmed files are the same, indicating that no reads were lost in the process of trimming the barcodes
	* no files contain reads longer than 159 (demultiplexed) or 151 (trimmed) basepairs

file                          format  type  num_seqs  sum_len  min_len  avg_len  max_len
SRR23803536.fastq             FASTQ   DNA      1,234  163,200       43    132.3      159
SRR23803536.trimmed.fastq.gz  FASTQ   DNA      1,234  153,328       35    124.3      151
SRR23803537.fastq             FASTQ   DNA        567   87,433       43    154.2      159
SRR23803537.trimmed.fastq.gz  FASTQ   DNA        567   82,897       35    146.2      151
SRR23803538.fastq             FASTQ   DNA         89   12,751       72    143.3      159
SRR23803538.trimmed.fastq.gz  FASTQ   DNA         89   12,039       64    135.3      151
SRR23803539.fastq             FASTQ   DNA         10    1,403      104    140.3      159
SRR23803539.trimmed.fastq.gz  FASTQ   DNA         10    1,323       96    132.3      151

5. **Reflection questions:**
Each sample contains a different number of reads. Sample 1 (SRR23803536) contains 1,234 reads. Sample
2 (SRR23803537) contains 567 reads. Sample 3 (SRR 23803538) contains 89 reads. Finally, sample 4
(SRR23803539) contains 10 reads. However, among all of these reads, the max lengths are the same. None
of the reads are longer than 159 bp (untrimmed)/151 bp (trimmed). The average length of each read differs
between samples, but only by about 20 bp. The sample with the longest average length is sample 2. The 
sample with the shortest average length is sample 1.
