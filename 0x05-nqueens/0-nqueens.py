#!/usr/bin/env python3
"""Nqueens"""
import sys


def print_usage_and_exit():
    """Shows the use and exit with code 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_integer(s) -> bool:
    """Checks if a given parameter is an integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False


def solve_n_queens(n):
    """Solves the problem"""
    def is_safe(board, row, col):
        """CHecks if a slot on the board is safe for the Queen"""
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
            res.append([[i, row.index(1)] for i, row in enumerate(board)])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve_recursively(board, col + 1)
                board[i][col] = 0

    res = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_recursively(board, 0)
    return res


def main():
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
    main()
