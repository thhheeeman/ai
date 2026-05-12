def is_safe(board, row, col, n):

    # Check upper column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:

        for i in board:
            print(i)

        print()
        return

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            solve(board, row + 1, n)

            board[row][col] = 0


# Main Program
n = 4

board = [[0] * n for _ in range(n)]

solve(board, 0, n)