# UML Class Diagram Generator

![Python Version](https://img.shields.io/badge/python-3.10%2B-yellow)
[![Downloads](https://static.pepy.tech/badge/uml-class-diagram-generator)](https://pepy.tech/project/uml-class-diagram-generator)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

The **UML Class Diagram Generator** is a powerful Python-based tool designed to automatically generate UML class diagrams from Python source code. It parses your Python files, extracts class definitions, methods, and attributes, and creates a structured UML diagram in XML format. This diagram can be easily visualized using tools like [draw.io](https://app.diagrams.net/).

This tool is perfect for developers and teams who want to quickly visualize the architecture of their Python projects without manually drawing class diagrams.

## Features

- **Automatic Class Parsing**: Detects and parses class definitions, including methods and attributes.
- **Import Resolution**: Automatically resolves and includes imported files within the specified package.
- **Interactive Command-Line Interface**: Guides you through selecting the base directory and main script for UML generation.
- **UML Diagram in XML**: Outputs the UML class diagram in XML format, ready to be opened with diagram tools like draw.io.

## Installation

You can install the UML Class Diagram Generator directly from PyPI:

```bash
pip install uml-class-diagram-generator
```

## Usage

After installing, you can generate UML class diagrams using the command-line tool `generate-uml`.

### Basic Usage

1. **Navigate to your project directory**:

   ```bash
   cd /path/to/your/project
   ```

2. **Run the UML generator**:

   ```bash
   generate-uml
   ```

3. **Follow the prompts**:
   - Enter the base package directory (default is `src`).
   - Select the main script for which you want to generate the UML diagram.
   - Enter the name of the sub-package directory to resolve imports.

4. **Find your UML Diagram**:
   - The tool will generate an XML file named `<sub_package_directory>_class_diagram.xml`.
   - Open this XML file in [draw.io](https://app.diagrams.net/) to view the class diagram.

### Example

Let's say you have the following directory structure:

```
my_project/
│
├── src/
│   ├── main.py
│   └── module/
│       └── my_class.py
└── tests/
    └── test_my_class.py
```

You would run `generate-uml`, specify `src` as the base directory, select `main.py` as the main script, and provide `module` as the sub-package directory. The tool will then generate a `module_class_diagram.xml` file containing the UML diagram for the classes in `main.py` and `my_class.py`.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/siddharthverma-1607/uml-class-diagram-generator).

## Acknowledgments

- This tool leverages Python's Abstract Syntax Tree (AST) module to parse and analyze Python source code.
- Inspired by the need for efficient project architecture visualization.
