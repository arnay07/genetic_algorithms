#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`problem` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 25/11/2019

"""

from random import *
from individual import *
import math
import operator
import sys

class Problem():
    def __init__(self, x_min, x_max):
        """
        Build a problem

        """
        self.__x_min = x_min
        self.__x_max = x_max

    def best_individual(self,population):
        """
        return the best fitted individual from population.
        Depending on the problem, it can correspond to the individual
        with the highest or the lowest fitness value.

        :param population: list(Individual) the list of individuals to sort.
        :rtype: an Individual object
        :return: the best fitted individual of population.
        """
        best = population[0]
        max = best.get_score()
        for individu in population[1:]:
            fitness = individu.get_score()
            if fitness > max:
                best = individu
                max = fitness
        return best

    def get_min(self):
        """
        returns the x_min
        """
        return self.__x_min

    def get_max(self):
        """
        returns the x_max of the problem
        """
        return self.__x_max

    def create_individual(self, size):
        """
        create a randomly generated indidivual for this problem.

        :rtype: an Individual object.
        :return: a randomly generated individual for this problem.
        """
        individu = Individual(size)
        individu.evaluate(self)
        return individu

    def evaluate_fitness(self,individual):
        """
        compute the fitness of individual for this problem.

        :param individual: (an Individual object) - the individual to consider.
        :rtype: an Individual object
        :return: the fitness of individual for this problem
        """
        #the formula is x = x_min+ n*((x_max-x_min)/n_max)
        #n is obtained by individual.calculate_N()
        #n_max is the max number on size bits

        n_max = 2**individual.get_size() - 1
        x = self.get_min()+ individual.calculate_N()*\
                ((self.get_max()-self.get_min())/n_max)
        return (x, x**2 * math.sin(x) * math.cos(x))

    def sort_population(self,population):
        """
        sort population from best fitted to worst fitted individuals.
        Depending on the problem, it can correspond to ascending or descending
        order with respect to the fitness function.

        side effect: population is modified by this method.

        :param population: (list(Individual)) - the list of individuals to sort.
        """
        population.sort(key = lambda individual: individual.get_score())


    def tournament(self,first,second):
        """
        perform a tournament between two individuals, the winner is the most fitted one, it is returned.
        :param first: (an Individual object) - an individual.
        :param second: (an Individual object) - an individual.
        :rtype: Individual object
        :return: the winner of the tournament
        """
        if first.get_score() > second.get_score():
            return first
        else:
            return second



def main():
    """
    define the main method that the problem will be resolved
    """
    problem = Problem(15,17)
    individus = [problem.create_individual(8) for i in range(100)]
    for individu in individus:
        print("{} {}".format(individu, individu.get_score()))
    print()
    print()
    for i in range(20):
        next_gen1 = []
        next_gen2 = []
        shuffle(individus)
        j=0
        while(j<99):
            individu1, individu2 = individus[j], individus[j+1]
            best_individu_tournoi = problem.tournament(individu1, individu2)
            next_gen1.append(best_individu_tournoi)
            cross1, cross2 = individu1.cross_with(individu2)
            cross1.evaluate(problem)
            cross2.evaluate(problem)
            best_individu_cross = problem.tournament(cross1, cross2)
            next_gen2.append(best_individu_cross)
            j+=2
        next_gen = next_gen1+next_gen2
        for individu in next_gen:
            individu.mutate(0.1)
            individu.evaluate(problem)
            print("{} {}".format(individu, individu.get_score()))
        print()
        problem.sort_population(next_gen)
        for individu in next_gen:
            print("{} {}".format(individu, individu.get_score()))
        print()
        meilleurs = next_gen[len(next_gen)-5:][:]
        next_gen = next_gen[5:][:]
        individus = next_gen+meilleurs
        for individu in individus:
            print("{} {}".format(individu, individu.get_score()))
        print()
        print()
    res = problem.best_individual(individus)
    print("{} {}".format(res, problem.evaluate_fitness(res)[0]))
    return res


if __name__=='__main__':
    main()
#    problem = Problem(13,18)
#    population = Population(10, 8)
#    individus = population.get_population()
#    for individu in individus:
#        individu.evaluate(problem)
#        print("{} {}".format(individu, individu.get_score()))
#    print()
#    problem.sort_population(individus)
#    for individu in individus:
#        print("{} {}".format(individu, individu.get_score()))
#

#
#






