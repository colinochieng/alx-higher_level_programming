#!/usr/bin/python3
"""The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard"""


class Solution:
    """The N Queen solution generating class"""
    def solveNQueens(self, n):
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


def get_queen_positions(results):
    """Generating a list of lists containing list of positions"""
    queen_positions = []
    for result in results:
        positions = []
        for i in range(len(result)):
            for j in range(len(result)):
                if result[i][j] == 'Q':
                    positions.append([i, j])
        queen_positions.append(positions)
    return queen_positions


if __name__ == '__main__':
    import sys

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

    n = int(sys.argv[1])
    solution = Solution()
    results = solution.solveNQueens(n)
    queen_positions = get_queen_positions(results)
    for i in queen_positions:
        print(i)
