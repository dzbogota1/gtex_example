#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt

infile, outfile = sys.argv[1], sys.argv[2]

# Read the GCT (skip the first 2 metadata rows)
df = pd.read_csv(infile, sep="\t", skiprows=2)

# Columns with TPMs
expr = df.iloc[:, 2:]

# For each gene: find max TPM and tissue
df["max_TPM"] = expr.max(axis=1)
df["best_tissue"] = expr.idxmax(axis=1)

# Select top 10 genes by TPM
top_genes = df.nlargest(10, "max_TPM")

# Create labels in GENE (Tissue) format
labels = [f"{gene} ({tissue})" 
          for gene, tissue in zip(top_genes["Description"], top_genes["best_tissue"])]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(labels, top_genes["max_TPM"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("max observed TPM")
plt.title("Top 10 genes by tissue")
plt.tight_layout()
plt.savefig(outfile, dpi=300)

print(f"plot saved in {outfile}")