import numpy as np
from base_game.tile import Direction
import Math

class DNA:
    mutation_rate = .05
    fitness = 0


class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = [] * population_size

    def create_offspring(self):


    def select_parent(self):
        """
        Uses a fitness proportionate methodology to select parents for breeding.  Individuals with higher fitness scores
        are more likely to be selected.  In a population of 4 with weights [1, 5, 10, 20], the first individual will
        have a 1/36 chance of being selected, and the last will have a 20/36 chance.
        """
        sum_fitness = 0
        for pop in self.population:
            sum_fitness += pop.fitness

        temp = 0
        dna = 0
        for i in range(Math.random(sum_fitness)):
            if temp == 0: # MOVE ON TO THE NEXT GENE
                dna = self.population[]
