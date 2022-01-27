"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""

import numpy as np
import math

def different_sum_count_bounded(N, z):
    """
    Ways of writing N as sum of positive integers x,y <= z
    """
    if N > 2*z:
        return 0
    min_x = max(1, N-z)
    max_x = N-min_x
    return (max_x - min_x + 2) // 2

counts = np.zeros(2000, dtype=int)

for N in range(2,4000):
    for z in range(N//2, 2000):
        d_sq = z*z + N*N
        d = round(math.sqrt(d_sq))
        if d * d == d_sq:
            counts[z] += different_sum_count_bounded(N, z)

count_sum = np.cumsum(counts)
print(np.searchsorted(count_sum, 1000000))
