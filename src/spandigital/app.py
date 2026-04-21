import sys


def read_input():
    raw_data = []

    if '--filename' in sys.argv:
        filename = sys.argv[sys.argv.index('--filename') + 1]
        with open(filename, 'r') as f:
            raw_data = f.read().splitlines()

    if len(raw_data) > 0:
        raw_data = [data for data in raw_data if data.strip() != ""]

    return raw_data


def compute_scoreboard(game_matches: list[str]) -> dict[str, int]:
    scoreboard = {}

    scores = {
        'win': 3,
        'tie': 1
    }

    for game_match in game_matches:
        if not ',' in game_match:
            print(f"Skipping malformed line: {game_match}...")
        else:
            team_and_score1, team_and_score2 = game_match.rsplit(',', 1)
            if team_and_score1 == '' or team_and_score2 == '':
                print(f"Skipping malformed line: {game_match}...")
            else:
                team_score1 = team_and_score1.strip().rsplit(' ', 1)
                team_score2 = team_and_score2.strip().rsplit(' ', 1)
                team1 = team_score1[0]
                team2 = team_score2[0]
                import re
                score1 = int(re.sub(r'\D', '', team_score1[1]))
                score2 = int(re.sub(r'\D', '', team_score2[1]))

                if score1 > score2:
                    scoreboard[team1] = scoreboard.get(team1, 0) + scores['win']
                    scoreboard[team2] = scoreboard.get(team2, 0)
                elif score1 == score2:
                    scoreboard[team1] = scoreboard.get(team1, 0) + scores['tie']
                    scoreboard[team2] = scoreboard.get(team2, 0) + scores['tie']
                else:
                    scoreboard[team1] = scoreboard.get(team1, 0)
                    scoreboard[team2] = scoreboard.get(team2, 0) + scores['win']

    return scoreboard


def get_teams_ranking(scoreboard: dict[str, int]) -> list[list[str]]:
    ranking = []
    previous_score = None
    current_rank = 1
    for rank, items in enumerate(sorted(scoreboard.items(), key=lambda item: (-item[1], item[0])), 1):
        team, score = items
        if score != previous_score:
            current_rank = rank
        ranking.append([current_rank, team, score])
        previous_score = score

    return ranking


def format_ranking(ranking: list[list[str]]) -> list[str]:
    pass


def main() -> None:
    raw_data: list[str] = read_input()
    scoreboard: dict[str, int] = compute_scoreboard(raw_data)
    ranking: list[list[str]] = get_teams_ranking(scoreboard)
    # formatted_ranking: list[str] = format_ranking(ranking)
    # print('\n'.join(formatted_ranking))


if __name__ == "__main__":
    main()
