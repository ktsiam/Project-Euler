"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

cube_map = {}

for i in range(100000):
    cube = "".join(reversed(sorted(str(i**3))))
    if cube not in cube_map:
        cube_map[cube] = []
    cube_map[cube].append(i)
    if len(cube_map[cube]) >= 5:
        print(cube, cube_map[cube], cube_map[cube][0]**3)
        exit(0)
        
