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
        insert_positions = calculate_insert_positions(script_content, positions)

        # Insert hash separators in reverse order to preserve line numbers
        for pos in reversed(insert_positions):
            script_content.insert(pos, "# " + "#" * 78 + "\n")

        with open(file_path, "w") as f:
            f.writelines(script_content)

        spinner.succeed("Inserted hash separators")

    except Exception as e:
        spinner.fail("Failed to insert hash separators")
        logging.error(f"Error occurred: {e}")
        traceback.print_exc()


def find_class_function_positions(script_content):
    positions = []
    pattern = re.compile(r"^(class|def)\s+\w+\s*\(?[^:]*:$")

    for index, line in enumerate(script_content):
        if pattern.match(line.strip()):
            positions.append(index)

    return positions


def calculate_insert_positions(script_content, positions):
    insert_positions = []
    for pos in positions:
        indent_level = len(script_content[pos]) - len(script_content[pos].lstrip())
        for i in range(pos + 1, len(script_content)):
            line = script_content[i]
            current_indent = len(line) - len(line.lstrip())
            # Check for lines with lesser indent (end of block) or end of file
            if current_indent <= indent_level or i == len(script_content) - 1:
                insert_positions.append(i)
                break

    return insert_positions


# Example usage:
if __name__ == "__main__":
    insert_hash_separator("../test.py")
