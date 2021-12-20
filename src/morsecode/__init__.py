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
    string = string.upper()
    return " ".join(MORSE_MAPPING[char] for char in string if char in MORSE_MAPPING)


def decode(string: str) -> str:
    """Convert morse code to string."""
    return "".join(REVERSE_MAPPING.get(code, "") for code in string.split())
