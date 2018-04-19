import pytest

from motd.util import random_quote

def test_random_quote_returns_quote(quote):
    rando = random_quote([quote])

    assert rando == quote, "it should pick our quote out of the list"


def test_random_throws_error_on_empty():
    with pytest.raises(Exception):
        random_quote([])
