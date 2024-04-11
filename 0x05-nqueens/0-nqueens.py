#!/usr/bin/python3
import sys


def solveNQueens(n):
    cols = set()
    posDiag = set()  # r + c
    negDiag = set()  # r - c

    solutions = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            curr_sol = ["".join(row) for row in board]
            solutions.append(curr_sol)
            return

        for c in range(n):
            if c in cols or r + c in posDiag or r - c in negDiag:
                continue

            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return solutions


def print_solutions(solutions):
    positions = []

    for sol in solutions:
        pos = []
        for row in range(n):
            for col in range(n):
                if sol[row][col] == "Q":
                    pos.append([row, col])
                    break
        positions.append(pos)

    for pos in positions:
        print(pos)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQueens(n)
    print_solutions(solutions)
