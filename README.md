# Code Challenge

## Purpose

This awesome tool helps you parse your favorite team's match results
and helps you visualize the current rankings from them.

## Installation Steps

### Prerequisites

- Operating System:

| OS      | Version                  |
|---------|--------------------------|
| Windows | Windows 11 or higher     |
| Mac     | macOS Catalina or Higher |
| Linux   | Ubuntu 22.x              |

- Resources:

| Resource Type | Minimum Requirement             |
|---------------|---------------------------------|
| RAM           | At least 100 MB of free memory. |
| CPU           | Just a single core is needed.   |

### Installation

1. Download `uv` tool using the official docs here: https://docs.astral.sh/uv/getting-started/installation/.

> [!NOTE]
> Please make sure you meet the requirements needed for installing `uv`, described in the documentation.

2. Clone this repository in your local computer using:
    ```sh
    git clone https://github.com/iamezcua-dev/code-challenge.git
    ```
3. Enter to the generated folder and from there, run:

   ```sh
   uv tool install .
   ```

> [!NOTE]
> After you have run this command, you should have a `game-stats` executable ready to use.

## Usage

1. You should have a file containing your game matches, which should meet the following format:
   ```csv
   Lions 3, Snakes 3
   Tarantulas 1, FC Awesome 0
   Lions 1, FC Awesome 1
   Tarantulas 3, Snakes 1
   Lions 4, Grouches 0
   ```

2. Use the `game-stats` tool to get your rankings:
   ```sh
   game-stats --filename <your-file-path.extension>
   ```

### Uninstallation

1. To remove this tool, you must execute this command.
   ```sh
   uv tool uninstall code-challenge
   ```
2. You can optionally remove the cloned repo and follow the instuctions to uninstall `uv`
   described [here](https://docs.astral.sh/uv/getting-started/installation/#uninstallation).

## Support

If you see something weird, please report it to [Eddie Jobs](iamezcua.dev@gmail.com).
