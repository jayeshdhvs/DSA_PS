"""Module providing Function to check sudoku baord """
import collections
def is_valid(grid):
    """ This function checks if given Sudoku board is valid or not """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if grid[r][c]==".":
                continue
            if (grid[r][c] in rows[r]
                or grid[r][c] in cols[c]
                or grid[r][c] in boxes[(r//3,c//3)]):
                return "Invalid"
    return "Valid"

INPUT = "53..7....\n6..195...\n.98...\
        .6.\n8...6...3\n4..8.3..\
        1\n7...2...6\n.6....28.\n...419..5\n....8..79"

def create_borad(values):
    """Create a sudoku borad from users input"""
    board = []
    refined_input = values.split('\n')
    for i in range(9):
        row = refined_input[i]
        board.append(row)
    return board

Board = create_borad(INPUT)
IS_VALID = is_valid(Board)
print("Given Sudoku board is ",IS_VALID)
