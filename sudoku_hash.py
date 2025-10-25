from sudoku import Sudoku
puzzle = Sudoku(3, 2)
puzzle.show()

board = puzzle.board
print(board)

solution = puzzle.solve()
solution.show_full()