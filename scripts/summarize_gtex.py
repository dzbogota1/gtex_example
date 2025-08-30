import sys
import pandas as pd

# input file
infile = sys.argv[1]

# read gct
df = pd.read_csv(infile, sep="\t", skiprows=2)

# The expression part consists of all columns after the first 2
expr = df.iloc[:, 2:]

# Sum TPM per sample
sample_sums = expr.sum()

# Identify the sample with the highest total expression
max_sample = sample_sums.idxmax()
max_value = sample_sums.max()

# Print summary
print("summary")
print("---------------------------")
print(f"Num of genes: {df.shape[0]}")
print(f"Num of samples: {expr.shape[1]}")
print(f"Sample with higher total TPM: {max_sample} ({max_value:.2f})")
