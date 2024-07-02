from setuptools import setup, find_packages

setup(
    name='auto_hash_separator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'halo',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'hash-separator = code_separator.cli:main',
        ],
    },
    author='Bryan Antoine',
    author_email='b.antoine.se@gmail.com',
    description='Python package for inserting hash separators between functions and classes.',
    long_description='''Auto_Hash_Separator is a Python package designed to automate the insertion of hash separators 
    between functions and classes within Python files. This tool enhances code readability by visually separating 
    distinct sections of code, improving maintainability and collaboration in development projects.

    Features:
    🔍 Automatically inserts hash separators in Python files.
    📁 Supports processing of single files, all Python files in a directory, or specific directories.
    🛠️ Enhances code organization and readability.
    🚀 Lightweight and easy-to-use.

    Auto_Hash_Separator is ideal for developers looking to streamline code organization and maintain clean, 
    structured Python projects. Whether you're working on a small script or a large-scale application, 
    Auto_Hash_Separator helps you maintain clarity and structure in your codebase.

    Visit our [GitHub repository](https://github.com/bantoinese83/Code_separator) for more information and to get 
    started with Auto_Hash_Separator today!
    ''',
    url='https://github.com/bantoinese83/Code_separator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
