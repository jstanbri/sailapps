# sailaps Documentation

Welcome to the sailaps documentation. This is a Python-based toolkit for managing sailing applications collaboration.

## Overview

sailaps provides utilities for:
- Understanding JSON exported from SailWave
- Building CSV files for import into Sailrace
- Syncing data from Sailrace back to SailWave

## Quick Start

### Installation

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the project root:
```
HUBSPOT_API_KEY=your_api_key_here
```

2. The application reads configuration from environment variables

## Project Structure

```
sailaps/
├── src/               # Main application code
├── tests/             # Test suite
├── docs/              # Documentation
├── .env               # Environment variables (local only)
├── requirements.txt   # Python dependencies
└── README.md          # Project overview
```

## Documentation

- [Installation Guide](./installation.md)
- [User Guide](./usage.md)
- [API Reference](./api.md)
- [Contributing](./contributing.md)

## Key Concepts

### Data Flow

1. Export JSON from SailWave
2. Process with sailaps scripts
3. Generate CSV for Sailrace
4. Import into Sailrace
5. Sync changes back to SailWave

### Dependencies

- **requests** - HTTP API calls
- **pandas** - Data processing
- **openpyxl** - Excel file support
- **python-dotenv** - Environment configuration

## Logging

All operations are logged to the `logs/` directory with timestamps and status information.

## Support

For issues or questions, refer to the project's GitHub repository or contact the maintainers.
