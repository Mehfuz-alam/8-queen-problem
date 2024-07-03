import random

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(board):
    n = len(board)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                neighbor = list(board)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(n):
    current_board = random_board(n)
    current_conflicts = count_conflicts(current_board)
    
    while True:
        neighbors = get_neighbors(current_board)
        neighbor_conflicts = [(count_conflicts(neighbor), neighbor) for neighbor in neighbors]
        best_neighbor_conflicts, best_neighbor = min(neighbor_conflicts)
        
        if best_neighbor_conflicts >= current_conflicts:
            break
        
        current_board = best_neighbor
        current_conflicts = best_neighbor_conflicts
    
    return current_board, current_conflicts

def solve_n_queens(n):
    solution, conflicts = hill_climbing(n)
    while conflicts != 0:
        solution, conflicts = hill_climbing(n)
    return solution

if __name__ == "__main__":
    n = 8
    solution = solve_n_queens(n)
    print("Solution:")
    print_board(solution)
