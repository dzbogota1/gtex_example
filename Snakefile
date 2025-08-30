rule download_gtex:
    output:
        "data/GTEx_gene_tpm.gct.gz"
    shell:
        """
        mkdir -p data
        wget -O {output} https://storage.googleapis.com/adult-gtex/bulk-gex/v10/rna-seq/GTEx_Analysis_v10_RNASeQCv2.4.2_gene_median_tpm.gct.gz
        """

rule extract_gtex:
    input:
        "data/GTEx_gene_tpm.gct.gz"
    output:
        "data/GTEx_gene_tpm.gct"
    shell:
        """
        gunzip -c {input} > {output}
        """

rule summarize_gtex:
    input:
        "data/GTEx_gene_tpm.gct"
    shell:
        """
        python scripts/summarize_gtex.py {input}
        """

rule plot_top_genes:
    input:
        "data/GTEx_gene_tpm.gct"
    output:
        "results/top_genes.png"
    shell:
        """
        mkdir -p results
        python scripts/plot_top_genes.py {input} {output}
        """

