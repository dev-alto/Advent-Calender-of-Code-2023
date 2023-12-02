#
# Advent Calender of Code 2024 ©️ Lance Ruiz
#

import regex

color_max = {
    'red': 12, 'green': 13, 'blue': 14
}

def main():
    inputFile = open('input.txt', 'r')

    sum_power = 0

    for game in inputFile:
        parsed = regex.findall(f'\d+|{"|".join(color_max)}', game)
        game_id = parsed.pop(0)

        print(f'game #{game_id}')

        revealed_cubes = parsed

        cube_max_amount = {
            'red': 0, 'green': 0, 'blue': 0
        }       
        
        while len(revealed_cubes) > 0:
            cube_amount = int(revealed_cubes.pop(0))
            cube_color = revealed_cubes.pop(0)
            
            # print(str(cube_amount) + ' ' + cube_color)
            if cube_max_amount[cube_color] < cube_amount:
                cube_max_amount[cube_color] = cube_amount

        power = cube_max_amount['red'] * cube_max_amount['green'] * cube_max_amount['blue']
        sum_power = sum_power + power
        # print(power)
        print(cube_max_amount)
        
    print(sum_power)

main()