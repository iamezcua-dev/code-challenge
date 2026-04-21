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


def main() -> None:
    raw_data: list[str] = read_input()


if __name__ == "__main__":
    main()
