# Usage Guide

## Overview

sailaps provides command-line utilities for managing sailing application data between SailWave and Sailrace.

## Basic Workflow

### Convert SailWave JSON to Sailrace CSV

sailaps can convert exported SailWave data (JSON format) into CSV format suitable for Sailrace import.

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run the conversion script
python src/app.py
```

This will:
1. Read `src/Xmas.json` (SailWave export)
2. Extract competitor data (sailors, sail numbers, class, fleet, etc.)
3. Filter out empty placeholder entries
4. Generate `competitors.csv` in the project root

### CSV Output Format

The generated CSV includes the following columns:
- **SailNo** - Sail number
- **Class** - Boat class (e.g., Pico, Solo)
- **Fleet** - Fleet/Division assignment
- **Helm** - Helmsman/Sailor name
- **PY** - Portsmouth Yardstick rating
- **Nationality** - Competitor nationality
- **Medical** - Medical conditions
- **Medical Flag** - Medical flag indicator
- **Age Group** - Age group classification
- **Email** - Email address
- **Sex** - Gender
- **Photo Path** - Path to competitor photo

### Example Output

```
SailNo,Class,Fleet,Helm,PY,Nationality,Medical,Medical Flag,Age Group,Email,Sex,Photo Path
7891,Pico,Small,Molly Stanbridge,,IRL,Bonkers,1,18,mmstanbridge@icloud.com,Female,\\192.168.1.23\public\Pictures\20230801_140730.jpg
4645,SOLO,Medium,James Stanbridge,1139,GBR,Insulin Dependent Diabetic,1,Senior,jstanbridge@gmail.com,Male,\\192.168.1.23\public\Pictures\20230901_143304.jpg
```

## Configuration

### Input Files

- **SailWave JSON**: `src/Xmas.json` (or specify custom path)
- Location: Must be in the `src/` directory or provide full path

### Output Files

- **Competitors CSV**: `competitors.csv` (in project root)
- Format: UTF-8 encoded, comma-separated values

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_example.py

# Run specific test class
pytest tests/test_example.py::TestJsonToCsvConversion
```

## Code Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Run linting
pylint src/

# Type checking
mypy src/
```

## Troubleshooting

### FileNotFoundError: Xmas.json

**Issue:** Cannot find input JSON file

**Solution:** 
1. Ensure `Xmas.json` is in the `src/` directory
2. The script uses relative paths - run from project root

### CSV Import Errors

**Issue:** Sailrace rejects the generated CSV

**Solution:**
1. Check the CSV file format in `competitors.csv`
2. Verify column headers match expected format
3. Check for special characters in data

### Empty CSV Output

**Issue:** CSV has only headers, no data rows

**Solution:**
1. Verify input JSON has competitors with `compsailno` field
2. The script filters out empty placeholder entries
3. Check JSON structure with a JSON viewer

## Support

For issues or questions:
1. Check the logs if available
2. Review [API Reference](./api.md)
3. File an issue on GitHub
