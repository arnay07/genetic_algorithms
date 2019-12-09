#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`individual` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 30/11/2019

"""

from random import *
import math

POPULATION_SIZE = 600
LETTERS = 'abcdefghijklmnopqrstuvwxyz '
TARGET = "ceci est le secret a retrouver ce que nous voyons"

class Individual(object):
    def __init__(self, size):
        self.__size = size
        self.__chromosome = self.init_value()
        self.__fitness = 0

    def init_value(self):
        """
        randomly initialize the genome value of self

        :return: the genome of self
        :rtype: list
        """
        genome = []
        for i in range(self.get_size()):
            genome.append(choice(LETTERS))
        return genome

    def get_size(self):
        return self.__size

    def evaluate(self):
        """
        """
        global TARGET
        fitness = 0
        for i in range(self.get_size()):
            fitness += abs(ord(self.get_value()[i])-ord(TARGET[i]))
        self.set_score(fitness)

    def get_score(self):
        """
        """
        return self.__fitness

    def get_value(self):
        """
        """
        return self.__chromosome

    def mutate(self, probability):
        """
        apply mutation operation to self : each element of the genome
        sequence is randomly changed with given probabiliy

        side effect: self's genome is modified
        :param probability: (float) the probability of mutation for every gene
        :UC: probability in [0,1[

        """
        global TARGET
        assert 0 <= probability < 1, 'the probability must be between 0 and 1 excluded'

        for i in range(self.get_size()):
            if random() < probability:
                self.get_value()[i] = choice(LETTERS)

    def tournament(self, other):
        """
        perform a tournament between two individuals, the winner is the most fitted one, it is returned.
        :param first: (an Individual object) - an individual.
        :param second: (an Individual object) - an individual.
        :rtype: Individual object
        :return: the winner of the tournament
        """
        if self.get_score() < other.get_score():
            return self
        else:
            return other

    def sort_population(population):
        """
        sort population from best fitted to worst fitted individuals.
        Depending on the problem, it can correspond to ascending or descending
        order with respect to the fitness function.

        side effect: population is modified by this method.

        :param population: (list(Individual)) - the list of individuals to sort.
        """
        population.sort(key = lambda individual: individual.get_score())

    def cross_with(self, other):
        """
        perform a 1 point crossover between self and other,
        two new built individuals are returned

        :param other: (Individual) another individual

        """
        coupe_point = randint(1, self.get_size()//2)
        individu1 = self.copy()
        individu2 = other.copy()
        genome_list1 = individu1.get_value()[:]
        genome_list2 = individu2.get_value()[:]
        i=0
        while(i<coupe_point):
            genome_list1[i], genome_list2[i] = \
            genome_list2[i], genome_list1[i]
            i+=1
        individu1.set_value(genome_list1)
        individu2.set_value(genome_list2)
        return (individu1, individu2)


    def copy(self):

        """
        build a copy of self, the genome is a copy of self’s genome

        :return: a new individual which is a << clone >> of self
        :rtype: an Individual object

        """
        individual_copy = Individual(self.get_size())
        individual_copy.set_value(self.get_value()[:])
        return individual_copy


    def set_score(self, new_score):
        """
        change the fitness score of self

        :param new_score: (int) the new fitness score

        """
        self.__fitness = new_score

    def set_value(self, new_value):
        """
        change the genome value of self

        :param new_value: (list) the new genome value

        """
        self.__chromosome = new_value

    def best_individual(population):
        """
        return the best fitted individual from population.
        Depending on the problem, it can correspond to the individual
        with the highest or the lowest fitness value.

        :param population: list(Individual) the list of individuals to sort.
        :rtype: an Individual object
        :return: the best fitted individual of population.
        """
        best = population[0]
        min = best.get_score()
        for individu in population[1:]:
            fitness = individu.get_score()
            if fitness < min:
                best = individu
                min = fitness
        return best

    def __repr__(self):
        """
        """
        return '{}'.format("".join(self.get_value()))


def main():
    """
    define the main method that the problem will be resolved
    """
    global POPULATION_SIZE
    global TARGET
    individus = [Individual(len(TARGET)) for i in range(POPULATION_SIZE)]
    for individu in individus:
        individu.evaluate()
        print("{} {}".format(individu, individu.get_score()))
    print()
    print()
    Individual.sort_population(individus)
    i=0
    found = False
    while (i<600): #and not found):
        s = 5
        next_gen1 = []
        next_gen1 += individus[:s]
        s1 = POPULATION_SIZE-s
        next_gen2 = []
        individus_a_considerer = individus[:s][:]
        shuffle(individus_a_considerer)
        for j in range(0,s1-1,2):
            individu1, individu2 = individus_a_considerer[j%s],\
            individus_a_considerer[(j+1)%s]
            best_individu_tournoi = individu1.tournament(individu2)
            next_gen2.append(best_individu_tournoi)
            cross1, cross2 = individu1.cross_with(individu2)
            cross1.evaluate()
            cross2.evaluate()
            best_individu_cross = cross1.tournament(cross2)
            next_gen2.append(best_individu_cross)
        for individu in next_gen2:
            individu.mutate(0.1)
            individu.evaluate()

        next_gen = next_gen1+next_gen2
        Individual.sort_population(next_gen)
        individus = next_gen
        found = Individual.best_individual(individus).get_score()==0
        print("{} {}".format(Individual.best_individual(individus),i))
        print()
        i+=1
    print(i)
    res = Individual.best_individual(individus)
    print("{} {}".format(res, res.get_score()))
    return res


if __name__=='__main__':
    main()








