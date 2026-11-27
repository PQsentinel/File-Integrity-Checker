
# File Integrity Checker

A Python-based security tool that uses SHA-256 hashing to monitor file integrity, create file baselines, and detect unauthorized or unexpected file changes.

This project was developed as part of my SkillMe Cybersecurity Virtual Internship.

## Features

### Week 1: SHA-256 File Hashing
- Calculates SHA-256 hashes of files.
- Reads files in 4096-byte chunks.
- Scans files in a directory.
- Handles missing or unreadable files.

### Week 2: File Integrity Monitoring
- Creates a baseline of file hashes.
- Saves and loads baselines using JSON.
- Recursively scans directories and subdirectories.
- Detects added files.
- Detects modified files.
- Detects deleted files.
- Reports when no changes are detected.
- Includes automated tests using pytest.

## Project Structure

```text
File-Integrity-Checker/
├── hash_checker.py
├── baseline.json
├── test_folder/
│   ├── file1.txt
│   ├── file3.txt
│   ├── file4.txt
│   ├── file5.txt
│   └── documents/
│       ├── report.txt
│       └── notes.txt
├── tests/
│   └── test_hash_checker.py
└── README.md
```

## Requirements

- Python 3
- pytest (for automated testing)

The application uses Python standard libraries:
- hashlib
- os
- json
- sys

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/PQsentinel/File-Integrity-Checker.git
cd File-Integrity-Checker
```

### 2. Scan files

```bash
python3 hash_checker.py scan
```

### 3. Create a baseline

```bash
python3 hash_checker.py baseline
```

This creates or updates `baseline.json`, storing the SHA-256 hashes of files in the monitored directory.

### 4. Check for changes

```bash
python3 hash_checker.py check
```

The tool compares the current directory snapshot against the saved baseline and reports:

- Added files
- Modified files
- Deleted files

If no changes are detected, it reports that the directory remains unchanged.

## Running Automated Tests

Install pytest if it is not already installed:

```bash
sudo apt install python3-pytest
```

Run the tests:

```bash
python3 -m pytest -v
```

The test suite verifies:

1. Correct SHA-256 hash calculation.
2. Recursive scanning of subdirectories.
3. Added file detection.
4. Deleted file detection.
5. Modified file detection.
6. Unchanged file detection.
7. Baseline saving and loading.

## How It Works

The tool reads files in binary mode and calculates their SHA-256 hashes.

During baseline creation, file paths and their hashes are stored in a JSON file.

During integrity checks, the current snapshot is compared against the saved baseline using Python dictionaries and sets.

A difference in file paths or hashes helps identify added, deleted, or modified files.

## Ethical and Legal Notice

Only use this tool to monitor files and directories that you own or have explicit permission to access.

Do not use it to inspect or monitor systems without authorization.

## Author

PQ

GitHub: https://github.com/PQsentinel
