#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`problem1` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 25/11/2019

"""

from random import *
from individual1 import *
import math
import operator

class Problem1():
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
        max = 0
        for individu in population:
            fitness = self.evaluate_fitness(individu)
            if fitness > max:
                res = individu
                max = fitness
        return res

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
        individu = Individual1(size)
        individu.init_value()

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
                ((self.get_max()-self.get_min())//n_max)
        return x**2 * math.sin(x) * math.cos(x)

    def sort_population(self,population):
        """
        sort population from best fitted to worst fitted individuals.
        Depending on the problem, it can correspond to ascending or descending
        order with respect to the fitness function.

        side effect: population is modified by this method.

        :param population: (list(Individual)) - the list of individuals to sort.
        """
        dict_fitnesses = {}
        fitnesses = []
        for individu in population:
            fitness = self.evaluate_fitness(individu)
            dict_fitnesses[individu] = fitness

        sorted_fitness = sorted(dict_fitnesses.items(), key=\
                operator.itemgetter(1))

        for i in range(len(population)):
            population[i] = sorted_fitness[i][0]

    def tournament(self,first,second):
        """
        perform a tournament between two individuals, the winner is the most fitted one, it is returned.
        :param first: (an Individual object) - an individual.
        :param second: (an Individual object) - an individual.
        :rtype: Individual object
        :return: the winner of the tournament
        """
        first_fitness = self.evaluate_fitness(first)
        second_fitness = self.evaluate_fitness(second)
        if first_fitness > second_fitness:
            return first
        else:
            return second
