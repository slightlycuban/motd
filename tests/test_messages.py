from mock import patch
import pytest

from motd import get_quotes, load_quotes, Message


class TestGetQuotes(object):
    def test_get_quotes_returns_quotes(self, quote):
        with patch('motd.Message.query') as mock_query:
            mock_query.all.return_value = [Message(quote=quote)]

            quotes = get_quotes()

            assert quotes == [quote], "should just return the quote"


class TestLoadQuotes(object):
    def test_load_quotes_with_empty_db(self, quote):
        with patch('motd.db') as mock_db, \
            patch('motd.Message.query') as mock_query:

            mock_query.all.return_value = []
            quotes = [quote]

            load_quotes(quotes)

            args, _ = mock_db.session.add.call_args
            message, = args
            assert message.quote == quote, "should save what we quoted"

    def test_load_quotes_with_full_db(self, quote):
        with patch('motd.db') as mock_db, \
            patch('motd.Message.query') as mock_query:

            mock_query.all.return_value = [Message(quote=quote)]
            quotes = [quote]

            load_quotes(quotes)

            # It shouldn't try to save anything
            mock_db.session.add.assert_not_called()

    def test_load_quotes_with_partial(self, quote, double_quote):
        with patch('motd.db') as mock_db, \
            patch('motd.Message.query') as mock_query:

            mock_query.all.return_value = [Message(quote=quote)]
            quotes = [quote, double_quote]

            load_quotes(quotes)

            assert mock_db.session.add.call_count == 1, \
                "should only call add once"
            args, _ = mock_db.session.add.call_args
            message, = args
            assert message.quote == double_quote, \
                "should save the extra quote"
