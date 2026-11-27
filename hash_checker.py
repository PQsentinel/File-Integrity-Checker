
import hashlib
import os
import json
import sys


# WEEK 1: Calculate the SHA-256 hash of one file
def hash_file(path):
    sha256_hash = hashlib.sha256()

    try:
        with open(path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    except OSError:
        print(f"Could not read the file: {path}")
        return None


# WEEK 1: Scan and display files in a folder
def scan_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)

            if file_hash is not None:
                print(f"{filename}: {file_hash}")


# WEEK 2: Build a snapshot of files and their hashes
def build_snapshot(folder_path):
    snapshot = {}

    if not os.path.isdir(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return None

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            relative_path = os.path.relpath(
                file_path, folder_path
            )

            file_hash = hash_file(file_path)

            if file_hash is not None:
                snapshot[relative_path] = file_hash

    return snapshot


# WEEK 2: Save the baseline to a JSON file
def save_baseline(snapshot, baseline_path):
    if snapshot is None:
        print("Cannot save baseline: folder scan failed.")
        return

    try:
        with open(baseline_path, "w") as file:
            json.dump(snapshot, file, indent=4)

        print("Baseline saved successfully!")

    except OSError:
        print("Could not save the baseline.")


# WEEK 2: Load the saved baseline
def load_baseline(baseline_path):
    try:
        with open(baseline_path, "r") as file:
            baseline = json.load(file)

        if not isinstance(baseline, dict):
            print("Invalid baseline format.")
            return None

        if not all(
            isinstance(path, str) and isinstance(file_hash, str)
            for path, file_hash in baseline.items()
        ):
            print("Invalid baseline entries.")
            return None

        return baseline

    except (OSError, json.JSONDecodeError):
        print("Could not load the baseline.")
        return None


# WEEK 2: Compare the baseline with the current snapshot
def compare_snapshots(baseline, current):
    baseline_files = set(baseline.keys())
    current_files = set(current.keys())

    added = sorted(current_files - baseline_files)
    deleted = sorted(baseline_files - current_files)

    common_files = baseline_files & current_files

    modified = sorted(
        path for path in common_files
        if baseline[path] != current[path]
    )

    return {
        "added": added,
        "modified": modified,
        "deleted": deleted
    }


# WEEK 2: Display the file integrity report
def check_changes(baseline, current):
    changes = compare_snapshots(baseline, current)

    added = changes["added"]
    modified = changes["modified"]
    deleted = changes["deleted"]

    print("\n===== FILE INTEGRITY REPORT =====")

    print("\nADDED FILES:")
    if added:
        for path in added:
            print(f"+ {path}")
    else:
        print("None")

    print("\nMODIFIED FILES:")
    if modified:
        for path in modified:
            print(f"* {path}")
    else:
        print("None")

    print("\nDELETED FILES:")
    if deleted:
        for path in deleted:
            print(f"- {path}")
    else:
        print("None")

    if not added and not modified and not deleted:
        print("\nNo changes detected.")

    print("\n=================================")


# COMMAND HANDLER
if __name__ == "__main__":

    folder_path = "test_folder"
    baseline_path = "baseline.json"

    if len(sys.argv) != 2:
        print("Usage: python3 hash_checker.py [scan|baseline|check]")

    elif sys.argv[1] == "scan":
        scan_folder(folder_path)

    elif sys.argv[1] == "baseline":
        snapshot = build_snapshot(folder_path)
        save_baseline(snapshot, baseline_path)

    elif sys.argv[1] == "check":
        baseline = load_baseline(baseline_path)

        if baseline is not None:
            current = build_snapshot(folder_path)

            if current is not None:
                check_changes(baseline, current)

    else:
        print("Unknown command.")
        print("Available commands: scan, baseline, check")
