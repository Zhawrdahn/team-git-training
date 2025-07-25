from app.utils import greet_user


def test_greet_user(capsys):
    greet_user("Tester")
    captured = capsys.readouterr()
    assert "Hello, Tester!" in captured.out
