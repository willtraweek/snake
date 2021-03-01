import numpy as np
from base_game.tile import Direction
import random
from queue import PriorityQueue
from base_game.menu import Menu


class DNA:
    mutation_rate = 10  # THE PERCENT CHANCE FOR A RANDOM MUTATION TO OCCUR
    fitness = 1  # INIT THIS VALUE TO 1
    depth = 5  # HIDDEN NODES LAYER COUNT = DEPTH - 1
    hidden_length = 15  # HOW MANY NODES IN EACH HIDDEN LAYER
    input_length = 0
    output_length = 4

    def __init__(self, mother=None, father=None):
        if self.input_length == 0:
            raise RuntimeError("Please set input length")
        self.genes = []

        for i in range(self.depth):
            if i == 0:
                temp = np.random.randint(low=-1, high=2, size=(self.input_length, self.hidden_length))
            elif i == self.depth - 1:
                temp = np.random.randint(low=-1, high=2, size=(self.hidden_length, self.output_length))
            else:
                temp = np.random.randint(low=-1, high=2, size=(self.hidden_length, self.hidden_length))

            if mother and father:
                for x in range(len(temp)):
                    for y in range(len(temp[x])):
                        if round(y) == 0:
                            temp[x][y] = mother.genes[i][x][y]
                        else:
                            temp[x][y] = father.genes[i][x][y]

                        if random.randint(0, 100) <= self.mutation_rate:
                            temp[x][y] = random.randint(-1, 1)

            self.genes.append(temp)

    def __lt__(self, other):
        return self.fitness > other.fitness  # HAD TO BE FLIPPED TO WORK IN THE PRIORITY QUEUE

    def predict(self, inputs):
        temp = inputs
        for i in range(self.depth):
            temp = np.dot(temp, self.genes[i])
        return temp


class Population:
    generation = 0
    # THESE ARE FOR MENU STATISTICS
    score = 0
    move_count = 0
    fitness = 0

    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        for _ in range(population_size):
            self.population.append(DNA())
        self.current = 0

    def _increment(self):
        """
        Moves to the next dna strand in the population and creates offspring if it reaches the end
        """
        if self.current == self.population_size - 1:
            self.current = 0
            self.generation += 1
            self.fill_statistics()
            self.create_offspring()
        else:
            self.current += 1

    def create_offspring(self):
        population = []
        for _ in range(self.population_size):
            mother, father = self.select_parents()
            child = DNA(mother, father)
            population.append(child)
        self.population = population

    def select_parents(self):
        """
        Uses a fitness proportionate methodology to select parents for breeding.  Individuals with higher fitness scores
        are more likely to be selected.  In a population of 4 with weights [1, 5, 10, 20], the first individual will
        have a 1/36 chance of being selected, and the last will have a 20/36 chance.
        """
        temp_queue = PriorityQueue(self.population_size)
        for pop in self.population:
            temp_queue.put(pop)

        self.population = []
        for i in range(self.population_size):
            if i > self.population_size * .8:
                self.population.append(temp_queue.get())

        fitness_weights = []
        for pop in self.population:
            # IF A POP HAS A NEGATIVE FITNESS, SET IT TO ZERO
            if pop.fitness < 0:
                pop.fitness = 0

            fitness_weights.append(pop.fitness)

        while len(self.population) < 2:
            # THIS MAKES SURE THERE ARE ALWAYS 2 PARENTS
            self.population.append(DNA())

        mother = weighted_random_selection(self.population, fitness_weights)
        father = weighted_random_selection(self.population, fitness_weights)
        #while mother == father:
            # PREVENT ONE STRONG GENE FROM RULING THE POOL
            #father = weighted_random_selection(self.population, fitness_weights)

        return mother, father
        temp = 0
        dna = 0
        for i in range(Math.random(sum_fitness)):
            if temp == 0: # MOVE ON TO THE NEXT GENE
                dna = self.population[]
