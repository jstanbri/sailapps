"""Shared pytest fixtures and configuration."""

import pytest
from pathlib import Path


@pytest.fixture
def temp_data_dir(tmp_path):
    """Provide a temporary directory for test data files."""
    return tmp_path


@pytest.fixture
def mock_env(monkeypatch):
    """Provide environment variable mocking."""
    return monkeypatch


@pytest.fixture
def project_root():
    """Provide the project root directory path."""
    return Path(__file__).parent.parent
