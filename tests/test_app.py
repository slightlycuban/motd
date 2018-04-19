"""Just an E2E test for MotD"""

def test_get_a_message(client):
    result = client.get('/')

    assert result.status_code == 200, "getting index should be ok"

    assert "Your sage thought of the day" in result.data, \
        "getting index should show us a message"
