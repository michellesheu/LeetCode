from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize your three defaultdict(set) objects.
        # Loop through $r$ from $0$ to $8$
        # :Loop through $c$ from $0$ to $8$:
        # Get the value $v$ at board[r][c].
        # If $v$ is ".", skip.
        # Check the three sets using the expression above.
        # Return False if a duplicate is found.
        # Add $v$ to rows[r], cols[c], and blocks[(r // 3, c // 3)].
        # Return True at the very end.
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        row_len = len(board)
        col_len = len(board[0])
        for r in range(row_len):
            for c in range(col_len):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in rows[r] or val in cols[c] or val in blocks[(r//3,c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                blocks[(r//3,c//3)].add(val)
        return True