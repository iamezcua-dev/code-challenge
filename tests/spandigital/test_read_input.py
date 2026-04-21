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


def test_read_input_no_filename_arg(monkeypatch):
    monkeypatch.setattr('sys.argv', ['app'])
    actual = read_input()
    assert actual == []


def test_read_input_file_not_found(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename', 'input/nonexistent.txt'])
    actual = read_input()
    assert actual == []


def test_read_input_filters_blank_lines(monkeypatch, tmp_path):
    f = tmp_path / "blanks.txt"
    f.write_text("Lions 3, Snakes 3\n\n\nTarantulas 1, FC Awesome 0\n  \n")
    monkeypatch.setattr('sys.argv', ['--filename', str(f)])
    actual = read_input()
    assert actual == ["Lions 3, Snakes 3", "Tarantulas 1, FC Awesome 0"]


def test_read_input_missing_value_after_filename_flag(monkeypatch):
    monkeypatch.setattr('sys.argv', ['--filename'])
    actual = read_input()
    assert actual == []
