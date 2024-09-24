import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('reports/combined_reports.csv')

# Sum the votes grouped by Component and carry over the Category column
vote_totals = df.groupby(['Category', 'Component'])[['Use', 'Study', 'Modify', 'Share']].sum().reset_index()

# Add a new column for the total votes
vote_totals['Total'] = vote_totals[['Use', 'Study', 'Modify', 'Share']].sum(axis=1)

# Add a new column for vote category based on total votes
vote_totals['Vote Category'] = pd.cut(vote_totals['Total'], 
                                       bins=[-float('inf'), 8, 16, 24, 32, float('inf')], 
                                       labels=['No', 'Lean No', 'Maybe', 'Lean Yes', 'Yes'], 
                                       right=False)

# Order by the 'Total' column in descending order
vote_totals = vote_totals.sort_values(by='Total', ascending=False)

# Write the results to a new CSV file
vote_totals.to_csv('reports/vote_totals.csv', index=False)
