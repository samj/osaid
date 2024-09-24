import pandas as pd
import os

def read_markdown_table(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Predefined column headers
    headers = ['Component', 'Use', 'Study', 'Modify', 'Share']
    
    rows = []
    current_category = None
    
    for line in lines:
        line = line.strip()
        
        # Check for category line
        if line.startswith('|**') and '** ' in line:
            current_category = line.split('**')[1].strip()
            continue
        
        # Skip markdown table formatting line
        if line.startswith('| ---'):
            continue
        
        # Process table rows
        if '|' in line:
            cells = [cell.strip() for cell in line.split('|')]
            # Remove leading and trailing empty strings
            if cells[0] == '':
                cells = cells[1:]
            if cells[-1] == '':
                cells = cells[:-1]
            if len(cells) == len(headers):
                if current_category is not None:
                    cells.insert(0, current_category)  # Insert category as the first column
                    rows.append(cells)
    
    if not rows:
        return None
    
    # Create DataFrame
    df = pd.DataFrame(rows, columns=['Category'] + headers)
    
    return df

def read_all_reports(directory):
    all_reports = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            df = read_markdown_table(file_path)
            if df is not None:
                df.insert(0, 'System', os.path.basename(filename).replace('.md', ''))  # Add system column as the first column
                all_reports.append(df)
    
    if not all_reports:
        print("No valid tables found in the directory.")
        return pd.DataFrame()  # Return an empty DataFrame if no valid tables are found
    
    # Concatenate all DataFrames
    combined_df = pd.concat(all_reports, ignore_index=True)
    
    return combined_df

# Directory containing the markdown reports
reports_directory = 'reports'

# Read all reports into a single DataFrame
df = read_all_reports(reports_directory)

if not df.empty:
    # Display the DataFrame
    print(df)
else:
    print("No data to display.")
