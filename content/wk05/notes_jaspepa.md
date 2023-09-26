Random gene: 
NC_001148.4     RefSeq  mRNA    592332  593069  .       -       .       ID=rna-NM_001184113.1;
Parent=gene-YPR016C;Dbxref=GeneID:856126,GenBank:NM_001184113.1;Name=NM_001184113.1;end_range=593069,.;
gbkey=mRNA;gene=TIF6;locus_tag=YPR016C;partial=true;product=translation initiation factor 6;start_range=.,592332;
transcript_id=NM_001184113.1
Cursory search: This encodes a protein that is part of the 60S ribosomal complex. 

Syntax to view: samtools view ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001148.4:592332-593069 | head
(I accidentally put the snowflake_yeast soft link in common/refs instead of common). 
Output: samtools specifications and some fastq reads 
samtools view -c ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam NC_001148.4:592332-593069
Output: 1004

Syntax to estimate coverage: 
samtools coverage -r NC_001148.4:592332-593069 ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam
Output: 
#rname  startpos        endpos  numreads        covbases        coverage        meandepth       meanbaseq       meanmapq
NC_001148.4     592332  593069  1004    738     100     137.9   38      60

Histogram command: samtools coverage --histogram ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam
Relevant histogram: Chromosome NC_001148.4
NC_001148.4 (948.1Kbp)
>  90.00% │█▅████▆█████████████████████████████████████▆▄█████████████████████████████████████████▆██████▆▇▇│ Number of reads: 1043894
>  80.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│     (1466 filtered)
>  70.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   946.1Kbp
>  60.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 99.79%
>  50.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   127x
>  40.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      38
>  30.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       56.5
>  20.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 9.8Kbp
>   0.00% │█████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       97.7K     195.5K    293.2K    390.9K    488.6K    586.4K    684.1K    781.8K           948.1K 

Consensus: initial syntax 
samtools consensus -r NC_001148.4:592332-593069 -f pileup ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam | head
Output: 
NC_001148.4     592332  0       122     C       395     ccccCCCccCcCcCCcccCcCCCccccCCCcCCcCcCcccCcccCcCccCCCccCcCcCccCcCcCCcCcccCCcCCcCCcCCcccCCccCCCcccCcCCccCcCcCcCCCccccCCccCCc       GIIIGIGIGIGGIIIGGIGGGIIGIIIGGGGIGGGIGGIIGGGIAGIIIIIIGIIGIGIGGGGGIIGAIIIIGIGGGG.IG.GIGIIGIGIIIGGGGGAGIGA<.IGIIGGIG.IIIGIG.<
NC_001148.4     592333  0       122     T       399     ttttTTTttTtTtTTtttTtTTTttttTTTtTTtTtTtttTtttTtTttTTTttTtTtTttTtTtTTtTtttTTtTTtTTtTTtttTTttTTTtttTtTTttTtTtTtTTTttttTTttTTt       GIIIIIIIIGIAGIIGGIGGGGIGGIIGIGIGGGGIGGGIGGII.GIGIGGAGIAGIAGIIGIGGIGGGIIIGAIGII.A<AGIAGIGIGIIIIGGIGA.II<<GGIIIGIIIAIGIIII<G
NC_001148.4     592334  0       123     A       399     aaaaAAAaaAaAaAAaaaAaAAAaaaaAAAaAAaAaAaaaAaaaAaAaaAAAaaAaAaAaaAaAaAAaAaaaAAaAAaAAaAAaaaAAaaAAAaaaAaAAaaAaAaAaAAAaaaaAAaaAAaa      GAIIAIIIIIGGGIAGGIGGGIIGIGIGIAIGIGIGIGIGGIII<<IGIGIGGGAGIIIIIGIIIGGGGIIIGGI.GI.G.GGI<IGIIIIIIIIGGG..IIGGGGIGIGIIIGIIIGII<GI
NC_001148.4     592335  0       123     T       399     ttttTTTttTtTtTTtttTtTTTttttTTTtTTtTtTtttTtttTtTttTTTttTtTtTttTtTtTTtTtttTTtTTtTTtTTtttTTttTTTtttTtTTttTtTtTtTTTttttTTttTTtt      GGIIGIAIGIGGIIGGIIGAGIGGIIIGIGGGIIIGIGGIIIII..IGIIGGIG.GIIGIIIGIIIGGGIIIGGIAII<.<AIGGIGGIIIIGIIGGG.AIIAG.GGIIIIGIGIGIGIIAGI
NC_001148.4     592336  0       121     G       394     ggggGGGggGgGgGggGgGGGggggGGGgGGgGgGgggGgggGgGggGGGggGgGgGggGgGgGGgGgggGGgGGgGGgGGgggGGggGGGgggGgGGggGgGgGgGGGggggGGggGGgg        GAIIGGGIIGIIIGIIGIGGGGIGIGIGIGIGIGIIGIIIGG<AIGIIIGGIGIIIGIIGAGIIGGGIIIGAG<IG<<.GIIAGGGIIIIIGGGIIGAII<G.IGIGGIIGGIGIGGG.GG
NC_001148.4     592337  0       120     A       390     aaaAAAaaAaAaAaaAaAAAaaaaAAAaAAaAaAaaaAaaaAaAaaAAAaaAaAaAaaAaAaAAaAaaaAAaAAaAAaAAaaaAAaaAAAaaaAaAAaaAaAaAaAAAaaaaAAaaAAaa AIIGGIIGGIGIIGIGIGIIGIIGGGAIGGIGG.GGIAIGIA<IGIGIGGIAIGIGGGGGIIGGAGIIIIGG.IGAA.AGI.GG<IIGIIIGGGG..IGAGGIGIGIIIGGGIIGIGAGG
NC_001148.4     592338  0       124     G       403     gggGGGggGgGgGggGgGGGggggGGGgGGgGgGgggGgggGgGggGGGggGgGgGggGgGgGGgGgggGGgGGgGGgGGgggGGggGGGgggGgGGggGgGgGgGGGggggGGggGGggGGgg     GGG.GGIIIIIIIGIIIGIIIGIGIGGGIIGIIGGIIGIIIG.IGGGGIGGGIGIIIIGGIIIAAGIIIIGGGIIAGGGIIAIGGIGGGIIGIGI<.IIGAGIGIIGIII.GIIGIGGAGGGGI
NC_001148.4     592339  0       123     T       399     ttTTTttTtTtTttTtTTTttttTTTtTTtTtTtttTtttTtTttTTTttTtTtTttTtTtTTtTtttTTtTTtTTtTTtttTTttTTTtttTtTTttTtTtTtTTTttttTTttTTttTTtt      AGGGGIIIGGGGIGGGGGGIGIGIGGGGGGIIGGII<IGGGGIGIII.GGGGIGGIIAGGIIAGGIGIGAI<AIAGGGGIAGGGIIGGIIGI<GG<IIGGGIGIGGIIIGIGGIIGAAI<<GI
NC_001148.4     592340  0       121     A       394     aaAAAaaAaAaAaaAaAAAaaaaAAAaAAaAaAaaaAaaaAaaAAAaaAaAaAaaAaAAaAaaaAAaAAaAAaAAaaaAAaaAAAaaaAaAAaaAaAaAaAAAaaaaAAaaAAaaAAaaAa        GGAGGIGIGGIGGIGGGGGIIGIGGGI<GGGGGGIIGIIGG<IGG<GGGGIIGIIGIIAGGIIIGAIAAIAG<GGGGIGGGIIIIIIGAGGAIIGGAGGGIGGIIGIGGIIGGGGGAGIGI
NC_001148.4     592341  0       121     G       394     ggGGGggGgGgGggGgGGGggggGGGgGGgGgGgggGgggGggGGGggGgGgGggGgGGgGgggGGgGGgGGgGGgggGGggGGGgggGgGGggGgGgGgGGGggggGGggGGggGGggGg        GIGGIIIIIGIGIIIGGGIIIGIGGGGGIGIGGIGGGIIIGAIIGGGGGIIIIIGGIIGGGIIIIAGGGGGG.GGIGGIIIGIIIGIGGG.GIIGGAIGGIIGIG<IIIIIG<AGGGAIGI

Make fasta: syntax 
samtools consensus -r NC_001148.4:592332-593069 -f fasta ~/common/refs/snowflake_yeast/aligned/SRR23803536.sorted.bam

>NC_001148.4
CTATGAGTAGGTTTCAATCAAAGTATCACGTAGGTTACCTGAAATGGATTCTGGTTGGGCATCTTGCAAG
CGGAAAATACTTTCAATAACACTCAATTCTGGGGCTGTAGTATCCAGACCTGTAACTGCCAAGTAATCGT
TCACAACCATACCGGCACCGACAACTGAACTACCACGGTTAACGGTACCAGCCACCAAAGGAACTTGTAA
TAAGGAGGACAATTCTTCTTGATCTTGGACACTTGTTTGTGGATGCACTAACCCACCTTGATTACTTAAA
GAACAATATGACCCAACTAAGATATTACCTGATATGGTTTGACGGAAGACCTCAACGCCTAGTACATCAC
TTATCAATTCTTCAGTTTCTCTGTCGATATCTGGATGCACTAAAGCAACGTAATCATTACAACAGATGAC
GTTACCCAAGGCAGATAGTCTTTCCTCTACCCTTTGAATCTTAACGGAATCCGGCAAACTATTTCTTAAA
TGTTGTAATTCTTGATCAGTAGTTTGGGTTGGAACTAGCAGACCTCTACGGTTACCCGCGGTCATTCTAC
CGATGATACGCGTACCAGCAATAGTGGTATGAACGATGGGAATAGCATCTCCTAATTCAGCTTCAAATGC
AGAGTAAAAGTTTTCAGAACCACCAACAGCAACCAAACAGTAAGTATTCGTTAATTTGGAGAATACACCG
ATTTCATTGGAGTTTTCAAATTGAGTCCTGGTAGCCAT

Compare to reference: had syntax errors with faidx as listed in lecture, so I looked up the reference online at the
same website that listed this gene as a ribosomal complex component: https://www.ncbi.nlm.nih.gov/nuccore/NM_001184113.1 
        1 atggctacca ggactcaatt tgaaaactcc aatgaaatcg gtgtattctc caaattaacg
       61 aatacttact gtttggttgc tgttggtggt tctgaaaact tttactctgc atttgaagct
      121 gaattaggag atgctattcc catcgttcat accactattg ctggtacgcg tatcatcggt
      181 agaatgaccg cgggtaaccg tagaggtctg ctagttccaa cccaaactac tgatcaagaa
      241 ttacaacatt taagaaatag tttgccggat tccgttaaga ttcaaagggt agaggaaaga
      301 ctatctgcct tgggtaacgt catctgttgt aatgattacg ttgctttagt gcatccagat
      361 atcgacagag aaactgaaga attgataagt gatgtactag gcgttgaggt cttccgtcaa
      421 accatatcag gtaatatctt agttgggtca tattgttctt taagtaatca aggtgggtta
      481 gtgcatccac aaacaagtgt ccaagatcaa gaagaattgt cctccttatt acaagttcct
      541 ttggtggctg gtaccgttaa ccgtggtagt tcagttgtcg gtgccggtat ggttgtgaac
      601 gattacttgg cagttacagg tctggatact acagccccag aattgagtgt tattgaaagt
      661 attttccgct tgcaagatgc ccaaccagaa tccatttcag gtaacctacg tgatactttg
      721 attgaaacct actcatag 
They are reverse complements and I didn't observe polymorphisms. 
