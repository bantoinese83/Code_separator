import logging
import re
import traceback

from halo import Halo


logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def insert_hash_separator(file_path):
    spinner = Halo(text="Inserting hash separators", spinner="dots")
    spinner.start()

    try:
        with open(file_path, "r") as f:
            script_content = f.readlines()

        positions = find_class_function_positions(script_content)

        # Insert hash separators in reverse order to preserve line numbers
        for pos in reversed(positions):
            insert_position = find_insert_position(script_content, pos)
            script_content.insert(insert_position, "# " + "#" * 78 + "\n")

        with open(file_path, "w") as f:
            f.writelines(script_content)

        spinner.succeed("Inserted hash separators")

    except Exception as e:
        spinner.fail("Failed to insert hash separators")
        logging.error(f"Error occurred: {e}")
        traceback.print_exc()


def find_class_function_positions(script_content):
    positions = []
    stack = []
    pattern = re.compile(r"^(class|def)\s+\w+\s*\(?[^:]*:$")

    for index, line in enumerate(script_content):
        indent_level = len(line) - len(line.lstrip())

        # Handle nested classes and functions
        while stack and indent_level <= stack[-1][1]:
            stack.pop()

        if pattern.match(line.strip()):
            positions.append(index)
            stack.append((index, indent_level))

    return positions


def find_insert_position(script_content, pos):
    for i in range(pos - 1, -1, -1):
        line = script_content[i].strip()
        if line and not line.startswith("#"):
            return i + 1
    return pos


# Example usage:
if __name__ == "__main__":
    insert_hash_separator("../test.py")
