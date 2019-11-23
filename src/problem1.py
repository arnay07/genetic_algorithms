#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`problem1` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 2019, November 

"""

from random import *
from individual1 import *



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
        
        









    def sort_population(self,population):
        """
        sort population from best fitted to worst fitted individuals. 
        Depending on the problem, it can correspond to ascending or descending 
        order with respect to the fitness function.
        
        side effect: population is modified by this method.
        
        :param population: (list(Individual)) - the list of individuals to sort.
        """
        pass










    def tournament(self,first,second):
        """
        perform a rounament between two individuals, the winner is the most fitted one, it is returned.
        :param first: (an Individual object) - an individual.
        :param second: (an Individual object) - an individual.
        rtype: Individual object
        :return: the winner of the tournament
        """
        pass
    
        
        
    
        
        
