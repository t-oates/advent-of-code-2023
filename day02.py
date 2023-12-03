"""Day 2 of the Advent of Code 2023.

See https://adventofcode.com/2023/day/2
"""

###### NOTE - CODE NOT YET FULLY TESTED/DOCUMENTED


def solve(input_file: str, part: int = 1) -> int:
    """Solve day 02."""
    with open(input_file) as f:
        input_lines = f.readlines()

    games = [parse_input_line(input_line) for input_line in input_lines]

    if part == 1:
        bag_contents = {'red': 12, 'green': 13, 'blue': 15}
        return sum(get_possible_games(games, bag_contents))

    elif part == 2:
        return sum(get_game_power(game) for game in games)

    else:
        raise ValueError(f"'part' must be 1 or 2, not {part}")


def parse_input_line(input_line: str):
    """Convert line of input data into list of dicts with cube quantities

    e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
         --> [{'blue': 3, 'red': 4},
              {'red': 1, 'green': 2, 'blue': 6},
              {'green': 2}]
    """
    return [parse_handful(handful)
            for handful in input_line.split(':')[-1].split(';')]


def parse_handful(handful_str: str):
    """Convert e.g. '3 blue, 4 red' to {'blue': 3, 'red': 4}"""
    handful = {}
    for item in handful_str.strip().split(', '):
        num, colour = item.split()
        handful[colour] = int(num)
    return handful


def get_possible_games(games, bag_contents):
    """Yield all games that are possible with a given bag contents.

    i.e., if one round of the game contains more cubes of a certain
    colour that the bag contents has, then the game is impossible."""
    for game_num, handfuls in enumerate(games, 1):
        if game_is_possible(handfuls, bag_contents):
            yield game_num


def game_is_possible(handfuls: list[dict[str, int]],
                     bag_contents: dict[str, int]) -> bool:
    """Determine whether a single game is possible with a given bag contents"""
    return all(handful_is_possible(handful, bag_contents)
               for handful in handfuls)


def handful_is_possible(handful: dict[str, int],
                        bag_contents: dict[str, int]) -> bool:
    """Determine whether a single handful is possible with a given bag contents"""
    for colour, num in handful.items():
        if num > bag_contents[colour]:
            return False
    return True


def get_game_power(handfuls):
    """Get 'power' of the game.

    This is take the minimum number of each colour of cubes required to make
    the game possible, and multiplying them together.
    """
    min_cubes = get_min_required_cubes(handfuls)
    return min_cubes[0] * min_cubes[1] * min_cubes[2]


def get_min_required_cubes(handfuls) -> tuple[int, int, int]:
    """Get minimum number of cubes of each colour required to play a game.

    This is returned as a tuple representing (red, green, blue).
    """
    return tuple(max(handful.get(colour, 0) for handful in handfuls)
                 for colour in 'red green blue'.split())



if __name__ == '__main__':
    print("Part 1:", solve('inputs/02.txt', part=1))
    print("Part 2:", solve('inputs/02.txt', part=2))
