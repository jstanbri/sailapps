import json
import csv

def json_to_csv(json_file, csv_file):
    """Convert Xmas.json competitors data to CSV format."""
    
    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract competitors data
    competitors = data.get('competitors', {})
    
    # Define the CSV columns and their JSON mappings
    csv_columns = [
        ('SailNo', 'compsailno'),
        ('Class', 'compclass'),
        ('Fleet', 'compdivision'),
        ('Helm', 'comphelmname'),
        ('PY', 'comprating'),
        ('Nationality', 'compnat'),
        ('Medical', 'compmedical'),
        ('Medical Flag', 'compmedicalflag'),
        ('Age Group', 'comphelmagegroup'),
        ('Email', 'comphelmemail'),
        ('Sex', 'comphelmsex'),
        ('Photo Path', 'comphelmphoto'),
    ]
    
    # Extract header names
    headers = [col[0] for col in csv_columns]
    
    # Extract data rows - only include competitors with actual data
    rows = []
    for comp_id, comp_data in competitors.items():
        # Skip empty placeholders - only include if they have a sail number
        if not comp_data.get('compsailno'):
            continue
        
        row = []
        for header, json_key in csv_columns:
            value = comp_data.get(json_key, '')
            row.append(value)
        rows.append(row)
    
    # Write to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"✓ Successfully converted {json_file} to {csv_file}")
    print(f"  Exported {len(rows)} competitors")

# Usage
if __name__ == '__main__':
    from pathlib import Path
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Use paths relative to the script directory
    json_file = script_dir / 'Xmas.json'
    csv_file = script_dir.parent / 'competitors.csv'
    
    json_to_csv(str(json_file), str(csv_file))