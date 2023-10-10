#!/bin/bash

# Script for aligning and variant calling yeast sequence data
# variant_call path/to/reads_1 path/to/reads_2 path/to/variants.bcf

# Define some constants
REF=/data/share/courses/OMICS/SGD/bwaindex/R64.fasta
FILTER='DP>=10&&QUAL>20'

(bwa mem $REF $1 $2 |       
  samtools view --bam |    
  samtools sort |          
  bcftools mpileup -Ou -f $REF - |
  bcftools call -m |         
  bcftools filter -Ob -i $FILTER > $3)
