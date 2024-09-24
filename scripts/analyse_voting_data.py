#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the CSV file
file_path = '../data/voting_data_consolidated.csv'
df = pd.read_csv(file_path)

# Define systems and freedoms
systems = ['Llama', 'Pythia', 'OpenCV', 'Bloom']
freedoms = ['Use', 'Study', 'Modify', 'Share']
category_order = ['Code', 'Data', 'Model', 'Other']

# Function to parse votes into a dictionary structure
def parse_votes(vote_string):
    vote_data = {freedom: [] for freedom in freedoms}
    if isinstance(vote_string, str):
        for freedom_vote in vote_string.split('//'):
            for freedom in freedoms:
                if freedom in freedom_vote:
                    experts = re.findall(r'[A-Z]{2,4}', freedom_vote)
                    vote_data[freedom] = experts
    return vote_data

# Process the data into a structured format
processed_data = []
for _, row in df.iterrows():
    component = row['Component']
    category = row['Category']
    for system in systems:
        parsed = parse_votes(row[system])
        for freedom in freedoms:
            for expert in parsed[freedom]:
                processed_data.append({
                    'Category': category,
                    'Component': component,
                    'System': system,
                    'Freedom': freedom,
                    'Expert': expert
                })

# Create a dataframe from the processed data
processed_df = pd.DataFrame(processed_data)

# Total votes per component
total_votes_per_component = processed_df.groupby('Component').size().reset_index(name='Total Votes')

# Votes per freedom per component
votes_per_freedom_component = processed_df.groupby(['Component', 'Freedom']).size().unstack(fill_value=0).reset_index()

# Total votes per category
total_votes_per_category = processed_df.groupby('Category').size().reset_index(name='Total Votes')

# Total votes per freedom
total_votes_per_freedom = processed_df.groupby('Freedom').size().reset_index(name='Total Votes')

# Sort the total votes per component for descending and ascending
total_votes_per_component_sorted = total_votes_per_component.sort_values(by='Total Votes', ascending=False)
total_votes_per_component_asc = total_votes_per_component.sort_values(by='Total Votes', ascending=True)

# Plot 1: Total votes per component (descending)
plt.figure(figsize=(10, 8))
plt.barh(total_votes_per_component_sorted['Component'], total_votes_per_component_sorted['Total Votes'], color='skyblue')
plt.xlabel('Total Votes')
plt.ylabel('Component')
plt.title('Total Votes per Component')
plt.tight_layout()
plt.savefig('../figures/total_votes_per_component_desc.png')
plt.close()

# Plot 2: Total votes per component (ascending)
plt.figure(figsize=(10, 8))
plt.barh(total_votes_per_component_asc['Component'], total_votes_per_component_asc['Total Votes'], color='lightgreen')
plt.xlabel('Total Votes')
plt.ylabel('Component')
plt.title('Total Votes per Component')
plt.tight_layout()
plt.savefig('../figures/total_votes_per_component_asc.png')
plt.close()

# Plot 3: Total votes per category
plt.figure(figsize=(10, 6))
plt.bar(total_votes_per_category['Category'], total_votes_per_category['Total Votes'], color='orange')
plt.xlabel('Category')
plt.ylabel('Total Votes')
plt.title('Total Votes per Category')
plt.tight_layout()
plt.savefig('../figures/total_votes_per_category.png')
plt.close()

# Plot 4: Total votes per freedom
plt.figure(figsize=(10, 6))
plt.bar(total_votes_per_freedom['Freedom'], total_votes_per_freedom['Total Votes'], color='purple')
plt.xlabel('Freedom')
plt.ylabel('Total Votes')
plt.title('Total Votes per Freedom')
plt.tight_layout()
plt.savefig('../figures/total_votes_per_freedom.png')
plt.close()

# Stacked bar chart for votes per freedom per component (ascending)
freedom_order = ['Use', 'Study', 'Modify', 'Share']
votes_per_freedom_component_sorted = votes_per_freedom_component[freedom_order].set_index(votes_per_freedom_component['Component']).sort_values(by='Use', ascending=True)

plt.figure(figsize=(12, 8))
votes_per_freedom_component_sorted.plot(kind='barh', stacked=True, figsize=(12, 8), color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
plt.xlabel('Total Votes')
plt.ylabel('Component')
plt.title('Votes per Freedom per Component')
plt.tight_layout()
plt.savefig('../figures/votes_per_freedom_per_component.png')
plt.close()
