# test_insert_hash_separator.py

import pytest

from code_separator import insert_hash_separator


@pytest.fixture
def temp_script(tmpdir):
    script_content = """
    class MyClass1:
        def __init__(self):
            self.name = "MyClass1"

        def greet(self):
            print(f"Hello from {self.name}!")


    def square(x):
        return x ** 2
    """
    script_path = tmpdir.join("test_script.py")
    with open(script_path, "w") as f:
        f.write(script_content)
    return script_path


def test_insert_hash_separator(temp_script):
    insert_hash_separator(temp_script)

    with open(temp_script, "r") as f:
        modified_content = f.read()

    assert modified_content.count("# " + "#" * 78 + "\n") == 4  # Adjust based on your script structure


def test_insert_hash_separator_empty_file(tmpdir):
    empty_script_path = tmpdir.join("empty_script.py")
    open(empty_script_path, "w").close()  # Create an empty script file

    insert_hash_separator(empty_script_path)

    with open(empty_script_path, "r") as f:
        modified_content = f.read()

    assert modified_content == ""

def test_insert_hash_separator_no_functions_or_classes(tmpdir):
    script_content = """
    x = 10
    y = 20
    z = x + y
    """
    script_path = tmpdir.join("no_functions_or_classes.py")
    with open(script_path, "w") as f:
        f.write(script_content)

    insert_hash_separator(script_path)

    with open(script_path, "r") as f:
        modified_content = f.read()

    assert modified_content == script_content
