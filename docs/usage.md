# Usage Guide

## Overview

sailaps provides command-line utilities for managing sailing application data between SailWave and Sailrace.

## Basic Workflow

### 1. Export Data from SailWave

Export race series data from SailWave as JSON format.

### 2. Process with sailaps

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run processing script
python -m src.makelist
```

### 3. Generate CSV for Import

The script generates `client_import.csv` ready for Sailrace import.

### 4. Import into Sailrace

Import the generated CSV file into Sailrace.

### 5. Sync Back to SailWave

```bash
# Export from Sailrace and sync changes
python -m src.synclist
```

## Configuration

### Environment Variables

Configuration is managed through the `.env` file:

```env
HUBSPOT_API_KEY=your_key_here
LOG_LEVEL=INFO
```

### Log Files

Logs are stored in the `logs/` directory:
- `logs/makelist.log` - Processing logs
- `logs/synclist.log` - Sync operation logs

## Common Tasks

### View Recent Logs

```bash
# Windows
Get-Content logs/makelist.log -Tail 20

# Unix/macOS
tail -20 logs/makelist.log
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_example.py
```

### Code Quality Checks

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

### FileNotFoundError

**Issue:** Cannot find input Excel file

**Solution:** Ensure Excel files are in the project root directory with correct names

### API Rate Limits

**Issue:** HubSpot API returns 429 (Too Many Requests)

**Solution:** The application implements automatic retry logic with exponential backoff. Check `logs/` for detailed error information.

### CSV Import Errors

**Issue:** Sailrace rejects the generated CSV

**Solution:**
1. Check the CSV file format in `client_import.csv`
2. Review logs in `logs/makelist.log`
3. Verify data compatibility

## Advanced Usage

### Custom CSV Export

Modify the export format by editing the relevant function in `src/makelist.py`.

### Batch Processing

For processing multiple files:

```bash
# Process all Excel files in a directory
for file in *.xlsx; do
    python -m src.makelist "$file"
done
```

## Support

For issues or questions:
1. Check the logs in `logs/` directory
2. Review [API Reference](./api.md)
3. File an issue on GitHub
