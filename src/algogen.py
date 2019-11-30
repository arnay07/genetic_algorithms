#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`algogen` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité

:date: 14/11/2019

"""


import sys


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
        self.__problem = problem
        self.__population_size = population_size
        self.__crossover_rate = crossover_rate
        self.__mutation_probability = mutation_probability

    def get_problem(self):
        """
        return the genetic algorithm's problem
        """
        return self.__problem

    def get_population_size(self):
        """
        return the population size
        """
        return self.__population_size

    def get_crossover_rate(self):
        """
        return the crossover rate
        """

        return self.__crossover_rate

    def get_mutation_probability(self):
        """
        return the mutation probability
        """

        return self.__mutation_probability

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
