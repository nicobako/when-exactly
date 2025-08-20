import doctest
from pathlib import Path

import pytest

import when_exactly as we

FILES = [f for f in Path("./docs/").rglob("*.md")] + [
    f for f in Path("./src/when_exactly/").rglob("*.py") if f.name != "__init__.py"
]


@pytest.mark.parametrize(
    "file",
    FILES,
    ids=[f.name for f in FILES],
)  # type: ignore
def test_docs(file: Path) -> None:
    file_str = str(file)

    def run_test_file(verbose: bool = True) -> doctest.TestResults:
        return doctest.testfile(
            filename=file_str,
            module_relative=False,
            globs={"we": we},
            verbose=verbose,
        )

    test_results = run_test_file(verbose=False)
    if test_results.failed != 0:
        # Rerun with verbose output if there were failures
        test_results = run_test_file(verbose=True)

    assert test_results.failed == 0


def test_docstrings() -> None:
    doctest.testmod(
        we,
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.FAIL_FAST,
        globs={"we": we},
        verbose=True,
    )
