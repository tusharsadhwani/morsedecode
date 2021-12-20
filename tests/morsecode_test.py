import pytest

import morsecode


@pytest.mark.parametrize(("string", "output"), (("SOS", "... --- ..."),))
def test_encode(string, output):
    """Tests encoding from text to morse code"""

    assert morsecode.encode(string) == output


@pytest.mark.parametrize(("string", "output"), (("... --- ...", "SOS"),))
def test_decode(string, output):
    """Tests encoding from text to morse code"""

    assert morsecode.decode(string) == output
