# API Reference

This page documents the public API for sailaps modules.

## Module: app

Main module for converting SailWave JSON data to Sailrace CSV format.

### Functions

#### `json_to_csv(json_file: str, csv_file: str) -> None`

Convert SailWave JSON export to Sailrace CSV format.

Reads a SailWave JSON export file, extracts competitor data, filters out empty placeholders, and writes valid competitors to a CSV file suitable for Sailrace import.

**Parameters:**
- `json_file` (str): Path to input SailWave JSON file
- `csv_file` (str): Path for output CSV file

**Returns:**
- `None`

**Raises:**
- `FileNotFoundError`: If JSON input file doesn't exist
- `json.JSONDecodeError`: If JSON file is invalid
- `IOError`: If unable to write CSV file

**Filtering:**
- Only competitors with a `compsailno` (sail number) are exported
- Empty placeholder entries (no sail number) are automatically filtered out

**CSV Columns Output:**
1. SailNo - Sail number
2. Class - Boat class
3. Fleet - Fleet/Division
4. Helm - Helmsman name
5. PY - Portsmouth Yardstick rating
6. Nationality - Competitor nationality
7. Medical - Medical conditions
8. Medical Flag - Medical flag indicator
9. Age Group - Age group
10. Email - Email address
11. Sex - Gender
12. Photo Path - Photo file path

**Example:**
```python
from src.app import json_to_csv

# Convert SailWave JSON to Sailrace CSV
json_to_csv('src/Xmas.json', 'competitors.csv')
```

**Usage from Command Line:**
```bash
# Run the main script
python src/app.py
```

## JSON Input Format

Expected SailWave JSON structure:

```json
{
  "competitors": {
    "1": {
      "compsailno": "7891",
      "compclass": "Pico",
      "compdivision": "Small",
      "comphelmname": "Sailor Name",
      "comprating": "",
      "compnat": "IRL",
      "compmedical": "",
      "compmedicalflag": "0",
      "comphelmagegroup": "18",
      "comphelmemail": "sailor@example.com",
      "comphelmsex": "Female",
      "comphelmphoto": ""
    }
  }
}
```

## Error Handling

The module provides clear error messages for common issues:

```python
from src.app import json_to_csv

try:
    json_to_csv('input.json', 'output.csv')
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
except IOError:
    print("Unable to write CSV file")
```

## Performance

- Processing time depends on competitor count
- Example: 2 competitors processed in ~0.1 seconds
- Memory efficient: processes data inline without holding large structures

## Type Hints

All functions use type hints for better IDE support:

```python
def json_to_csv(json_file: str, csv_file: str) -> None:
    """Convert JSON to CSV."""
    pass
```

## Version Compatibility

- **Python**: 3.12+
- **Standard Library**: Uses only json, csv, pathlib modules
- **No External Dependencies Required** for core functionality

## See Also

- [Installation Guide](./installation.md)
- [Usage Guide](./usage.md)
- [Contributing](./contributing.md)
