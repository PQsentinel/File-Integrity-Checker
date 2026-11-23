# File Integrity Checker

A Python-based tool that calculates SHA-256 hashes of files to monitor file integrity and detect changes.

## Features

- Calculates SHA-256 hashes.
- Scans multiple files in a directory.
- Reads files in 4096-byte chunks.
- Detects file modifications through hash comparison.
- Handles missing or unreadable files.

## Requirements

- Python 3
- Standard Python libraries: hashlib and os

## Usage

1. Clone or download this repository.
2. Create a folder named `test_folder`.
3. Add files you want to monitor.
4. Run:

   python3 hash_checker.py

## How It Works

The tool reads each file in binary mode and calculates its SHA-256 hash. Changes to a file's content produce a different hash.

## Ethical and Legal Notice

Only use this tool to monitor files and directories that you own or have explicit permission to access. Do not use it to inspect or monitor systems without authorization.

## Author

PQ
