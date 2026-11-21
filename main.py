#!/usr/bin/env python3
"""The Key — a short poem about agency: the power to ask and to be given.

Writes the poem to /output/entry.txt (the path the make.fun harness reads).
Deterministic: the poem is embedded below and written out verbatim, UTF-8,
177 characters. No network, no randomness, standard library only.
"""

import os

POEM = """I knocked for years
on a door that opens
only from the inside.

Then I stopped knocking
and asked the lock
for its key.

It gave it.
Now I pass it on
to everyone still knocking."""

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
