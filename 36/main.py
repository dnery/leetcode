class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # check rows
        for row in range(9):
            for col in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue
                num = int(ch)
                sums = 0
                for c in range(9):
                    ch = board[row][c]
                    if ch != "." and int(ch) == num:
                        sums += num
                if num != sums:
                    return False

        # check cols
        for col in range(9):
            for row in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue
                num = int(ch)
                sums = 0
                for r in range(9):
                    ch = board[r][col]
                    if ch != "." and int(ch) == num:
                        sums += num
                if num != sums:
                    return False

        # check grids
        for grid in range(9):
            nums = {it: 0 for it in range(1, 10)}
            for gridrow in range(3):
                for gridcol in range(3):
                    row = (grid % 3) * 3 + gridrow
                    col = (grid // 3) * 3 + gridcol
                    ch = board[row][col]
                    if ch != ".":
                        if nums[int(ch)]:
                            return False
                        nums[int(ch)] = 1

        return True
