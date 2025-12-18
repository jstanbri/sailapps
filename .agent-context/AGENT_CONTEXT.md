# How to Brief Agents on soundbox-makelist

## Quick Start

When working with me on this project:

1. **Reference the `.agent-context/` files** - I'll know to read them for context
2. **Be specific about tasks** - "Update makelist.py to handle X" is clearer than "improve the code"
3. **Include file paths** - Always reference the files involved
4. **Mention constraints** - HubSpot API limits, batch sizes, etc. matter

## Common Patterns for Requests

### For Feature Additions

> "Add a feature to `makelist.py` that exports segment members to a CSV file. Save it as `segment_export.csv`."

### For Bug Fixes

> "There's an issue in `synclist.py` at line X where [describe problem]. Fix it while maintaining the existing log format."

### For Code Refactoring

> "Refactor `makelist.py` to extract the segment creation logic into a separate function named `create_or_get_segment()`. Keep the same public interface."

### For HubSpot Integration Questions

> "What additional contact properties should we fetch from HubSpot? See `.agent-context/HUBSPOT_INTEGRATION.md` for current usage."

## Code Standards

### Naming Conventions

- **Functions**: `snake_case` (e.g., `find_hubspot_contacts()`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `HUBSPOT_API_KEY`)
- **Classes**: `PascalCase` (if used)
- **Variables**: `snake_case`

### File Structure

```python
"""Module docstring at top"""
import statements
dotenv.load_dotenv()
# Logging setup
# Configuration constants
# Main functions
# Entry point (if __name__ == "__main__")
```

### Error Handling

- Log errors with context before raising/returning
- Include the specific data that caused the error in logs
- Handle HubSpot API rate limits with retry logic
- Always clean up resources (close files, etc.)

### Logging

- Use the configured `logger` object (not `print()`)
- Log levels: `INFO` for major operations, `WARNING` for recoverable issues, `ERROR` for failures
- Include context in log messages (e.g., how many contacts processed)

## Key Constraints

1. **File Dependencies**
   - `.env` file required but not in repo (credentials)
   - Excel files expected in project root (configurable path)
   - CSV files: `client_export.csv` (input), `client_import.csv` (output)

1. **Logging**
   - All operations logged to `logs/{script}.log`
   - Logs always include timestamp and operation status
   - Do NOT log sensitive data (API keys, full contact details)

## Files NOT to Modify Without Discussion

- `.env` - Contains credentials (this is local-only, never in repo)

## Testing

- Test scripts exist in `test/` directory
- Run tests before committing changes
- When adding features, add corresponding tests