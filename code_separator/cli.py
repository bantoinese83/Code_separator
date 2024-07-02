import argparse
import os
import glob
from code_separator.core import insert_hash_separator


def process_directory(directory):
    """
    Process all Python files in the given directory by inserting hash separators.

    Args:
    - directory (str): The directory path containing Python files.
    """
    python_files = glob.glob(os.path.join(directory, "*.py"))
    for file_path in python_files:
        insert_hash_separator(file_path)


def main():
    """
    Command-line interface for inserting hash separators between functions and classes in Python files.
    Supports processing single files, all files in the current directory, or all files in a specified directory.
    """
    parser = argparse.ArgumentParser(
        description="Insert hash separators between functions and classes in Python files."
    )
    parser.add_argument(
        "file_path", type=str,
        help="Path to the Python file or directory. Use 'all' to process all Python files in a directory."
    )

    args = parser.parse_args()

    if args.file_path.endswith(".py"):
        # Process a single Python file
        insert_hash_separator(args.file_path)
    elif args.file_path == "all":
        # Process all Python files in the current directory
        process_directory(os.getcwd())
    elif os.path.isdir(args.file_path):
        # Process all Python files in a specific directory
        process_directory(args.file_path)
    else:
        # Invalid input
        print("Invalid file path or directory. Please provide a valid Python file or directory path.")


if __name__ == "__main__":
    main()
