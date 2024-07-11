#!/usr/bin/env python3
"""N QUEENS"""
import sys


def nqueens():
    """A function that defines the moves of a queen in a chess"""
    def print_usage_and_exit():
        print("Usage: nqueens N")
        sys.exit(1)

    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def solve_n_queens(n):
        def is_safe(board, row, col):
            for i in range(col):
                if board[row][i] == 1:
                    return False

            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            return True

        def solve_recursively(board, col):
            if col >= n:
                val.append([[i, row.index(1)] for i, row in enumerate(board)])
                return

            for i in range(n):
                if is_safe(board, i, col):
                    board[i][col] = 1
                    solve_recursively(board, col + 1)
                    board[i][col] = 0

        val = []
        board = [[0 for _ in range(n)] for _ in range(n)]
        solve_recursively(board, 0)
        return val

    if len(sys.argv) != 2:
        print_usage_and_exit()

    arg = sys.argv[1]
    if not is_integer(arg):
        print("N must be a number")
        sys.exit(1)

    N = int(arg)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    nqueens()
