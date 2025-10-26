"""
utils.py
--------
Helper functions for saving CSV files, validating rows, and loading configuration.
"""

import csv
import json

def validate_rows(header: list, rows: list):
    """
    Validate that all rows have the same length as the header.

    Parameters
    ----------
    header : list
        List of column names.
    rows : list
        List of rows (each row is a list of values).

    Raises
    ------
    ValueError
        If any row has a different length than the header.
    """
    expected_len = len(header)
    for i, row in enumerate(rows):
        if len(row) != expected_len:
            raise ValueError(
                f"Row {i} has length {len(row)}, expected {expected_len}."
            )


def save_csv(filename: str, header: list, rows: list):
    """
    Save data to a CSV file with validation.

    Parameters
    ----------
    filename : str
        Path to the CSV file.
    header : list
        List of column names.
    rows : list
        List of rows (each row is a list of values).
    """
    validate_rows(header, rows)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def load_config(path: str = "../config.json") -> dict:
    """
    Load configuration from a JSON file.

    Parameters
    ----------
    path : str, optional
        Path to the JSON configuration file (default '../config.json').

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
