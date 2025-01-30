import doctest
from pathlib import Path

import pytest

FILES = [f for f in Path("./docs/").rglob("*.md")]


@pytest.mark.parametrize(
    "file",
    FILES,
    ids=[f.name for f in FILES],
)  # type: ignore
def test_docs(file: Path) -> None:
    test_results = doctest.testfile(
        filename=f"{file}",
        module_relative=False,
    )

    assert test_results.failed == 0
