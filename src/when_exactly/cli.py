from argparse import ArgumentParser

from when_exactly.__version__ import __version__


def main() -> None:
    parser = ArgumentParser(
        prog="when-exactly",
        description="When Exactly CLI",
    )
    parser.add_argument(
        "--version",
        dest="version",
        action="store_true",
        help="Show the version of when-exactly",
    )
    args = parser.parse_args()
    if args.version:
        print(f"{parser.prog} version {__version__}")
