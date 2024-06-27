#!/usr/bin/python3


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell starts with 4 possible perimeter edges
                perimeter += 4

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # Check bottom neighbor
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                # Check right neighbor
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
