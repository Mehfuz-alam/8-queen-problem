import random
from deap import base, creator, tools, algorithms

# Problem parameters
N_QUEENS = 8

# Fitness function: Number of non-attacking pairs of queens
def eval_queens(individual):
    size = len(individual)
    # Count the number of pairs of queens that do not attack each other
    horizontal_collisions = sum([individual.count(queen)-1 for queen in individual]) / 2
    diagonal_collisions = 0

    n = len(individual)
    left_diagonal = [0] * (2*n-1)
    right_diagonal = [0] * (2*n-1)
    for i in range(n):
        left_diagonal[i+individual[i]] += 1
        right_diagonal[n-1-i+individual[i]] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        if left_diagonal[i] > 1:
            diagonal_collisions += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            diagonal_collisions += right_diagonal[i] - 1

    return int(maxFitness - (horizontal_collisions + diagonal_collisions)),  # fitness score

def print_board(board):
    for row in board:
        line = ""
        for col in range(len(board)):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

# Set up the DEAP toolbox
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(N_QUEENS), N_QUEENS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxUniform, indpb=0.5)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_queens)

# Genetic Algorithm constants:
population_size = 300
crossover_probability = 0.7
mutation_probability = 0.2
generations = 100

maxFitness = (N_QUEENS*(N_QUEENS-1))/2  # 8*7/2=28

# Initialize population
population = toolbox.population(n=population_size)

# Run the Genetic Algorithm
for gen in range(generations):
    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < crossover_probability:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < mutation_probability:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate individuals with invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # Replace the population with the offspring
    population[:] = offspring

    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in population]

    length = len(population)
    mean = sum(fits) / length
    sum2 = sum(x*x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5

    print(f"Generation {gen}: Max {max(fits)}, Avg {mean}, Std {std}")

    # Check for solution
    if max(fits) == maxFitness:
        best_ind = tools.selBest(population, 1)[0]
        print(f"Best individual found in generation {gen}: {best_ind}")
        print_board(best_ind)
        break
else:
    best_ind = tools.selBest(population, 1)[0]
    print("No perfect solution found.")
    print(f"Best individual: {best_ind}")
    print_board(best_ind)
