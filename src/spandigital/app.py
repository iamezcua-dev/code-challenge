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


def compute_scoreboard(data: list[str]) -> dict[str, int]:
    pass


def get_teams_ranking(scoreboard: dict[str, int]) -> list[list[str]]:
    pass


def main() -> None:
    raw_data: list[str] = read_input()
    scoreboard: dict[str, int] = compute_scoreboard(raw_data)
    ranking: list[list[str]] = get_teams_ranking(scoreboard)
    print(ranking)


if __name__ == "__main__":
    main()
