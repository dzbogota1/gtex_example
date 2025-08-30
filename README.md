GTEx TPM Histogram
==================

This project downloads a transcript per million (TPM) file from a public GTEx URL, decompresses it, performs a quick analysis of its contents, and generates a histogram that visualizes the genes with the highest expression levels (top TPM values).

Steps:

1 - Download: Retrieve the TPM dataset from the specified GTEx URL.

2 - Decompress: Unpack the file for further processing.

3 - Analysis: Parse the dataset and identify the most highly expressed genes.

4 - Visualization: Produce a histogram displaying the top expressed genes based on TPM.

Output:

- results/top10.tsv: Table of the top expressed genes.

- results/top10_hist.png: Histogram plot of the top genes by TPM.
