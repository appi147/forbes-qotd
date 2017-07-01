from forbesqotd import qotd

def test_1():
    app = qotd.forbes()
    s = app.get_quote()
    assert isinstance(s, basestring)
