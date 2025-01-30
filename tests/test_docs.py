import doctest
import pytest
from pathlib import Path

FILES = [f for f in Path("./docs/").rglob("*.md")]


@pytest.mark.parametrize(
    "file",
    FILES,
    ids=[f.name for f in FILES],
)
def test_docs(file: Path) -> None:
    test_results = doctest.testfile(
        filename=f"{file}",
        module_relative=False,
    )

    assert test_results.failed == 0
