import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
import numpy as np

# Load the CSV file
df = pd.read_csv('reports/vote_totals.csv')

# Extract the 'Total' column
total_values = df[['Total']]

# Define ordered vote category colors and names
vote_category_colors = ['#d1a09b', '#e8cea3', '#f9f3d1', '#d6fbc4', '#a4ea78']
vote_category_names = ['No', 'Lean No', 'Maybe', 'Lean Yes', 'Yes']

# Define indexes for each clustering scenario
indexes_2 = [0, 4]
indexes_3 = [0, 2, 4]
indexes_4 = [0, 1, 3, 4]
indexes_5 = [0, 1, 2, 3, 4]

# Function to perform K-means clustering and plot results
def perform_kmeans(n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df[f'Cluster_{n_clusters}'] = kmeans.fit_predict(total_values)
    return kmeans

# Perform K-means clustering for n=2, 3, 4, and 5
kmeans_2 = perform_kmeans(2)
kmeans_3 = perform_kmeans(3)
kmeans_4 = perform_kmeans(4)
kmeans_5 = perform_kmeans(5)

# Create the figures directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

# Function to assign colors and names based on cluster means
def assign_colors_and_names(kmeans, colors, names):
    cluster_means = kmeans.cluster_centers_.flatten()
    sorted_indices = np.argsort(cluster_means)[::-1]  # Sort in descending order
    return [colors[i] for i in sorted_indices], [names[i] for i in sorted_indices]

# Function to print components by cluster
def print_components_by_cluster(kmeans, n_clusters, file, ordered_names):
    cluster_means = kmeans.cluster_centers_.flatten()
    sorted_indices = np.argsort(cluster_means)[::-1]
    for i, idx in enumerate(sorted_indices):
        cluster_components = df[df[f'Cluster_{n_clusters}'] == idx]['Component'].tolist()
        file.write(f"Cluster {ordered_names[i]} (Mean: {cluster_means[idx]:.2f}): {cluster_components}\n")

# Plotting the results
plt.figure(figsize=(24, 6))

with open('figures/kmeans_clusters.txt', 'w') as file:
    for i, (kmeans, n_clusters, indexes) in enumerate([(kmeans_2, 2, indexes_2), (kmeans_3, 3, indexes_3), (kmeans_4, 4, indexes_4), (kmeans_5, 5, indexes_5)], start=1):
        selected_colors = [vote_category_colors[j] for j in indexes]
        selected_names = [vote_category_names[j] for j in indexes]
        ordered_colors, ordered_names = assign_colors_and_names(kmeans, selected_colors, selected_names)
        cluster_labels = kmeans.labels_
        plt.subplot(1, 4, i)
        for j in range(n_clusters):
            cluster_points = total_values[cluster_labels == j]
            plt.scatter(cluster_points, [0]*len(cluster_points), c=ordered_colors[j], label=ordered_names[j])
        plt.scatter(kmeans.cluster_centers_, [0]*n_clusters, c='red', marker='x', s=200, linewidths=3)
        plt.title(f'K-means Clustering (n={n_clusters})')
        plt.xlabel('Total')
        plt.yticks([])
        plt.legend()

        # Print components by cluster
        file.write(f"\nComponents by cluster for n={n_clusters}:\n")
        print_components_by_cluster(kmeans, n_clusters, file, ordered_names)

plt.tight_layout()
plt.savefig('figures/kmeans_clustering.png')
plt.show()
