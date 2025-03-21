# Optimal-K-means-Clustering
Workflow for analyzing virtual screening hits with k-means clustering after first finding the optimal number of clusters

This workflow depends on use of Pat Walters's Python k-means implementation (https://github.com/PatWalters/kmeans) and Schrödinger's Glide

-------------
Dependencies:
-------------
	- natsort 8.4.0
	- pandas 2.1.1
	- numpy 1.26.0
	- mols2grid 2.0.0
	- matplotlib 3.8.1
	- rdkit 2024.9.5
	- notebook 7.0.4

"natsort" and "mols2grid", specifically, were installed using pip3.

1) Generate the "fingerprints_parquet.gz" using this ^ workflow and [some top slice] of your virtual screening results

2) Run the generation of the clustered data using "generate_csvs.py" This was designed for clustering the top 10K results
   - from a screen into a variety of different cluster counts, ranging from 10 to 10K (for exhaustive purposes)

3) Run the Jupyter notebook until you generate the plot of average cluster similarity over numbers of clusters.
   - Using the "elbow" method, you can pick what seems to be the optimal number of clusters for your molecules based on where the
   relationship between similarity and cluster number turns linear.

4) When you've chosen your number of clusters, load that specific .csv file and run the analysis until you output the "tophits.sdf" file.
   - This will extract the top-scoring compound in each cluster and output all of them to a new .sdf file.

5) Perform the visual inspection of hits in "tophits.sdf" to determine which clusters (based on those molecules) seem interesting.
   - The next steps are based on examining inspecting the molecules, where it's necessary to keep track of the frames of the molecules as indices you'll reference later.
   - This workflow was built more for use in PyMOL.
   - If used with Maestro, you'll have to make sure "tophits.sdf" is ordered to start at the first object (i.e. the top-most molecule must start at index 1)

6) Back in the notebook, manually input which frame numbers for the compounds in the clusters you'd like to inspect.
   - Complete the analysis to output the top N molecules in the desired clusters to a new SDF.
