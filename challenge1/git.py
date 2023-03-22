import os
import filecmp

MESSAGES = {
    "file_not_found": "{} does not exist.",
    "invalid_arguments": "{} command requires {}(s) as argument(s)",
    "git_command_type_error": "{}: {}",
    "commit_message_missing": "Please enter a commit message",
    "missing_file_paths": "Error: The following file paths do not exist: {}",
    "unsupported_command": "Command '{}' is not supported by git",
    "invalid_file_path": "{} is not a valid file path",
    "files_identical": "{} and {} are identical",
    "files_different": "{} and {} are different",
    "files_committed": "Files committed: {}",
    "files_status": "Status for: {}",
    "files_log": "Log for: {}"
}

def if_file_exists(filepath):
    """Checks if a file exists at the given path, and prints an error message if it does not."""
    if not os.path.isfile(filepath):
        MESSAGES["file_not_found"].format(filepath)
        return False
    else:
        return True

def do_command(command, *args):
    """Executes a git command with the given arguments."""

    command_map = {
        "status": status,
        "commit": commit,
        "log": log,
        "diff": diff
    }
    git_command_class = command_map.get(command, None)

    if git_command_class is None:
        return MESSAGES["unsupported_command"].format(command)

    expected_types = {
        "status": list,
        "commit":(list, str),
        "log": list,
        "diff": (str, str)
    }

    try:
        expected_type = expected_types[command]
        if not all(isinstance(arg, expected_type) for arg in args):
            raise TypeError(MESSAGES["invalid_arguments"].format(command, expected_type.__ne__))

        git_command = git_command_class(*args)
        return git_command
    except TypeError as e:
        raise TypeError(MESSAGES["git_command_type_error"].format(git_command_class.__name__, e))

def status(pathSpecs):
    all_paths_exist = all(os.path.isfile(path) for path in pathSpecs)

    if not all_paths_exist:
        missing_paths = [path for path in pathSpecs if not os.path.isfile(path)]
        return MESSAGES["missing_file_paths"].format(', '.join(missing_paths))

    return MESSAGES["files_status"].format(', '.join(pathSpecs))

def commit(filePaths, message):

    all_paths_exist = all(os.path.isfile(path) for path in filePaths)

    if not all_paths_exist:
        missing_paths = [path for path in filePaths if not os.path.isfile(path)]
        return MESSAGES["missing_file_paths"].format(', '.join(missing_paths))

    if not message or message == "":
        return MESSAGES["commit_message_missing"]

    return MESSAGES["files_committed"].format(', '.join(filePaths))

def log(pathsToShowLogFor):
    all_paths_exist = all(os.path.isfile(path) for path in pathsToShowLogFor)
    if not all_paths_exist:
        missing_paths = [path for path in pathsToShowLogFor if not os.path.isfile(path)]
        return MESSAGES["missing_file_paths"].format(', '.join(missing_paths))
    return MESSAGES["files_log"].format(', '.join(pathsToShowLogFor))

def diff(file1, file2):
    if not os.path.isfile(file1) or not os.path.isfile(file2):
        if not os.path.isfile(file1):
            return MESSAGES["invalid_file_path"].format(file1)
        else:
            return MESSAGES["invalid_file_path"].format(file2)
    elif filecmp.cmp(file1, file2):
        return MESSAGES["files_identical"].format(file1,file2)
    else:
        return MESSAGES["files_different"].format(file1,file2)


result_commit = do_command("commit", ["test_file1.txt","test_file2.txt"], "test commit")
print(result_commit)

result_status = do_command("status", ["test_file1.txt","test_file2.txt"])
print(result_status)

result_diff = do_command("diff", "test_file1.txt","test_file1_copy.txt")
print(result_diff)

result_log = do_command("log", ["test_file1.txt","test_file1_copy.txt"])
print(result_log)
