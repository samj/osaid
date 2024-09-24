import pandas as pd
import ace_tools_open as tools

# Load the CSV file
file_path = 'component_voting_raw.csv'
raw_votes = pd.read_csv(file_path)

# Show the structure of the data to understand the format
raw_votes.head()


# Define a function to parse the votes and split them into freedoms and initials
def parse_votes(vote_str):
    freedoms = ['Use', 'Study', 'Modify', 'Share']
    parsed_votes = {freedom: [] for freedom in freedoms}
    
    if isinstance(vote_str, str):
        # Split by freedom categories
        for freedom in freedoms:
            if freedom in vote_str:
                # Extract the part corresponding to the freedom
                start_idx = vote_str.find(freedom) + len(freedom) + 1
                end_idx = vote_str.find('//', start_idx)
                if end_idx == -1:
                    end_idx = len(vote_str)
                initials = vote_str[start_idx:end_idx].strip()
                # Remove commas and extra spaces, then split by space
                parsed_votes[freedom] = initials.replace(",", "").split()
    return parsed_votes

# Process the data into a structured format
structured_data = []

# Iterate over each row in the raw data
for idx, row in raw_votes.iterrows():
    component = row['Component']
    for system in ['Llama', 'Pythia', 'OpenCV', 'Bloom']:
        vote_str = row[system]
        parsed_vote = parse_votes(vote_str)
        for freedom, voters in parsed_vote.items():
            for voter in voters:
                structured_data.append({
                    'Component': component,
                    'System': system,
                    'Freedom': freedom,
                    'Voter': voter
                })

# Convert the structured data into a DataFrame
votes_df = pd.DataFrame(structured_data)

# Display the cleaned-up and flattened data to the user
tools.display_dataframe_to_user(name="Flattened Votes Data", dataframe=votes_df)
