# sailaps Documentation

Welcome to the sailaps documentation. A Python toolkit for converting SailWave sailing race data to Sailrace CSV format.

## Overview

sailaps provides utilities for:
- Converting SailWave JSON exports to Sailrace-compatible CSV
- Extracting competitor data (sailors, sail numbers, class, fleet, ratings, etc.)
- Filtering invalid/placeholder entries automatically
- Generating formatted CSV output ready for import

## Quick Start

### Installation

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Convert SailWave JSON to CSV
python src/app.py
```

This reads `src/Xmas.json` and outputs `competitors.csv` to the project root.

## Project Structure

```
sailaps/
├── src/               # Source code
│   ├── app.py        # Main JSON to CSV conversion
│   └── Xmas.json     # Example SailWave export
├── tests/            # Test suite
├── docs/             # Documentation
├── .github/          # GitHub Actions CI/CD
├── .env              # Environment variables (local only)
├── requirements.txt  # Python dependencies
└── README.md         # Project overview
```

## Key Features

✓ **Automatic Filtering** - Skips empty placeholder entries, only exports valid competitors with sail numbers

✓ **Clean CSV Output** - Generates properly formatted CSV with standard headers compatible with Sailrace

✓ **Type Hints** - All code includes type hints for better IDE support

✓ **Comprehensive Tests** - 83% code coverage with unit tests for core functionality

✓ **Zero External Dependencies** - Uses only Python standard library (json, csv, pathlib)

## Data Flow

```
SailWave JSON (Xmas.json)
        ↓
   json_to_csv()
        ↓
   Filter empty entries
        ↓
   Extract competitor data
        ↓
   Format as CSV
        ↓
   Output (competitors.csv)
```

## Documentation

- [Installation Guide](./installation.md) - Setup and troubleshooting
- [Usage Guide](./usage.md) - How to use the conversion tool
- [API Reference](./api.md) - Function documentation and examples
- [Contributing](./contributing.md) - How to contribute to the project

## Example Output

Input: `src/Xmas.json` with 12 competitor entries (10 empty placeholders + 2 valid)

Output: `competitors.csv` with 2 data rows (only valid competitors)

```
SailNo,Class,Fleet,Helm,PY,Nationality,Medical,Medical Flag,Age Group,Email,Sex,Photo Path
7891,Pico,Small,Molly Stanbridge,,IRL,Bonkers,1,18,mmstanbridge@icloud.com,Female,\\server\path
4645,SOLO,Medium,James Stanbridge,1139,GBR,Insulin Dependent Diabetic,1,Senior,jstanbridge@gmail.com,Male,\\server\path
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Current coverage: 83%
```

## Key Files

- **src/app.py** - JSON to CSV conversion function
- **src/Xmas.json** - Example SailWave export
- **tests/test_example.py** - Comprehensive test suite
- **requirements.txt** - Project dependencies

## Support

For issues or questions:
1. Check the [Usage Guide](./usage.md)
2. Review [API Reference](./api.md)
3. File an issue on GitHub

## Version

Current: **0.0.1 (Development)**

Language: **Python 3.12+**
