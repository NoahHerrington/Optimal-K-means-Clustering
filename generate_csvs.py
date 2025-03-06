import os
import numpy as np

clusters_lin = np.linspace(10,10000,100).round()

clusters = [int(num) for num in clusters_lin]

for cluster in clusters: os.system(f"python3 kmeans.py \
        cluster --fp_file fingerprints_parquet.gz \
        --clusters {cluster} --out km_{cluster}clustered_results.csv")
