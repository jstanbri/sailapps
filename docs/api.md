# API Reference

This page documents the public API for sailaps modules.

## Module: makelist

Main module for processing sailing data and generating import files.

### Functions

#### `process_data(input_file: str) -> pd.DataFrame`

Process input data and prepare for export.

**Parameters:**
- `input_file` (str): Path to input Excel file

**Returns:**
- `pd.DataFrame`: Processed data ready for export

**Raises:**
- `FileNotFoundError`: If input file doesn't exist
- `ValueError`: If data format is invalid

**Example:**
```python
from src.makelist import process_data

data = process_data('input.xlsx')
```

#### `export_csv(data: pd.DataFrame, output_file: str) -> None`

Export processed data to CSV format.

**Parameters:**
- `data` (pd.DataFrame): Data to export
- `output_file` (str): Path for output CSV file

**Returns:**
- `None`

**Example:**
```python
from src.makelist import process_data, export_csv

data = process_data('input.xlsx')
export_csv(data, 'output.csv')
```

## Module: synclist

Synchronization utilities for data syncing between systems.

### Functions

#### `sync_records(source_data: dict) -> dict`

Sync records from source to destination.

**Parameters:**
- `source_data` (dict): Source data structure

**Returns:**
- `dict`: Synchronization results

**Raises:**
- `ConnectionError`: If sync service unavailable
- `ValueError`: If data validation fails

**Example:**
```python
from src.synclist import sync_records

results = sync_records(source_data)
```

## Logging

### Logger Configuration

All modules use Python's standard logging:

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Operation completed")
```

### Log Levels

- `DEBUG`: Detailed diagnostic information
- `INFO`: General informational messages (default)
- `WARNING`: Warning messages for recoverable issues
- `ERROR`: Error messages for failures
- `CRITICAL`: Critical errors requiring immediate attention

## Error Handling

### Custom Exceptions

Exception classes provide specific error information:

```python
from src.exceptions import DataValidationError

try:
    process_data(invalid_file)
except DataValidationError as e:
    logger.error(f"Data validation failed: {e}")
```

## Type Hints

All public functions use type hints for better IDE support:

```python
from typing import Optional
import pandas as pd

def process_with_options(
    data: pd.DataFrame,
    option: Optional[str] = None
) -> pd.DataFrame:
    """Process data with optional parameters."""
    pass
```

## Performance Considerations

### Memory Usage

Large Excel files are processed in chunks to minimize memory usage.

### Processing Time

Processing time depends on data size:
- Small files (<10K rows): < 1 second
- Medium files (10K-100K rows): 1-10 seconds
- Large files (>100K rows): 10+ seconds

## Version Compatibility

- **Python**: 3.12+
- **pandas**: 2.0+
- **requests**: 2.28+

## See Also

- [Installation Guide](./installation.md)
- [Usage Guide](./usage.md)
- [Contributing](./contributing.md)
