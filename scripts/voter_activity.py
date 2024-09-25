import pandas as pd

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
