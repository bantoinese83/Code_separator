# utils.py

import os


def list_python_files(directory):
    """
    Lists all Python files in a directory.
    """
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files
