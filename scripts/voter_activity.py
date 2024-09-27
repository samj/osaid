import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('data/voting_data_flattened.csv')

# Count votes by each expert
vote_counts = data['Expert'].value_counts()

# Convert to DataFrame and sort
vote_counts_df = vote_counts.reset_index()
vote_counts_df.columns = ['Expert', 'Vote Count']
vote_counts_df = vote_counts_df.sort_values(by='Vote Count', ascending=False)

# Display the result
print(vote_counts_df)

# Prepare data for the pie chart
labels = vote_counts_df['Expert']
sizes = vote_counts_df['Vote Count']
colors = plt.cm.Paired(range(len(labels)))  # Generate a color palette

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Vote Distribution by Expert')
plt.tight_layout()
plt.savefig('figures/vote_distribution_by_expert.png')
plt.close()


