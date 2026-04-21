from spandigital.app import get_teams_ranking


def test_get_teams_ranking():
    data = {
        'Grouches': 0,
        'Lions': 5,
        'Tarantulas': 6,
        'Snakes': 1,
        'FC Awesome': 1
    }

    expected = [
        [1, "Tarantulas", 6],
        [2, "Lions", 5],
        [3, "FC Awesome", 1],
        [3, "Snakes", 1],
        [5, "Grouches", 0]
    ]

    actual = get_teams_ranking(data)

    assert expected == actual
