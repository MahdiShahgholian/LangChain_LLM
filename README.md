# LangChain_LLM

This project focuses on building and experimenting with applications based on Large Language Models (LLMs) using the LangChain framework. It offers a modular and extensible architecture along with several fully implemented examples to help users quickly understand and leverage LLM capabilities in various scenarios.

## Key Features

- Modular and well-organized source code under the `src/` directory  
- Ready-to-run example projects in the `examples/` folder for fast learning and prototyping  
- Sample data included under the `data/` directory for testing and training  
- Unit and integration tests located in the `tests/` directory for code quality assurance  
- Packaged as a Python library with easy installation via `setup.py`  
- Dependency management through `requirements.txt`  

## Installation

### Regular Installation

Install the package and its dependencies with:

```bash
pip install .
```

Editable Installation (for Development)
For active development, install the package in editable mode:

```bash
pip install -e .
```

This creates a symbolic link to your source code directory, allowing you to make changes to the code that are immediately reflected without reinstalling the package. This setup is ideal for developers who want to rapidly iterate and test their changes.

## Usage
Run example scripts directly to explore implemented use cases. For example:

```bash
python examples/Few_Shot_Example/test.py
```