import random
from simanneal import Annealer

class QueensProblem(Annealer):
    def __init__(self, state):
        super(QueensProblem, self).__init__(state)

    def move(self):
        """Randomly swap two columns' values"""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculate the number of conflicting pairs of queens"""
        conflicts = 0
        n = len(self.state)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(self.state[i] - self.state[j]) == j - i:
                    conflicts += 1
        return conflicts

def print_board(state):
    n = len(state)
    board = [["." for _ in range(n)] for _ in range(n)]
    for col, row in enumerate(state):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print("\n")

if __name__ == "__main__":
    n = 8
    initial_state = list(range(n))
    random.shuffle(initial_state)

    queens = QueensProblem(initial_state)
    queens.Tmax = 10.0  # Max temperature
    queens.Tmin = 0.1   # Min temperature
    queens.steps = 10000  # Number of iterations

    state, e = queens.anneal()

    print("Final board:")
    print_board(state)
    print(f"Final energy (number of conflicts): {e}")
