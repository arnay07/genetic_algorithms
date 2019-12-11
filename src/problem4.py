#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`problem4` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 07/12/2019

"""

from random import *
from individual4 import *
from haunted_field import *
import math
import operator
import sys
from algogen import *





SCORES = {"M":1, " ":0, "*":2, '.':0}

class Problem():
    def __init__(self, width, height, nb_monsters):
        """
        Build a problem

        """
        self.__height = height
        self.__width = width
        self.__field= Haunted_Field(height,width)
        self.__field.init_monsters(nb_monsters)
        self.__fields = [Haunted_Field(height,width) for _ in range(20)]
    
        


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

    def get_height(self):
        """
        returns the x_min
        """
        return self.__height

    def get_width(self):
        """
        returns the x_max of the problem
        """
        return self.__width

    def get_field(self):
        return self.__field
    
    def get_fields(self):
        return self.__fields
    

    def get_motif(self, individu):
        """
        return the motif of an individual

        Parameters
        ----------
        individu : Individual
            individual in the field

        Returns
        -------
        string

        """
        res = ""
        score = 0
        field = self.get_field()
        y, x = individu.get_position()
        cases = [(y, x-1), (y+1,x-1), (y+1,x), (y+1,x+1), (y,x+1)]
        for case in cases:
            cell = field.get_cell(case[0], case[1])
            res += cell
        score = SCORES[res[0]]*3**0+SCORES[res[1]]*3**1+SCORES[res[2]]*3**2+\
            SCORES[res[3]]*3**3+SCORES[res[4]]*3**4

        return score

    def create_individual(self):
        """
        create a randomly generated indidivual for this problem.

        :rtype: an Individual object.
        :return: a randomly generated individual for this problem.
        """
        field = self.get_field()
        individu = Individual(1, self.get_width()//2+1)
        field.set_cell(1, self.get_width()//2+1, '.')
        return individu

    def evaluate_fitness(self,individual):
        """
        compute the fitness of individual for this problem.

        :param individual: (an Individual object) - the individual to consider.
        :rtype: an Individual object
        :return: the fitness of individual for this problem
        """
        field = self.get_field()
        field.backup_field()
        step = 0
        fieldline = 1
        nb_used = 1
        # print('start nb_used count\n')
        while (1 <= fieldline <= self.get_height() and 1 <= individual.get_position()[0]\
                <= self.get_height() and 1 <= individual.get_position()[1] <= self.get_width()\
                and individual.get_state() == IndividualState.start):

            score = self.get_motif(individual)
            move = individual.get_value()[score]
            y, x = individual.get_position()
            if move=='U':
                line = y-1
                column = x
                fieldline -= 1
            elif move=='L':
                line = y
                column = x-1
            elif move=='D':
                line = y+1
                column = x
                fieldline += 1
                if fieldline == self.get_height():
                    individual.set_state(IndividualState.success)
            elif move=='R':
                line = y
                column = x+1

            individual.set_position(line, column)

            if field.is_monster(line, column):
                individual.set_state(IndividualState.monster)
            elif field.is_obstacle(line, column):
                individual.set_state(IndividualState.blocked)
            elif field.is_empty(line, column):
                step += 1
                if step == (self.get_height()*self.get_width())//2:
                    # print('alive')
                    individual.set_state(IndividualState.alive)              
                field.set_cell(line, column, '.')
                nb_used += 1
                # print('{}\n'.format(nb_used))
            elif field.is_used(line, column):
                step += 1
                if step == (self.get_height()*self.get_width())//2:
                    # print('alive')
                    individual.set_state(IndividualState.alive)

        # print('{} {}\n'.format(nb_used, fieldline))
        
        scoreindividu = nb_used + fieldline * self.get_width()
        
        if individual.get_state()==IndividualState.monster:
            # print("monster")
            scoreindividu += (self.get_height() - fieldline) * 20
        elif individual.get_state()==IndividualState.success:
            # print('success')
            scoreindividu += (self.get_width()*self.get_height() - nb_used) * 10
        elif individual.get_state()==IndividualState.blocked:
            # print('blocked')
            scoreindividu += (self.get_height() - fieldline) * 2
            
        
        individual.set_state(IndividualState.start)
        individual.set_position(1, self.get_width()//2+1)
        individual.set_fieldline(fieldline)
        
    
        # print('{} {}\n'.format(individual, scoreindividu))
        field.restore_field()
        # print(field)
        
        return scoreindividu
    
    
    
    def evaluate_print_field(self, individual, field):
        
        champs_traverses = 0
        
        field.backup_field()
        step = 0
        fieldline = 1
        nb_used = 1
        # print('start nb_used count\n')
        while (1 <= fieldline <= self.get_height() and 1 <= individual.get_position()[0]\
               <= self.get_height() and 1 <= individual.get_position()[1] <= self.get_width()\
               and individual.get_state() == IndividualState.start):

            score = self.get_motif(individual)
            move = individual.get_value()[score]
            y, x = individual.get_position()
            if move=='U':
                line = y-1
                column = x
                fieldline -= 1
            elif move=='L':
                line = y
                column = x-1
            elif move=='D':
                line = y+1
                column = x
                fieldline += 1
                if fieldline == self.get_height():
                    individual.set_state(IndividualState.success)
                    champs_traverses += 1
            elif move=='R':
                line = y
                column = x+1

            individual.set_position(line, column)

            if field.is_monster(line, column):
                individual.set_state(IndividualState.monster)
            elif field.is_obstacle(line, column):
                individual.set_state(IndividualState.blocked)
            elif field.is_empty(line, column):
                step += 1
                if step == (self.get_height()*self.get_width())//2:
                    # print('alive')
                    individual.set_state(IndividualState.alive)              
                field.set_cell(line, column, '.')
                nb_used += 1
                # print('{}\n'.format(nb_used))
            elif field.is_used(line, column):
                step += 1
                if step == (self.get_height()*self.get_width())//2:
                    # print('alive')
                    individual.set_state(IndividualState.alive)

        # print('{} {}\n'.format(nb_used, fieldline))
        
        scoreindividu = nb_used + fieldline * self.get_width()
        
        if individual.get_state()==IndividualState.monster:
            # print("monster")
            scoreindividu += (self.get_height() - fieldline) * 20
        elif individual.get_state()==IndividualState.success:
            # print('success')
            scoreindividu += (self.get_width()*self.get_height() - nb_used) * 10
        elif individual.get_state()==IndividualState.blocked:
            # print('blocked')
            scoreindividu += (self.get_height() - fieldline) * 2
            
        
        individual.set_state(IndividualState.start)
        individual.set_position(1, self.get_width()//2+1)
        individual.set_fieldline(fieldline)
        
        print(field)
        # print('{} {}\n'.format(individual, scoreindividu))
        field.restore_field()
        # print(field)
        
        return champs_traverses
    
            
            



    def sort_population(self,population):
        """
        sort population from best fitted to worst fitted individuals.
        Depending on the problem, it can correspond to ascending or descending
        order with respect to the fitness function.

        side effect: population is modified by this method.

        :param population: (list(Individual)) - the list of individuals to sort.
        """
        population.sort(key = lambda individual: individual.get_fieldline())


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
    hauteur = int(sys.argv[3])
    largeur = int(sys.argv[4])
    population_size = int(sys.argv[1])
    nb_monstres = int(sys.argv[2])
    crossover_rate = int(sys.argv[5])
    probability = float(sys.argv[6])
    problem = Problem(largeur, hauteur, nb_monstres)
    population = [problem.create_individual() for i in range(population_size)]
    for individu in population:
        individu.evaluate(problem)
    
    field = problem.get_field()
    algo = AlgoGen(problem, 243,  population_size, crossover_rate, probability)
    best = algo.action_on_population(population)
    
    problem.evaluate_print_field(best, field)
    
    champs_traverses = 0
    for _ in range(20):
        problem_experience = Problem(largeur, hauteur, nb_monstres)
        field_experience = problem_experience.get_field()
        champs_traverses += problem_experience.evaluate_print_field(best, field_experience)
         
        
    print(champs_traverses)
    



if __name__=='__main__':
    main()



