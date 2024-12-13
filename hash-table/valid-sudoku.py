from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_digits = defaultdict(set)
        col_digits = defaultdict(set)
        box_digits = defaultdict(set)
        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in row_digits[row] or board[row][col] in col_digits[col] or board[row][col] in box_digits[(row//3, col//3)]):
                    return False
                row_digits[row].add(board[row][col])
                col_digits[col].add(board[row][col])
                box_digits[(row//3, col//3)].add(board[row][col])
        return True
