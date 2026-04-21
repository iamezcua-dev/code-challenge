from spandigital.app import read_input


def test_read_input_from_file(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename', 'input/input.txt'])
    expected = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0"
    ]
    actual = read_input()
    assert expected == actual


def test_read_input_from_empty_file(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename', 'input/empty_input.txt'])
    expected = []
    actual = read_input()
    assert expected == actual
