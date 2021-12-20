import sys

import morsecode


def encode() -> None:
    """CLI utility to convert text to morse code."""
    data = sys.argv[1:]
    if not data:
        print("Usage: morsecode Hello World!")
        sys.exit(1)

    text = " ".join(data)
    print(morsecode.encode(text))


def decode() -> None:
    """CLI utility to convert morse code to text."""
    data = sys.argv[1:]
    if not data:
        print("Usage: morsedecode --- .... / .... .. -.-.--")
        sys.exit(1)

    text = " ".join(data)
    print(morsecode.decode(text))
