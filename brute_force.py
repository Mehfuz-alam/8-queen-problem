from itertools import permutations

def solve_8_queens_brute_force():
    N = 8
    solutions = []
    cols = range(N)
    for perm in permutations(cols):
        if N == len(set(perm[i] + i for i in cols)) == len(set(perm[i] - i for i in cols)):
            solutions.append(perm)
    return solutions

def print_solution(solution):
    board = [["." for _ in range(8)] for _ in range(8)]
    for col, row in enumerate(solution):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print("\n")

if __name__ == "__main__":
    solutions = solve_8_queens_brute_force()
    print(f"Number of solutions: {len(solutions)}")
    for solution in solutions:
        print_solution(solution)
