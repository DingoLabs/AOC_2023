'''
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

'''

import fileinput
import re

bounds = {
    'red': 12,
    'green': 13,
    'blue': 14
}

answer = 0

with fileinput.input(files=('/Users/phillipcarman/projects/AOC2023/day02/input.txt')) as f:
    for line in f:
        game, cubes = line.split(": ")
        game = int(game[5:])

        poss = True
        for part in cubes.split('; '):
            aa = part.split(', ')
            for c in aa:
                num, color = c.split()
                if int(num) > bounds[color]:
                    poss = False

        answer += int(game) if poss else 0
        print(f"current answer: {answer}")
    print(f"final answer: {answer}")
