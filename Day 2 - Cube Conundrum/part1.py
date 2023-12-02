#
# Advent Calender of Code 2024 ©️ Lance Ruiz
#

import regex

color_amount = {
    'red': 0, 'green': 0, 'blue': 0
}

color_max = {
    'red': 12, 'green': 13, 'blue': 14
}

def main():
    inputFile = open('input.txt', 'r')
    possible_game_ids_sum = 0

    for game in inputFile:
        parsed = regex.findall(f'\d+|{"|".join(color_amount)}', game)
        game_id = parsed.pop(0)

        revealed_cubes = parsed
        print(revealed_cubes)

        impossible_game = False

        while len(revealed_cubes) > 0:
            cube_amount = revealed_cubes.pop(0)
            cube_color = revealed_cubes.pop(0)

            if int(cube_amount) > color_max[cube_color]:
                impossible_game = True
                break

        if not impossible_game:
            possible_game_ids_sum += int(game_id)
            print(f'game {game_id} is impossible')
        else:
            print(f'game #{game_id}')

            # color_amount[cube_color] += int(cube_amount)
            # print(f'{cube_amount} {cube_color} ', end=('' if len(revealed_cubes) > 2 else '\n'))

    # print(color_amount)
    print(possible_game_ids_sum)

main()