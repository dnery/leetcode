class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        isles = 0
        height = len(grid)
        width = len(grid[0])
        lis = []  # as in linear indexes

        # Notes:
        # - Write the nested loop instead of comprehension for lower memory footprint
        # - Modify the grid directly instead of a 'done' set for lower memory footprint
        # - This means you have to do a direct access whenever you need to check the value
        # - Use range() instead of enumerate() because you need to and uses less memory
        for row in range(height):
            for col in range(width):
                if grid[row][col] == "0":
                    continue

                # at this point there must be an isle
                lis.append(width * row + col)

                # explore the isle only once
                while len(lis) > 0:
                    li = lis.pop()
                    c = li % width
                    r = li // width
                    # ignore if already done
                    if grid[r][c] == "0":
                        continue
                    # check horizontal neighbors
                    if c - 1 >= 0 and grid[r][c - 1] != "0":
                        lis.append(li - 1)
                    if c + 1 < width and grid[r][c + 1] != "0":
                        lis.append(li + 1)
                    # check vertical neighbors
                    if r - 1 >= 0 and grid[r - 1][c] != "0":
                        lis.append(li - width)
                    if r + 1 < height and grid[r + 1][c] != "0":
                        lis.append(li + width)
                    # mark it as done
                    grid[r][c] = "0"

                isles += 1

        return isles
