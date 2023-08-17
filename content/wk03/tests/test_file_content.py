"A set of pytests for evaluating the wk03 assignment"

__copyright__ = "Copyright (C) 2023-present, Drexel Medicine. All rights reserved."
__author__ = "Will Dampier, PhD"

import csv
import hashlib
import os
import pytest


def read_csv(file_path):
    """Read the CSV file and yield file paths and MD5 checksums."""
    with open(file_path, "r", encoding="ascii") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            yield row[0], row[1]


def md5(filename):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as handle:
        for chunk in iter(lambda: handle.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Reading the CSV and collecting file paths and their expected md5 checksums
file_data = list(read_csv("tests/solutions.csv"))


@pytest.mark.parametrize("file_path, expected_md5", file_data)
def test_files(file_path, expected_md5):
    "Check files for existance and content"

    # Asserting that the file exists
    assert os.path.exists(file_path), f"{file_path} does not exist."

    # Calculating and checking the MD5 checksum of the file
    calculated_md5 = md5(file_path)
    assert (
        calculated_md5 == expected_md5
    ), f"MD5 mismatch for {file_path}. Expected: {expected_md5}, Got: {calculated_md5}"

    
# Copyright (C) 2023-present, Drexel Medicine. All rights reserved.
