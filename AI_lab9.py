import random

# Knapsack Problem Parameters
max_capacity = 50
weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 150, 200]
pop_size = 50
num_generations = 100
mutation_prob = 0.1

def create_chromosome():
    return [random.choice([0, 1]) for _ in range(len(weights))]

def initialize_group():
    return [create_chromosome() for _ in range(pop_size)]

def compute_fitness(chromosome):
    total_val = sum(gene * val for gene, val in zip(chromosome, values))
    total_wt = sum(gene * wt for gene, wt in zip(chromosome, weights))
    # Penalize solutions that exceed the knapsack capacity
    if total_wt > max_capacity:
        return 0
    else:
        return total_val

def pick_parents(group):
    fitness_vals = [compute_fitness(chrom) for chrom in group]
    total_fitness = sum(fitness_vals)
    parents = []
    while len(parents) < pop_size:
        chosen_idx = random.choices(range(len(group)), weights=fitness_vals)[0]
        parents.append(group[chosen_idx])
    return parents

def crossover(parent_a, parent_b):
    split_point = random.randint(1, len(parent_a) - 1)
    child_a = parent_a[:split_point] + parent_b[split_point:]
    child_b = parent_b[:split_point] + parent_a[split_point:]
    return child_a, child_b

def mutate(chromosome):
    mutation_index = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_index] = 1 - chromosome[mutation_index]

def apply_mutation(group):
    for chrom in group:
        if random.random() < mutation_prob:
            mutate(chrom)

def genetic_knapsack():
    # Initialization
    population = initialize_group()
    for _ in range(num_generations):
        # Selection
        parents = pick_parents(population)
        # Crossover
        next_generation = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                offspring_a, offspring_b = crossover(parents[i], parents[i + 1])
                next_generation.extend([offspring_a, offspring_b])
        # Mutation
        apply_mutation(next_generation)
        # Replace old population with new generation
        population = next_generation
    # Return the best solution found
    optimal_solution = max(population, key=compute_fitness)
    return optimal_solution, compute_fitness(optimal_solution)

# Run the genetic algorithm
best_items, best_value = genetic_knapsack()
# Display the results
print("Best Solution (Selected items):", best_items)
print("Best Fitness (Total value):", best_value)
