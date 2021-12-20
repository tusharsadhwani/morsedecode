import pytest

import morsecode


@pytest.mark.parametrize(
    ("string", "output"),
    (
        ("SOS", "... --- ..."),
        ("OH, HI MARK!", "--- .... --..-- / .... .. / -- .- .-. -.- -.-.--"),
    ),
)
def test_encode(string: str, output: str) -> None:
    """Tests encoding from text to morse code"""

    assert morsecode.encode(string) == output


@pytest.mark.parametrize(
    ("string", "output"),
    (
        ("... --- ...", "SOS"),
        ("--- .... --..-- / .... .. / -- .- .-. -.- -.-.--", "OH, HI MARK!"),
    ),
)
def test_decode(string: str, output: str) -> None:
    """Tests encoding from text to morse code"""

    assert morsecode.decode(string) == output
