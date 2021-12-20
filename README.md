# morsedecode

A morse code encoder and decoder utility.

## Installation

Install it via pip:

```console
pip install morsedecode
```

Alternatively, you can use `pipx` to run it without installing:

```console
pipx run morsedecode .... .. -.-.--
```

## Usage

```console
$ morsecode Hello World!
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--

$ morsedecode .... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--
HELLO WORLD!
```

## Development / Testing

To setup a development environment, run

```console
pip install -r requirements-dev.txt
```

Then run tests using:

```console
pytest
```

Or type-check your code using:

```console
mypy .
```
