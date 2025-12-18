# sailaps - Project Brief

## Project Overview

**sailaps** is a Python-based toolkit for managing sailing applications collaboration. It provides two main utilities for syncing and organizing sailors data.

### Purpose

- Understand json exported from SailWave
- Build csv files for import into Sailrace
- Sync data from Sailrace back to SailWave

### Tech Stack

- **Language**: Python 3.12+
- **Primary Dependency**: None
- **Data Handling**: Pandas, Excel files (.xlsx), CSV files
- **Configuration**: .env file for API credentials
- **Logging**: File-based logs in `logs/` directory

### Key Files

- `.env` - API credentials (HUBSPOT_API_KEY) - **not in version control**

### Current Status

- **Branch**: `development/0.0.1`
- **Default Branch**: `main`

### Dependencies

- `requests` - HTTP API calls to HubSpot
- `pandas` - CSV and Excel file handling
- `openpyxl` - Excel file support
- `python-dotenv` - Environment variable management

### Typical Workflow

1. User exports json file with race series data from SailWave
2. Script converts to csv for Sailrace import
3. User exports from Sailrace
4. Script syncs data back to SailWave
5. Logs and reports generated in `logs/` and as `.txt` files

### Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env with your HubSpot API key

### Important Notes

- API key is stored in `.env` (never commit this file)
- Logs are persistent in `logs/` directory for debugging
