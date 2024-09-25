import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os
import re
import ast

def parse_cluster_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    ordered_names = []
    ordered_colors = []
    components_by_cluster = {}
    current_cluster = None

    # Flags to track sections
    in_components_section = False

    for i, line in enumerate(lines):
        line = line.strip()

        # Check for Ordered names
        if line.startswith("Ordered names:"):
            names_str = line[len("Ordered names:"):].strip()
            ordered_names = ast.literal_eval(names_str)

        elif line.startswith("Ordered colors:"):
            colors_str = line[len("Ordered colors:"):].strip()
            ordered_colors = ast.literal_eval(colors_str)

        # Check for the start of Components section
        elif line.startswith("Components by cluster for n="):
            in_components_section = True

        elif in_components_section:
            # Check for Cluster headers
            cluster_match = re.match(r'^Cluster (.+?) \(Mean: ([\d\.]+)\):$', line)
            if cluster_match:
                cluster_name = cluster_match.group(1).strip()
                cluster_mean = float(cluster_match.group(2))
                current_cluster = {
                    'mean': cluster_mean,
                    'components': []
                }
                components_by_cluster[cluster_name] = current_cluster
            elif line.startswith("-") and current_cluster is not None:
                # Parse component lines
                comp_match = re.match(r'^- (.+?) \(Mean: ([\d\.]+)\)$', line)
                if comp_match:
                    comp_name = comp_match.group(1).strip()
                    comp_mean = float(comp_match.group(2))
                    current_cluster['components'].append((comp_name, comp_mean))
            elif not line:
                # Empty line indicates possible end of components
                continue
            else:
                # Any other content is ignored within the components section
                continue

    # Validate that we have the required data
    if not ordered_names or not ordered_colors:
        raise ValueError(f"Ordered names or colors not found in {filename}")

    return ordered_names, ordered_colors, components_by_cluster

def create_bar_chart(N, ordered_names, ordered_colors, components_by_cluster):
    # Collect data for plotting
    names = []
    means = []
    colors = []
    cluster_color_map = dict(zip(ordered_names, ordered_colors))

    for cluster_name in ordered_names:
        cluster_data = components_by_cluster.get(cluster_name, {})
        cluster_components = cluster_data.get('components', [])
        cluster_color = cluster_color_map[cluster_name]

        for comp_name, comp_mean in cluster_components:
            names.append(comp_name)
            means.append(comp_mean)
            colors.append(cluster_color)

    # Create bar chart
    plt.figure(figsize=(14, 7))
    bar_positions = range(len(names))
    plt.bar(bar_positions, means, color=colors)

    # Set labels and title
    plt.xticks(bar_positions, names, rotation=90)
    plt.ylabel('Mean')
    plt.title(f'Components by Cluster (n={N})')

    # Add legend
    legend_elements = [Patch(facecolor=cluster_color_map[name], label=name) for name in ordered_names]
    plt.legend(handles=legend_elements)

    # Adjust layout to prevent clipping of tick-labels
    plt.tight_layout()

    # Save the figure to a file
    output_filename = f'figures/components_by_cluster_bar_chart_{N}.png'
    plt.savefig(output_filename, dpi=300)
    plt.close()

    print(f"Bar chart saved to {output_filename}")

def main():
    for N in [2, 3, 4, 5]:
        filename = f'figures/kmeans_cluster_{N}.txt'
        if not os.path.exists(filename):
            print(f"File {filename} does not exist. Skipping.")
            continue

        try:
            ordered_names, ordered_colors, components_by_cluster = parse_cluster_file(filename)
            create_bar_chart(N, ordered_names, ordered_colors, components_by_cluster)
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

if __name__ == "__main__":
    main()
    