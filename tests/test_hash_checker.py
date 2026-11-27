
import hashlib
import os

from hash_checker import (
    build_snapshot,
    compare_snapshots,
    save_baseline,
    load_baseline
)


# TEST 1: Check whether a file is correctly hashed
def test_build_snapshot(tmp_path):
    content = "Hello, cybersecurity!"
    file_path = tmp_path / "hello.txt"

    file_path.write_text(content)

    snapshot = build_snapshot(tmp_path)

    expected_hash = hashlib.sha256(
        content.encode()
    ).hexdigest()

    assert snapshot["hello.txt"] == expected_hash


# TEST 2: Check whether files in subdirectories are detected
def test_build_snapshot_includes_subdirectories(tmp_path):
    subfolder = tmp_path / "documents"
    subfolder.mkdir()

    file_path = subfolder / "report.txt"
    file_path.write_text("Security report")

    snapshot = build_snapshot(tmp_path)

    assert "documents/report.txt" in snapshot


# TEST 3: Detect added files
def test_detect_added_file():
    baseline = {
        "file1.txt": "hash1"
    }

    current = {
        "file1.txt": "hash1",
        "new_file.txt": "hash2"
    }

    changes = compare_snapshots(baseline, current)

    assert changes["added"] == ["new_file.txt"]
    assert changes["modified"] == []
    assert changes["deleted"] == []


# TEST 4: Detect deleted files
def test_detect_deleted_file():
    baseline = {
        "file1.txt": "hash1",
        "file2.txt": "hash2"
    }

    current = {
        "file1.txt": "hash1"
    }

    changes = compare_snapshots(baseline, current)

    assert changes["deleted"] == ["file2.txt"]
    assert changes["added"] == []
    assert changes["modified"] == []


# TEST 5: Detect modified files
def test_detect_modified_file():
    baseline = {
        "file1.txt": "old_hash"
    }

    current = {
        "file1.txt": "new_hash"
    }

    changes = compare_snapshots(baseline, current)

    assert changes["modified"] == ["file1.txt"]
    assert changes["added"] == []
    assert changes["deleted"] == []


# TEST 6: Confirm no changes are detected
def test_no_changes_detected():
    baseline = {
        "file1.txt": "hash1",
        "file2.txt": "hash2"
    }

    current = {
        "file1.txt": "hash1",
        "file2.txt": "hash2"
    }

    changes = compare_snapshots(baseline, current)

    assert changes["added"] == []
    assert changes["modified"] == []
    assert changes["deleted"] == []


# TEST 7: Save and load the baseline
def test_save_and_load_baseline(tmp_path):
    baseline = {
        "file1.txt": "abc123",
        "documents/report.txt": "xyz789"
    }

    baseline_path = tmp_path / "baseline.json"

    save_baseline(baseline, baseline_path)

    loaded_baseline = load_baseline(baseline_path)

    assert loaded_baseline == baseline
