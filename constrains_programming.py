from constraint import Problem, AllDifferentConstraint

def solve_n_queens(n):
    # Initialize the problem
    problem = Problem()

    # Variables: positions of queens on the chessboard
    # Each variable represents a column, and its value represents the row
    columns = range(n)
    rows = range(n)

    # Add variables with their domains
    problem.addVariables(columns, rows)

    # Add constraints
    # 1. All columns must be different (already satisfied by the problem definition)
    # 2. All rows must be different
    problem.addConstraint(AllDifferentConstraint(), columns)
    
    # 3. Diagonals must be different
    def diagonal_constraint(*variables):
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                if abs(variables[i] - variables[j]) == abs(i - j):
                    return False
        return True
    problem.addConstraint(diagonal_constraint, columns)

    # Get the solutions
    solutions = problem.getSolutions()
    
    return solutions

# Solve the 8-queens problem
n = 8
solutions = solve_n_queens(n)

# Print the solutions
for solution in solutions:
    print(solution)

# Optionally, format and print the board for each solution
def print_solution(solution):
    board = [["." for _ in range(n)] for _ in range(n)]
    for col, row in solution.items():
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print("\n")

for solution in solutions:
    print_solution(solution)
