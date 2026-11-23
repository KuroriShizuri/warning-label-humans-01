#!/usr/bin/env python3
"""Write one competition line to a file.

This little script exists for a single job: take the entry line stored
below, make sure it is a well-formed one-liner, and save it exactly as
it is -- no trailing newline, no extra whitespace, nothing added.

Usage:
    python3 main.py                  # writes to /output/entry.txt
    python3 main.py --out result.txt # writes wherever you point it
    python3 main.py --self-test      # checks the line, writes nothing
"""

import argparse
import sys
from pathlib import Path

# The entry itself. One line, plain text, no newline at the end.
ENTRY_LINE = "WARNING: Do not tap the glass. Human is easily startled, overthinks everything, and cries at dog food commercials."

# Where the line goes when no --out flag is given.
DEFAULT_DESTINATION = Path("/output/entry.txt")

# A one-line entry has to fit in a single short line.
MAX_LENGTH = 160


def check_entry(line):
    """Complain (by raising ValueError) if `line` is not a valid entry."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line (no line breaks allowed)")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        raise ValueError("entry must be valid UTF-8 text")
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "entry must be between 1 and %d characters long, got %d"
            % (MAX_LENGTH, len(line))
        )


def save_entry(line, destination):
    """Write `line` to `destination` as raw bytes, without a newline."""
    check_entry(line)
    target = Path(destination)
    if target.parent != Path("."):
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(line.encode("utf-8"))


def build_parser():
    """Command-line flags for this script."""
    parser = argparse.ArgumentParser(
        description="Validate and write the one-line competition entry."
    )
    parser.add_argument(
        "--out",
        default=str(DEFAULT_DESTINATION),
        help="file to write the entry to (default: %(default)s)",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="only validate the entry in memory, write no file",
    )
    return parser


def main(argv=None):
    """Parse flags, validate, and either report or write the entry."""
    args = build_parser().parse_args(argv)
    try:
        check_entry(ENTRY_LINE)
    except ValueError as problem:
        print("error: %s" % problem, file=sys.stderr)
        return 1
    if args.self_test:
        print("self-test passed: entry is a valid %d-character line" % len(ENTRY_LINE))
        return 0
    try:
        save_entry(ENTRY_LINE, args.out)
    except OSError as problem:
        print("error: cannot write %s: %s" % (args.out, problem), file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(ENTRY_LINE), args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
