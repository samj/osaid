import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('reports/vote_totals.csv')

# Define colors for Vote Categories
vote_category_colors = {
    'Yes': '#a4ea78',
    'Lean Yes': '#d6fbc4',
    'Maybe': '#f9f3d1',
    'Lean No': '#e8cea3',
    'No': '#d1a09b'
}

# Group by Category and sum the votes
category_totals = df.groupby('Category').sum().reset_index()

# Sort by Total votes in descending order
category_totals = category_totals.sort_values(by='Total', ascending=False)

# Bar chart of total votes by category
plt.figure(figsize=(10, 6))
plt.bar(category_totals['Category'], category_totals['Total'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Total Votes')
plt.title('Total Votes by Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/total_votes_by_category.png')
plt.close()

# Stacked bar chart of total votes by category showing the freedoms
freedoms = ['Use', 'Study', 'Modify', 'Share']
category_totals_freedoms = df.groupby('Category')[freedoms].sum().reset_index()
category_totals_freedoms = category_totals_freedoms.set_index('Category')
category_totals_freedoms = category_totals_freedoms.loc[category_totals['Category']]  # Ensure same order

category_totals_freedoms.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.xlabel('Category')
plt.ylabel('Total Votes')
plt.title('Total Votes by Category and Freedom')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/stacked_votes_by_category.png')
plt.close()

# Group by Component and sum the votes
component_totals = df.groupby('Component').sum().reset_index()

# Sort by Total votes in descending order
component_totals = component_totals.sort_values(by='Total', ascending=False)

# Bar chart of total votes by component with colors based on Vote Category
colors = df.set_index('Component').loc[component_totals['Component']]['Vote Category'].map(vote_category_colors)

plt.figure(figsize=(10, 6))
plt.bar(component_totals['Component'], component_totals['Total'], color=colors)
plt.xlabel('Component')
plt.ylabel('Total Votes')
plt.title('Total Votes by Component')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.legend(handles=[plt.Line2D([0], [0], color=color, lw=4, label=label) for label, color in vote_category_colors.items()])
plt.savefig('figures/total_votes_by_component.png')
plt.close()

# Stacked bar chart of total votes by component showing the freedoms
component_totals_freedoms = df.groupby('Component')[freedoms].sum().reset_index()
component_totals_freedoms = component_totals_freedoms.set_index('Component')
component_totals_freedoms = component_totals_freedoms.loc[component_totals['Component']]  # Ensure same order

component_totals_freedoms.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.xlabel('Component')
plt.ylabel('Total Votes')
plt.title('Total Votes by Component and Freedom')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/stacked_votes_by_component.png')
plt.close()
