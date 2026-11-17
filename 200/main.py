class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        n = 0
        nodes = []
        height = len(grid)
        width = len(grid[0])

        # Couple of notes:
        # - Write the nested loop instead of comprehension for lower memory footprint
        # - Modify the grid directly instead of a 'done' set for lower memory footprint
        # - This means you have to do a direct access whenever you need to check the value
        # - Use range() instead of enumerate() because you need to and uses less memory
        for i_line in range(height):
            for i_offs in range(width):
                idx = width * i_line + i_offs
                if grid[i_line][i_offs] == "0":
                    continue

                # at this point we know there's an isle
                nodes.append(idx)
                n += 1

                # explore the isle and mark adjacents
                while len(nodes) > 0:
                    i = nodes.pop()
                    o = i % width
                    l = i // width
                    if grid[l][o] == "0":
                        continue
                    if o - 1 >= 0 and grid[l][o - 1] != "0":
                        nodes.append(i - 1)
                    if o + 1 < width and grid[l][o + 1] != "0":
                        nodes.append(i + 1)
                    if l - 1 >= 0 and grid[l - 1][o] != "0":
                        nodes.append(i - width)
                    if l + 1 < height and grid[l + 1][o] != "0":
                        nodes.append(i + width)
                    # mark it as done
                    grid[l][o] = "0"

        return n
