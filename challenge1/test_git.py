import unittest
import os
from git import do_command, MESSAGES
import filecmp


def test_do_command_commit_invalid_file_path():
    filePaths = ["invalid_path1.txt", "invalid_path2.txt"]
    message = "test commit message"
    try:
        do_command("commit", filePaths, message)
    except ValueError as e:
        assert MESSAGES["missing_file_paths"].format(', '.join(filePaths))
        assert os.path.exists(filePaths[0]) == False
        assert os.path.exists(filePaths[1]) == False

def test_do_command_commit_no_message():
    filePaths = ["invalid_path1.txt", "invalid_path2.txt"]
    message = ""
    try:
        do_command("commit", filePaths, message)
    except ValueError as e:
        assert MESSAGES["commit_message_missing"]

def test_do_command_diff_invalid_file_path():
    file1 = "invalid_path1.txt"
    file2 = "./test_file2.txt"
    try:
        do_command("diff", file1, file2)
    except ValueError as e:
        assert MESSAGES["file_not_found"].format(file1)
        assert os.path.exists(file1) == False
        assert os.path.exists(file2) == True

def test_do_command_diff_files_identical():
    file1 = "test_file1.txt"
    file2 = "test_file1.txt"
    try:
        do_command("diff", file1, file2)
    except ValueError as e:
        assert MESSAGES["files_identical"].format(file1,file2)
        assert filecmp.cmp(file1, file2) == True

def test_do_command_diff_files_different():
    file1 = "test_file1.txt"
    file2 = "test_file2.txt"
    result = do_command("diff", file1, file2)
    assert result == MESSAGES["files_different"].format(file1,file2)
    assert filecmp.cmp(file1, file2) == False

if __name__ == "__main__":
    unittest.main()