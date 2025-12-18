# sailapps
At our Sailing Club, we use sailwave for managing results. However there exist great mobile apps (Sailrace) that I would like to be able to use, however, they need this shim to swap data back and forth.

## Project Overview

**sailaps** is a Python-based toolkit for managing sailing applications collaboration. It provides utilities for converting SailWave data to Sailrace format.

### Purpose

- Understand json exported from SailWave
- Build csv files for import into Sailrace
- Sync data from Sailrace back to SailWave

### Tech Stack

- **Language**: Python 3.12+
- **Data Handling**: JSON input, CSV output
- **Configuration**: .env file for API credentials (local only)

### Current Status

- **Branch**: `development/0.0.1`
- **Default Branch**: `main`

### Typical Workflow

1. User exports json file with race series data from SailWave
2. Script converts to csv for Sailrace import
3. User exports from Sailrace
4. Script syncs data back to SailWave

## Documentation

For detailed information, see the [documentation](docs/):
- **[Installation Guide](docs/installation.md)** - Setup and troubleshooting
- **[Usage Guide](docs/usage.md)** - How to use the conversion tool
- **[API Reference](docs/api.md)** - Function documentation and examples
- **[Contributing](docs/contributing.md)** - How to contribute to the project

## Quick Start

### Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Convert SailWave JSON to Sailrace CSV

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run the conversion
python src/app.py
```

This reads `src/Xmas.json` and generates `competitors.csv` in the project root.

## Features

✓ Convert SailWave JSON exports to Sailrace CSV format
✓ Automatically filter out empty competitor placeholders
✓ Extract competitor data (sailors, sail numbers, class, fleet, etc.)
✓ Comprehensive test coverage (83%)
✓ Zero external dependencies for core functionality
✓ Cross-platform file path handling
