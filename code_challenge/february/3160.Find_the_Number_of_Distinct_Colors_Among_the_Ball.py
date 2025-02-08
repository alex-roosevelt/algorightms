# You are given an integer limit and a 2D array queries of size n x 2.

# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

# Note that when answering a query, lack of a color will not be considered as a color.

import collections
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        f = collections.Counter()
        colors = {}
        ans = []

        for x, y in queries:
            p = None
            if x in colors:
                p = colors[x]
                f[p] -=1

                if f[p] == 0:
                    del f[p]
            f[y] +=1
            colors[x] = y
            ans.append(len(f))
        
        return ans