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


# ##############################################################################
def insert_hash_separator(file_path):
    """
    Inserts hash separators between functions and classes in a Python file.
    """
    spinner = Halo(text="Inserting hash separators", spinner="dots")
    spinner.start()
    try:
        with open(file_path, "r") as f:
            script_content = f.read()

        pattern = r"(?:def\s+[^\(]+\()|(?:class\s+[^\(:]+:)"
        matches = list(re.finditer(pattern, script_content))
        positions = [match.start() for match in reversed(matches)]

        with open(file_path, "w") as f:
            for pos in positions:
                script_content = (
                        script_content[:pos]
                        + "\n# "
                        + "#" * 78
                        + "\n"
                        + script_content[pos:]
                )
            f.write(script_content)

        spinner.succeed("Inserted hash separators")
    except Exception as e:
        spinner.fail("Failed to insert hash separators")
        logging.error(f"Error occurred: {e}")
        traceback.print_exc()
