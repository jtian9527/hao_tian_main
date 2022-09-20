class Solution:
    def isValidSudoku(self, board):
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    #index是0开始的，所以需要-1
                    c = int(c) -1
                    rows[i][c] = rows[i][c] + 1
                    columns[c][j] = columns[c][j] + 1
                    subboxes[int(i/3)][int(j/3)][c] = subboxes[int(i/3)][int(j/3)][c] + 1
                    #判断
                    if rows[i][c]>1 or columns[c][j]>1 or subboxes[int(i/3)][int(j/3)][c]>1:
                        return False
        return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))

