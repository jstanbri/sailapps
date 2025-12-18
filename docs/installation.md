# Installation Guide

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jstanbri/sailapps.git
cd sailapps
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\Activate.ps1

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the project root with required credentials:

```env
HUBSPOT_API_KEY=your_api_key_here
```

**Important:** Never commit the `.env` file to version control.

### 5. Verify Installation

```bash
# Run tests to verify setup
pytest

# Check that all dependencies are installed
pip list
```

## Development Installation

For development work, install additional dependencies:

```bash
pip install -r requirements.txt
pip install pytest pytest-cov pylint black isort
```

## Troubleshooting

### Virtual Environment Not Activating

**Issue:** PowerShell execution policy prevents activation script

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Missing Dependencies

**Issue:** ModuleNotFoundError after installation

**Solution:**
```bash
# Verify virtual environment is activated
which python  # Unix/macOS
where python  # Windows

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

### Permission Denied on Scripts

**Issue:** Scripts in `.venv/bin/` not executable

**Solution:**
```bash
chmod +x .venv/bin/activate
```

## Next Steps

- Read [Usage Guide](./usage.md) for basic operations
- Review [API Reference](./api.md) for detailed function documentation
- Check out [Contributing Guidelines](./contributing.md) to contribute
