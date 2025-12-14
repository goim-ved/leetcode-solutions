from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    col = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            cell = board[r][c]
            if cell == ".":
                continue
            if (cell in rows[r] or
                cell in col[c] or
                cell in squares[(r // 3, c // 3)]):
                return False
            rows[r].add(cell)
            col[c].add(cell)
            squares[(r // 3, c // 3)].add(cell)
    return True

#myboard = [[1,2], [3,4]]
#print(myboard[1][0])