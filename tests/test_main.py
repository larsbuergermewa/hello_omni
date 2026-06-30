import subprocess

import pytest

from main import greet


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        (None, "Hello, Omni!"),
        ("World", "Hello, World!"),
        ("", "Hello, !"),
    ],
)
def test_greet(name, expected):
    if name is None:
        assert greet() == expected
    else:
        assert greet(name) == expected


def test_script_output():
    result = subprocess.run(
        ["uv", "run", "main.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "Hello, Omni!\n"
