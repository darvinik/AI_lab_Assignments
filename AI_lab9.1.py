import random

# Number of individuals in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"

# Take target string input from the user
TARGET = input("Enter the target string: ")

class Individual:
    """
    Class representing an individual in the population
    """
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        """Create random genes for mutation"""
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        """Create a chromosome or string of genes"""
        return [cls.mutated_genes() for _ in range(len(TARGET))]

    def mate(self, par2):
        """Perform mating and produce new offspring"""
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome)

    def cal_fitness(self):
        """Calculate fitness score"""
        return sum(1 for gs, gt in zip(self.chromosome, TARGET) if gs != gt)


def initialize_population():
    """Generate initial population"""
    return [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]


def select_parents(population):
    """Select parents for crossover"""
    return random.sample(population, k=2)


def crossover(parent1, parent2):
    """Perform crossover to produce offspring"""
    child_chromosome = [
        parent1.chromosome[i] if random.random() < 0.45 else
        parent2.chromosome[i] if random.random() < 0.90 else
        Individual.mutated_genes()
        for i in range(len(TARGET))
    ]
    return Individual(child_chromosome)


def main():
    global POPULATION_SIZE
    generation = 1
    found = False
    population = initialize_population()

    while not found:
        population = sorted(population, key=lambda x: x.fitness)
        if population[0].fitness == 0:
            found = True
            break

        new_generation = population[:int(0.1 * POPULATION_SIZE)]  # Elitism
        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            new_generation.append(child)

        population = new_generation
        print("Generation: {}	String: {}	Fitness: {}".format(
            generation, "".join(population[0].chromosome), population[0].fitness))
        generation += 1

    print("Final Generation: {}	String: {}	Fitness: {}".format(
        generation, "".join(population[0].chromosome), population[0].fitness))


if __name__ == '__main__':
    main()