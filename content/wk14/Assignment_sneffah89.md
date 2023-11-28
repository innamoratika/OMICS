## Question 1 
This is to help visualize data in a table format especially when you want to view it in windows. 

## Question 2
Using the command `head -n 1 otutab.tsv | tr -s '\t' '\n' | wc -l` there are `148` samples

## Question 3
**i**. Fix the command

`cut -f1,10 alpha.tsv | sort -n -k2,2 -t$'\t' | column -ts $'\t' | less -S`

**ii** Sort by number of reads

`cut -f1,9 alpha.tsv | sort -n -k2,2 -t$'\t' | column -ts $'\t' | less -S`

**iii** Any correlation between number of reads and species richness

The number of reads can influence the species richness or the diversity of species in a sample. However upon examination of the reads values and their corresponding richness values, this does not seem apparent. In order to ascertain any correlation, a `Pearson correlation coefficient (r)` can be performed. Pursuing this in google colab, i obtained  a positive but moderate correlation of `0.57` between reads and richness. 

See `Reads vs Richness` figure

The drawbacks of these kind of correlation analysis include the fact that correlation does not necessarily mean causation. Again, biases in sampling ,sequencing and data processing can also affect correlation results

**iv** Does richness and shannon's correlate with one another?

Again, upon examination of the shannon_e  and richness values the correlation is apparent. Therefore, a `Pearson correlation coefficient (r)` can be performed to determine this. When this was performed in google colab, a positive but moderate correlation of `0.5806` was obtained. 

See `Shannon_e vs Richness` figure

## Question 4
The Gamma diversity for this dataset is `305` OTUs

## Question 5
**i** what is striking about the diagonal values? Explain why this phenomenon exists.

Euclidean distance reflects the dissimilarity or dissimilarity between the samples. Therefore any sample ID will have an Euclidean distance of zero when compared to itself because there is no difference between them. This is why as we go diagonally across the table we see zeros, where each zero means a comparison between the same sample.  

**ii** What are two ways to present this data graphically?

The two ways the Euclidean distance can represented graphically include generating a heatmap and a Dendrogram

**iii** Make a graph! 

see `Euclidean distance heatmap` figure

**iv** Do the samples create separate groups? Do they not? What does it say about the underlying sample data?

From the `Euclidean diatance heatmap` the samples grouped into four distinct groups. This might indicate samples or observations within each cluster are more similar to each other than to samples in other clusters or exhibit a higher degree of similarity within the cluster as compared to samples in other clusters





