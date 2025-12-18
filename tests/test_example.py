"""Tests for sailaps JSON to CSV conversion functionality."""

import json
import pytest
from pathlib import Path
import csv
import sys

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from app import json_to_csv


class TestJsonToCsvConversion:
    """Test suite for JSON to CSV conversion."""

    def test_json_to_csv_basic(self, temp_data_dir):
        """Test basic JSON to CSV conversion."""
        # Arrange: Create test JSON data
        test_data = {
            "competitors": {
                "1": {
                    "compsailno": "7891",
                    "compclass": "Pico",
                    "compdivision": "Small",
                    "comphelmname": "Test Sailor",
                    "comprating": "",
                    "compnat": "IRL",
                    "compmedical": "",
                    "compmedicalflag": "0",
                    "comphelmagegroup": "18",
                    "comphelmemail": "test@example.com",
                    "comphelmsex": "Male",
                    "comphelmphoto": ""
                }
            }
        }
        
        json_file = temp_data_dir / "test.json"
        csv_file = temp_data_dir / "output.csv"
        
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        # Act
        json_to_csv(str(json_file), str(csv_file))
        
        # Assert
        assert csv_file.exists(), "CSV file should be created"
        
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 1, "Should have exactly 1 data row"
        assert rows[0]['SailNo'] == "7891", "SailNo should match"
        assert rows[0]['Helm'] == "Test Sailor", "Helm name should match"

    def test_json_to_csv_filters_empty_competitors(self, temp_data_dir):
        """Test that empty competitor placeholders are filtered out."""
        # Arrange: Create test JSON with both empty and valid competitors
        test_data = {
            "competitors": {
                "1": {
                    "comptotal": "26",
                    "compmedicalflag": "0"
                    # Missing compsailno - should be filtered
                },
                "2": {
                    "compsailno": "4645",
                    "compclass": "SOLO",
                    "compdivision": "Medium",
                    "comphelmname": "Real Sailor",
                    "comprating": "1139",
                    "compnat": "GBR",
                    "compmedical": "",
                    "compmedicalflag": "0",
                    "comphelmagegroup": "Senior",
                    "comphelmemail": "real@example.com",
                    "comphelmsex": "Male",
                    "comphelmphoto": ""
                }
            }
        }
        
        json_file = temp_data_dir / "test.json"
        csv_file = temp_data_dir / "output.csv"
        
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        # Act
        json_to_csv(str(json_file), str(csv_file))
        
        # Assert
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 1, "Should filter out empty competitor (only 1 valid row)"
        assert rows[0]['SailNo'] == "4645", "Valid competitor should be included"

    def test_json_to_csv_headers(self, temp_data_dir):
        """Test that CSV headers are correct."""
        # Arrange
        test_data = {
            "competitors": {
                "1": {
                    "compsailno": "1",
                    "compclass": "Test",
                    "compdivision": "Div",
                    "comphelmname": "Name",
                    "comprating": "100",
                    "compnat": "GBR",
                    "compmedical": "",
                    "compmedicalflag": "0",
                    "comphelmagegroup": "Adult",
                    "comphelmemail": "test@test.com",
                    "comphelmsex": "Male",
                    "comphelmphoto": ""
                }
            }
        }
        
        json_file = temp_data_dir / "test.json"
        csv_file = temp_data_dir / "output.csv"
        
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        # Act
        json_to_csv(str(json_file), str(csv_file))
        
        # Assert
        expected_headers = [
            'SailNo', 'Class', 'Fleet', 'Helm', 'PY', 'Nationality',
            'Medical', 'Medical Flag', 'Age Group', 'Email', 'Sex', 'Photo Path'
        ]
        
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
        
        assert headers == expected_headers, "CSV headers should match expected columns"

    def test_json_to_csv_file_not_found(self, temp_data_dir):
        """Test error handling when JSON file doesn't exist."""
        # Act & Assert
        with pytest.raises(FileNotFoundError):
            json_to_csv(str(temp_data_dir / "nonexistent.json"), "output.csv")

    def test_json_to_csv_empty_competitors(self, temp_data_dir):
        """Test handling of JSON with no valid competitors."""
        # Arrange
        test_data = {"competitors": {}}
        
        json_file = temp_data_dir / "test.json"
        csv_file = temp_data_dir / "output.csv"
        
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        # Act
        json_to_csv(str(json_file), str(csv_file))
        
        # Assert
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 0, "Should have no data rows when competitors dict is empty"
