import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

# Load the CSV file
df = pd.read_csv('reports/vote_totals.csv')

# Define vote category colors and names
vote_category_colors = ['#d1a09b', '#e8cea3', '#f9f3d1', '#d6fbc4', '#a4ea78']
vote_category_names = ['No', 'Lean No', 'Maybe', 'Lean Yes', 'Yes']

# Define indexes for each clustering scenario
indexes = {2: [0, 4], 3: [0, 2, 4], 4: [0, 1, 3, 4], 5: [0, 1, 2, 3, 4]}

# Create the figures directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

def perform_kmeans(n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df[f'Cluster_{n_clusters}'] = kmeans.fit_predict(df[['Total']])
    return kmeans

def assign_colors_and_names(kmeans, n_clusters):
    cluster_means = [kmeans.cluster_centers_[i][0] for i in range(n_clusters)]
    sorted_indices = np.argsort(cluster_means)
    cluster_colors = [vote_category_colors[indexes[n_clusters][i]] for i in sorted_indices]
    cluster_names = [vote_category_names[indexes[n_clusters][i]] for i in sorted_indices]
    return cluster_colors, cluster_names

def create_bar_chart(n_clusters):
    kmeans = perform_kmeans(n_clusters)
    
    # Sort components by total votes
    sorted_df = df.sort_values('Total', ascending=False)
    
    # Assign colors and names based on cluster means
    cluster_colors, cluster_names = assign_colors_and_names(kmeans, n_clusters)
    
    # Map clusters to colors
    cluster_to_color = {i: color for i, color in enumerate(cluster_colors)}
    colors = [cluster_to_color[cluster] for cluster in sorted_df[f'Cluster_{n_clusters}']]
    
    plt.figure(figsize=(15, 10))
    bars = plt.bar(range(len(sorted_df)), sorted_df['Total'], color=colors)
    plt.title(f'Components by Total Votes (n={n_clusters})')
    plt.xlabel('Components')
    plt.ylabel('Total Votes')
    plt.xticks(range(len(sorted_df)), sorted_df['Component'], rotation=90)
    
    # Add a legend
    legend_elements = [plt.Rectangle((0,0),1,1, color=color, label=name) 
                       for color, name in zip(cluster_colors, cluster_names)]
    plt.legend(handles=legend_elements)
    
    plt.tight_layout()
    plt.savefig(f'figures/bar_chart_n{n_clusters}.png')
    plt.close()

# Create bar charts for n=2, 3, 4, 5
for n in [2, 3, 4, 5]:
    create_bar_chart(n)

print("Bar charts have been saved in the 'figures' directory.")
