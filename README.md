# Optimal-K-means-Clustering
Workflow for analyzing virtual screening hits with k-means clustering after first finding the optimal number of clusters

This workflow depends on use of Pat Walters's Python k-means implementation (https://github.com/PatWalters/kmeans) and Schrödinger's Glide

1) Generate the "fingerprints_parquet.gz" using this ^ workflow and [some top slice] of your virtual screening results

2) Run the generation of the clustered data using "generate_csvs.py" This was designed for clustering the top 10K results
   from a screen into a variety of different cluster counts, ranging from 10 to 10K (for exhaustive purposes)

3) Run the Jupyter notebook until you generate the plot of average cluster similarity over numbers of clusters.
   Using the "elbow" method, you can pick what seems to be the optimal number of clusters for your molecules based on where the
   relationship between similarity and cluster number turns linear.

4) When you've chosen your number of clusters, load that specific .csv file and complete the analysis.
   The rest of the workflow extracts the top-scoring compound in each cluster and outputs all of them to a new .sdf file.
