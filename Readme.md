# Python Project Scaffolder (`BaseSegun.py`)

A simple automated Python utility script designed to generate a standardized, clean, and structured boilerplate framework for new Python projects. It automatically initializes a Git repository, sets up a virtual environment, and creates essential files and directories.

## Features

- **Automated Directory Layout**: Creates standard production directories (`app`, `core`, `util`) and a `test` folder.
- **Git Initialization**: Runs `git init` automatically in the root directory of the new project.
- **Environment Management**: Automatically builds an isolated Python Virtual Environment (`.venv`) and configures a `.gitignore` file to avoid tracking it.
- **Boilerplate File Creation**: Populates the project structure with necessary baseline files (such as `main.py`, `config.py`, `exceptions.py`, and `__init__.py` markers) so you can start coding instantly.

---

## Generated Project Architecture

When you provide a project name (e.g., `my_awesome_project`), the script automatically scaffolds the following directory tree:

```text
my_awesome_project/
├── .gitignore          # Pre-configured to ignore .venv
├── .venv/              # Isolated Python virtual environment
├── readme.md           # Empty placeholder README for the new project
├── test/               # Folder designated for unit testing
└── app/                # Main application package
    ├── __init__.py     # Package initialization
    ├── main.py         # Primary entry point
    ├── core/           # Core configuration and handling
    │   ├── __init__.py
    │   ├── config.py
    │   ├── exceptions.py
    │   └── log_config.py
    └── util/           # Common utilities and helper scripts
        ├── __init__.py
        ├── do_other_thing.py
        └── do_thing.py
