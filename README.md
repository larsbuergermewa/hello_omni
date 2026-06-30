# hello_omni

A minimal, [uv](https://github.com/astral-sh/uv)-managed Python hello-world project.

## Requirements

- Python 3.14 or newer
- uv

## Setup

```sh
uv sync
```

## Project structure

- `main.py` contains `greet()`, which returns the `Hello, <name>!` message, and `main()`, which prints the default greeting.
- `tests/test_main.py` verifies the greeting behavior and script output.

## Run

```sh
uv run main.py
```

This prints:

```
Hello, Omni!
```

## Running tests

```sh
uv run pytest
```
