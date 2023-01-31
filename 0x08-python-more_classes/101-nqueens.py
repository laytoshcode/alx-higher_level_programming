import sys

def solve_nqueens(n):
    def is_not_under_attack(row, col):
        # check if there is a queen in the same row
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def nqueens(row, n):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_not_under_attack(row, col):
                board[row] = col
                nqueens(row + 1, n)

    board = [-1] * n
    result = []
    nqueens(0, n)
    return result

def print_solutions(solutions, n):
    for solution in solutions:
        for i in range(n):
            line = ""
            for j in range(n):
                if solution[i] == j:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("")

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

    solutions = solve_nqueens(n)
    print_solutions(solutions, n)

