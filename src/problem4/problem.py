#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`problem` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 07/12/2019

"""

from random import *
from individual import *
from haunted_field import *
import math
import operator
import sys





SCORES = {"M":1, " ":0, "*":2, '.':0}

class Problem():
    def __init__(self, width, height, nb_monsters):
        """
        Build a problem

        """
        self.__height = height
        self.__width = width
        self.__field = Haunted_Field(height,width)
        self.__field.init_monsters(nb_monsters)
        

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
            # if 1<=case[0]<field.get_width()+2 and 1<=case[1]<field.get_height()+2:
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
        step = 0
        fieldline = 1
        nb_used = 1
        while (1 <= fieldline <field.get_height() and (1, 1) <=individual.get_position()\
               <=(field.get_height(), field.get_width()) and \
               individual.get_state()!=IndividualState.monster\
               and individual.get_state()!=IndividualState.blocked \
                   and individual.get_state()!= IndividualState.alive):
            score = self.get_motif(individual)
            move = individual.get_value()[score]
            x,y = individual.get_position()
            if move=='U':
                line = y+1
                column = x
                fieldline -= 1
            elif move=='L':
                line = y
                column = x-1
            elif move=='D':
                line = y-1
                column = x
                fieldline += 1
                if fieldline == field.get_height()+1:
                    individual.set_state(IndividualState.success)
            elif move=='R':
                line = y
                column = x+1      
                
            individual.set_position(column, line)
            
            if field.is_monster(line, column):
                individual.set_state(IndividualState.monster)
            elif field.is_obstacle(line, column):
                individual.set_state(IndividualState.blocked)
            elif field.is_empty(line, column):
                step += 1
                if step == (field.get_height()*field.get_width())//2:
                    individual.set_state(IndividualState.alive)
                field.set_cell(line, column, '.')
                nb_used += 1
            else:
                step += 1
                if step == (field.get_height()*field.get_width())//2:
                    individual.set_state(IndividualState.alive)
            
        scoreindividu = nb_used + fieldline * field.get_width()
        if individual.get_state()==IndividualState.monster:
            scoreindividu += (field.get_height() - fieldline) * 20
        elif individual.get_state()==IndividualState.success:
            scoreindividu += (field.get_width()*field.get_height - nb_used) * 10
        elif individual.get_state()==IndividualState.blocked:
            scoreindividu += (field.get_height() - fieldline) * 2
            
        return scoreindividu
        
        

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
    problem = Problem(16,16, 2)
    field = problem.get_field()
    print(field)
    population_size = field.get_height()*field.get_width()//2
    individus = [problem.create_individual() for i in range(population_size)]
    for individu in individus:
        print("{} {}".format(individu, individu.get_score()))
    print()
    print()
    for i in range(50):
        next_gen1 = []
        next_gen2 = []
        shuffle(individus)
        j=0
        while(j<population_size-1):
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
            individu.mutate(0.05)
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
    print("{} {}".format(res, problem.evaluate_fitness(res)))
    print(field)
    return res



if __name__=='__main__':
    main()
    # problem = Problem(7,7, 3)
    # field = problem.get_field()
    # print(field)
    # individu = problem.create_individual()
    # # population_size = field.get_height()*field.get_width()//2
    # # individus = [problem.create_individual() for i in range(5)]
    # # for individu in individus:
    # #     print("{} {}".format(individu, individu.get_score()))
    # # individu.evaluate(problem)
   
    
    