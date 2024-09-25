import pandas as pd

# Load the CSV file
df = pd.read_csv('reports/vote_totals.csv')

# Calculate the average of the 'Total' column
average_total = df['Total'].mean()

print(f"The average of the 'Total' column is: {average_total}")
thresholds = {
    "Yes": 2 * average_total,
    "Lean Yes": 1.5 * average_total,
    "Maybe": average_total,
    "Lean No": 0.5 * average_total,
    "No": 0
}

for category, threshold in thresholds.items():
    print(f"Threshold for '{category}': {threshold}")
