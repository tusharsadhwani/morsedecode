import pytest

import morsedecode


@pytest.mark.parametrize(
    ("string", "output"),
    (
        ("SOS", "... --- ..."),
        ("Oh, hi Mark!", "--- .... --..-- / .... .. / -- .- .-. -.- -.-.--"),
        ("A*b", ".- -..."),
    ),
)
def test_encode(string: str, output: str) -> None:
    """Tests encoding from text to morse code"""
    assert morsedecode.encode(string) == output


@pytest.mark.parametrize(
    ("string", "output"),
    (
        ("... --- ...", "SOS"),
        ("--- .... --..-- / .... .. / -- .- .-. -.- -.-.--", "OH, HI MARK!"),
        ("test .- bruh -...", "AB"),
    ),
)
def test_decode(string: str, output: str) -> None:
    """Tests encoding from text to morse code"""
    assert morsedecode.decode(string) == output
