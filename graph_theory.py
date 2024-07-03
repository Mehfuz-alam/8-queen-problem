def solve_8_queens():
    board = [[0] * 8 for _ in range(8)]  # Initialize an 8x8 board
    
    def is_valid(board, row, col):
        # Check if placing a queen at board[row][col] is valid
        # Check same column
        for i in range(row):
            if board[i][col] == 1:
                return False
        # Check upper-left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 1:
                return False
        # Check upper-right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
            if board[i][j] == 1:
                return False
        return True
    
    def dfs(board, row):
        if row == 8:
            return True
        for col in range(8):
            if is_valid(board, row, col):
                board[row][col] = 1  # Place queen
                if dfs(board, row + 1):
                    return True
                board[row][col] = 0  # Backtrack
        return False
    
    # Start DFS from the first row
    if dfs(board, 0):
        return board
    else:
        return None

def print_board(board):
    if board is None:
        print("No solution found.")
        return
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

if __name__ == "__main__":
    solution = solve_8_queens()
    print_board(solution)
