from spandigital.app import format_ranking


def test_format_ranking():
    expected = [
        "1. Tarantulas, 6 pts",
        "2. Lions, 5 pts",
        "3. FC Awesome, 1 pt",
        "3. Snakes, 1 pt",
        "5. Grouches, 0 pts"
    ]

    ranking = [
        [1, "Tarantulas", 6],
        [2, "Lions", 5],
        [3, "FC Awesome", 1],
        [3, "Snakes", 1],
        [5, "Grouches", 0]
    ]
    actual = format_ranking(ranking)

    assert expected == actual
