# Wk 5 Assignment
## A) MET7 gene - GeneID:85415; product=tetrahydrofolate synthase
*  MET7 is the S. cerevisiae gene for tetrahydrofolate synthase, and
is one of several MET genes involved in methionine synthesis 
* MET7 is a mitochondrial gene and has a human ortholog
* "catalyzes extension of the glutamate chains of the folate coenzymes, required for methionine synthesis and for maintenance of mitochondrial DNA; protein abundance increases in response to DNA replication stress"

## B)Determining Coverage for MET7
### To find the location of MET7:
	'grep -i "gene=MET7" ~/common/refs/SGD/annotations/genomic.gff'
### To view and count the aligned reads:
	'samtools view-h ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001147.6:786995-788641 | less -S'
	>There are a number of deletions and hard clips in the aligned reads for MET7
	'samtools view -c ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001147.6:786995-788641'
	> There are 3069 reads for MET7

###To estimate coverage with samtools coverage:
	'samtools coverage -r NC_001147.6:786995-788641 ~/common/snowflake_yeast/aligned/SRR23803536.sorted.bam'
	>Mean depth for MET7 is 203.488X
