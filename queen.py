import numpy as np

def is_valid_move(board, row, col):
    """
    Determines if a given queen placement on the board is valid.
    """
    # Check if the column is already occupied by another queen
    if np.any(board[:, col]):
        return False

    # Check if the row is already occupied by another queen
    if np.any(board[row, :]):
        return False

    # Check if the diagonal is already occupied by another queen
    n = board.shape[0]
    if np.any(np.diag(board, k=col-row)):
        return False
    if np.any(np.diag(np.fliplr(board), k=n-col-row)):
        return False

    return True

def solve_queen(board, row):
    """
    Solves the N-Queens problem recursively using backtracking.
    """
    # Base case: all queens have been placed
    if row == board.shape[0]:
        return True

    for col in range(board.shape[1]):
        if is_valid_move(board, row, col):
            board[row, col] = 1
            if solve_queen(board, row+1):
                return True
            board[row, col] = 0

    return False

def n_queens(n):
    """
    Finds all possible solutions to the N-Queens problem.
    """
    board = np.zeros((n, n))
    solutions = []
    solve_queen(board, 0)

    for board in all_boards:
        solution = [(i, np.argmax(row)) for i, row in enumerate(board)]
        solutions.append(solution)

    return solutions
