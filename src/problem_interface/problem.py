#!/usr/bin/python3
# -*- coding: utf-8 -*-


from random import *


class Problem_Interface(object):


    def __init__(self):
        """
        build a problem interface that will need to be adressed by the individuals
        of our population

        """
        pass



    def best_individual(self, population):
        """
        return the best fitted individual from population. 
        Depending on the problem, it can correspond to the individual 
        with the highest or the lowest fitness value.
        

        :param population:(list(Individual)) the list of individuals to sort
        :return: the best fitted individual of population
        :rtype: Individual

        """

        pass


    def create_individual(self):
        """ 
        create a randomly generated indidivual for this problem
        
        :return: a randomly generated individual for this problem
        :rtype: Individual

        """

