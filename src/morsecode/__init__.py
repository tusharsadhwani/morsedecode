"""Sample package."""

MORSE_MAPPING = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    ":": "---...",
    ";": "_._._.",
    "'": ".----.",
    '"': ".-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "/": "-..-.",
    "-": "-....-",
    "=": "-...-",
    "+": ".-.-.",
    "!": "-.-.--",
    "&": ".-...",
    "_": "..--.-",
    "$": "...-..-",
    "¿": "..-.-",
    "¡": "--...-",
    "@": ".--.-.",
    " ": "/",
}

REVERSE_MAPPING = {value: key for key, value in MORSE_MAPPING.items()}


def encode(string: str) -> str:
    """Convert a string to morse code."""
    try:
        return " ".join(MORSE_MAPPING[char] for char in string)
    except KeyError:
        raise ValueError("Unknown characters found in string.")


def decode(string: str) -> str:
    """Convert morse code to string."""
    try:
        return "".join(REVERSE_MAPPING[code] for code in string.split())
    except KeyError:
        raise ValueError("Unknown morse code found in string.")
