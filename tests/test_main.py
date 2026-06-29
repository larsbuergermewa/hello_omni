import subprocess

from main import greet


def test_greet_default():
    assert greet() == "Hello, Omni!"


def test_greet_custom_name():
    assert greet("World") == "Hello, World!"


def test_greet_empty_name():
    assert greet("") == "Hello, !"


def test_script_output():
    result = subprocess.run(
        ["uv", "run", "main.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Hello, Omni!" in result.stdout
