from spandigital.app import compute_scoreboard, read_input


def test_compute_scoreboard(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename', 'input/input.txt'])
    data = read_input()

    expected = {
        'Grouches': 0,
        'Lions': 5,
        'Tarantulas': 6,
        'Snakes': 1,
        'FC Awesome': 1
    }
    actual = compute_scoreboard(data)
    assert expected == actual


def test_compute_scoreboard_with_malformed_input(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename', 'input/malformed_input.txt'])
    data = read_input()

    expected = {
        ',Tarantulas': 3,
        'Snakes': 0,
        'Lions': 3,
        'Grouches': 0
    }
    actual = compute_scoreboard(data)

    assert expected == actual
