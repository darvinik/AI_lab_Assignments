import random

NUM_ITEMS = 10
BIN_CAPACITY = 10
ITEM_SIZES = [random.randint(1, 10) for _ in range(NUM_ITEMS)]
POPULATION_SIZE = 50
MUTATION_RATE = 0.1
NUM_GENERATIONS = 100

def initialize_population():
    return [[random.randint(0, len(ITEM_SIZES) - 1) for _ in ITEM_SIZES] for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    bins = {}
    for item, bin_id in enumerate(chromosome):
        bins.setdefault(bin_id, []).append(ITEM_SIZES[item])
    return len(bins) + sum(max(0, sum(b) - BIN_CAPACITY) for b in bins.values())  

def selection(population):
    fitness_scores = [1 / (1 + fitness(c)) for c in population]
    total = sum(fitness_scores)
    probabilities = [f / total for f in fitness_scores]
    return random.choices(population, weights=probabilities, k=2)

def crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_algorithm():
    population = initialize_population()
    for _ in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        population = sorted(new_population, key=fitness)[:POPULATION_SIZE] 
    return min(population, key=fitness)

best_solution = genetic_algorithm()
print("Best Packing Solution:", best_solution)
print("Fitness Score (Lower is Better):", fitness(best_solution))
