#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`algoGen` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité

:date: 14/11/2019

"""


class AlgoGen(object):


    def __init__(self, problem, population_size, crossover_rate, mutation_probability):
        """
        build a genetic algorithm to solve problem using a population of size population_size 
        and a probability of mutation of mutation_probability

        :param problem:(Problem object) the problem to solve
        :param population_size:(int) the size of the population (must be even)
        :param mutation_probability:(float) the mutation probability
        :param crossover_rate: the crossover rate
        :UC: population_size must be even and mutation_probability must be >= 0 and <1

        """
