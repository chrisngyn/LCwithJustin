"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

-----

Intuition (and with help from a YouTube video lol).

1. loop through the entire grid. when we find a 0, irrelevant. but when we find a 1, we should do something.
2. we should call a DFS helper function on the cell we find a '1' in, because we want to find all the neighbouring '1's as well.
3. we'll flip all the '1's we find from our DFS call to a 0 so that we don't accidentally call DFS on a connected part again.
"""

from typing import List

def numberIslands(grid: List[List[int]]) -> int:
    if grid is None or len(grid) == 0:  # malformed input, no islands in these cases
        return 0
    
    ret = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                ret += 1  # found an island
                dfsHelper(grid, i, j)  # run the dfs helper on it to flip all the connecting '1's to '0's

    return ret  # at the end of this nested for loop, we've have gone through all the elements, we have the # of islands!

def dfsHelper(grid: List[List[int]], i: int, j: int) -> None:
    # need to do a bunch of checks in the beginning so we know when to just terminate
    if i < 0 or i >= len(grid):  # out of bounds (i represents up and down)
        return
    if j < 0 or j >= len(grid[i]):
        return
    if grid[i][j] == '0':  # if we find a '0' in our traversal, terminate
        return
    else:
        grid[i][j] = '0'  # if we find a '1', flip it to a '0'
    
    dfsHelper(grid, i-1, j)  # call dfs 'up'
    dfsHelper(grid, i+1, j)  # call dfs 'down'
    dfsHelper(grid, i, j-1)  # call dfs 'left'
    dfsHelper(grid, i, j+1)  # call dfs 'right'

    return


grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numberIslands(grid1))  # 1
print(numberIslands(grid2))  # 3
