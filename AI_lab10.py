import random

num_jobs = 6
num_machines = 3
processing_times = [2, 5, 8, 4, 6, 3]  
population_size = 10
mutation_rate = 0.1
generations = 50

def generate_chromosome():
    return [random.randint(0, num_machines - 1) for _ in range(num_jobs)]

def fitness(chromosome):
    machine_loads = [0] * num_machines
    for job, machine in enumerate(chromosome):
        machine_loads[machine] += processing_times[job]
    return max(machine_loads) 

def selection(population):
    return min(random.sample(population, 2), key=lambda c: fitness(c))

def crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(num_jobs), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx = random.randint(0, num_jobs - 1)
        chromosome[idx] = random.randint(0, num_machines - 1)

def genetic_algorithm():
    population = [generate_chromosome() for _ in range(population_size)]
    for gen in range(generations):
        population = sorted(population, key=fitness)
        new_population = population[:2]  # Keep best two (elitism)
        while len(new_population) < population_size:
            parent1, parent2 = selection(population), selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
    best_schedule = min(population, key=fitness)
    print("Best Schedule:", best_schedule, "Min Completion Time:", fitness(best_schedule))

# Run Genetic Algorithm
genetic_algorithm()