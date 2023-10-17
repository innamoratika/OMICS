# Mary Marino Week 05 Notes

### My Randomly-Chosen Gene
```
NC_001148.4     RefSeq  CDS     647305  648375  .       +       0       ID=cds-NP_015365.1;Parent=rna-NM_001184137.1;Dbxref=SGD:S000006244,GeneID:856153,GenBank:NP_015365.1;Name=NP_015365.1;Note=Tap42p-interacting protein%3B negative regulator of the TORC1 signaling pathway that activates the type 2A-related phosphatase Sit4p by binding and antagonizing Tap42p%2C a SIT4 inhibitor%3B proposed to be part of a feedback loop to amplify Sit4p activity when TORC1 is inactivated%3B protein abundance increases in response to DNA replication stress;experiment=EXISTENCE:direct assay:GO:0005634 nucleus [PMID:14562095],EXISTENCE:direct assay:GO:0005737 cytoplasm [PMID:14562095|PMID:11914276],EXISTENCE:mutant phenotype:GO:1904262 negative regulation of TORC1 signaling [PMID:11741537];gbkey=CDS;gene=TIP41;locus_tag=YPR040W;product=Tip41p;protein_id=NP_015365.1
```
* My gene is TIP41, a Tap42p-interacting protein
* It negatively regulates the TORC1 signaling pathway, which is activated by Sit4p
* The Tip41 protein binds to Tap42p, which inhibits Sit4p and prevents the TORC1 pathway from being activated

### Coverage
* To find the location of my gene in the genome: `grep -i "gene=TIP41" ~/common/refs/SGD/annotations/genomic.gff`
	* Location: `NC_001148.4:647305-648375`
* To retreive the reads that aligned there: `samtools view ~/common/snowflake_yeast/aligned/SRR23803537.sorted.bam NC_001148.4:647305-648375 | head`
	* Or: `samtools view ~/common/snowflake_yeast/aligned/SRR23803537.sorted.bam NC_001148.4:647305-648375 | less -S`
* To find the coverage: `samtools coverage --histogram ~/common/snowflake_yeast/aligned/SRR23803537.sorted.bam`

```
NC_001148.4 (948.1Kbp)
>  90.00% │▇▄████▃████████████████▇███████████████████████  ███████████████████████████████████████████ ▇██████   │ Number of reads: 560834
>  80.00% │███████████████████████████████████████████████ ▇███████████████████████████████████████████▇███████   │     (843 filtered)
>  70.00% │███████████████████████████████████████████████ ████████████████████████████████████████████████████▄  │ Covered bases:   924.8Kbp
>  60.00% │███████████████████████████████████████████████ █████████████████████████████████████████████████████  │ Percent covered: 97.54%
>  50.00% │███████████████████████████████████████████████ █████████████████████████████████████████████████████ ▅│ Mean coverage:   86x
>  40.00% │███████████████████████████████████████████████▄█████████████████████████████████████████████████████ █│ Mean baseQ:      33
>  30.00% │█████████████████████████████████████████████████████████████████████████████████████████████████████ █│ Mean mapQ:       57.2
>  20.00% │█████████████████████████████████████████████████████████████████████████████████████████████████████ █│ 
>  10.00% │█████████████████████████████████████████████████████████████████████████████████████████████████████ █│ Histo bin width: 9.2Kbp
>   0.00% │█████████████████████████████████████████████████████████████████████████████████████████████████████▇█│ Histo max bin:   100%
          1       92.0K     184.1K    276.1K    368.2K    460.2K    552.2K    644.3K    736.3K    828.4K       948.1K 
```

### Consensus
* To calculate the consensus sequence and save it as instructed: `samtools consensus -r NC_001148.4:647305-648375 -f fasta ~/common/snowflake_yeast/aligned/SRR23803537.sorted.bam > marycmarino_gene_cons.fasta`
* My consensus sequence:
```
>NC_001148.4
ATGTCCAAAAGAAACACCCCACCGCTCAGATCATCAGGGATAAATACTATTCAAATAAATGCTGCTAGAG
AAATGCACGCTCAAACGGTGCGCGCTCGAAGAATGCCCATGCCAACTAGCGGCATCACTACACCCTCTGT
GCAACCAACTGCAGCCCCAGCAACACGACCTCGACATATTTGCAATAACCCAAACAATCCGCAGTGTCTC
CACTGTGGGTCTGTTATCATTCCATCTCCAAGGGCCACGTTACCCTTGGAGGACAACCCCTCCATCTCCA
TCAACGACTGGACCATCTCCTCCAGAAAGAAGCCCATTTTGAACTCGCAGGAATTAGACATCTGGGAAAA
CGAAAAACTCAAAGGTTTGACTTTGCCAGAGATGATTTTTGGTAACAACTACATCAGGATCGAAAACTCA
AAACAGCATTGGTCCATAGAGTTCAATGCCCTGGATGCTTTAAAGGAGGTTCAACTCCAGGATTCAGGTA
TTCGTGTTGCGTACTCAAACGACTGGATAAATTCTAAAAAAAGACAAAATTCAACTAATGGTGCGCAACG
GTTCACTAACGATGTGAACGACGATTCCTTAAGTATCATACACAAGTACGACTGGACTTACACTACGCGG
TACAAGGGCACAGAGAGCTCACCTGAGTCGAAATTCCGACTGGATAACGATCAAAAGCTGCCCCTTGACA
AACTGGCCGTACACGATAAAATCCTATTCTATGACGACATGATTCTTTTCGAAGACGAATTGGCAGACAA
TGGCATATCAATCCTTAACGTCAAAATAAGAGTTATGAACGAAAGGTTGCTGCTGCTGAGCCGGTTCTTT
TTAAGGGTGGACGATGTTCTGGTTAGGGTCTACGACACCAGGATTTACGTGGAGTTTGACGAAAACGTAG
TGATCAGAGAATCCAAGGAATTTGAAGGTAAATATCAGGATGTACTTGCTAAGCACCGGCTATCCCAATC
TCACGACCCAAAAGCTGCCTTGAGAGATAGTAATTGGGTAGCACAGAACACGCCGATGATCAAAAGACAA
TGTGAAATAATTCAGTTCTAA
```
