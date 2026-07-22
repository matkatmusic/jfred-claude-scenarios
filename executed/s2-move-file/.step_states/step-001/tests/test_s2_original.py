from s2_original import hello


def test_hello(capsys):
    hello()
    assert capsys.readouterr().out == "hello\n"
