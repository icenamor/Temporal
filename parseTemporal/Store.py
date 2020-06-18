#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features  - Temporal issue"
__email__ = "icenamor@inf.uc3m.es"
import math
# -----------------------------------------------------------------------------
## Class store the stadistics of temporal domains and problems
# -----------------------------------------------------------------------------
class Store:
    def __init__(self):
        "store the values"
        self.assignment = -1
        self.name =  "no-name"
        self.durative_actions = -1
        self.type_numeric_duration = 0
        self.type_function_duration = 0
        
        ##types numeric funtions
        self.avg_numeric_duration = -1
        self.min_numeric_duration = float("inf")
        self.max_numeric_duration = float("-inf")
        
        
        ##arity of the funtions
        self.functions = 0
        self.avg_arity = -1
        self.min_arity = float("inf")
        self.max_arity = float("-inf")
        
        self.avg_at_start_precondition = -1.0
        self.min_at_start_precondition = float("inf")
        self.max_at_start_precondition = float("-inf")
        self.std_at_start_precondition = -1.0
        
        self.avg_over_all_precondition = -1.0
        self.min_over_all_precondition =  float("inf")
        self.max_over_all_precondition = float("-inf")
        self.std_over_all_precondition = -1.0
        
        self.avg_at_start_postcondition = -1.0
        self.min_at_start_postcondition = float("inf")
        self.max_at_start_postcondition = float("-inf")
        self.std_at_start_postcondition = -1.0
        
        self.avg_at_end_postcondition = -1.0
        self.min_at_end_postcondition = float("inf")
        self.max_at_end_postcondition = float("-inf")
        self.std_at_end_postcondition = -1.0
        
    def calculateStatistics(self, valuesActions, durative_actions):
        self.durative_actions = durative_actions
        total_at_start_precondition = 0
        total_over_all_precondition = 0
        total_at_start_postcondition = 0
        total_at_end_postcondition = 0
        total_duration = 0
        
        for value in valuesActions:
            if value[1] == 0:
                self.type_numeric_duration = self.type_numeric_duration + 1
            elif value[1] == 1:
                self.type_function_duration = self.type_function_duration + 1
            total_at_start_precondition = total_at_start_precondition + value[2]
            total_over_all_precondition = total_over_all_precondition + value[3]
            total_at_start_postcondition = total_at_start_postcondition + value[4]
            total_at_end_postcondition = total_at_end_postcondition + value[5]
            total_duration = total_duration + value[6]
            
            if(self.min_numeric_duration> value[6]):
                self.min_numeric_duration =  value[6]
            if(self.min_at_end_postcondition > value[5]):
                self.min_at_end_postcondition =  value[5]
            if(self.min_at_start_postcondition > value[4]):
                self.min_at_start_postcondition =  value[4]
            if(self.min_over_all_precondition > value[3]):
                self.min_over_all_precondition =  value[3]
            if(self.min_at_start_precondition > value[2]):
                self.min_at_start_precondition =  value[2]
        
            if(self.max_numeric_duration < value[6]):
                self.max_numeric_duration =  value[6]
            if(self.max_at_end_postcondition < value[5]):
                self.max_at_end_postcondition =  value[5]
            if(self.max_at_start_postcondition < value[4]):
                self.max_at_start_postcondition =  value[4]
            if(self.max_over_all_precondition < value[3]):
                self.max_over_all_precondition =  value[3]
            if(self.max_at_start_precondition < value[2]):
                self.max_at_start_precondition =  value[2]
                
        self.avg_numeric_duration = float(total_duration) /self.durative_actions
        self.avg_at_start_precondition = float(total_at_start_precondition)/self.durative_actions
        self.avg_over_all_precondition = float(total_over_all_precondition)/self.durative_actions
        self.avg_at_start_postcondition =  float(total_at_start_postcondition)/self.durative_actions
        self.avg_at_end_postcondition = float(total_at_end_postcondition)/self.durative_actions
        ##for std
        total_at_start_precondition = -1
        total_over_all_precondition = -1
        total_at_start_postcondition = -1
        total_at_end_postcondition = -1
        for value in valuesActions:
            total_at_start_precondition = total_at_start_precondition + pow(value[2]-self.avg_at_start_precondition,2 )
            total_over_all_precondition = total_over_all_precondition + pow(value[3]-self.avg_over_all_precondition,2)
            total_at_start_postcondition = total_at_start_postcondition + pow(value[4]-self.avg_at_start_postcondition,2)
            total_at_end_postcondition = total_at_end_postcondition + pow(value[5]-self.avg_at_end_postcondition, 2)
        if(total_at_start_precondition > 0):
            self.std_at_start_precondition = math.sqrt(float(total_at_start_precondition)/self.durative_actions)
        else:
            self.std_at_start_precondition = 0
        if(self.std_over_all_precondition > 0):
            self.std_over_all_precondition = math.sqrt(float(total_over_all_precondition)/self.durative_actions)
        else:
            self.std_over_all_precondition  = 0
        if(self.std_at_start_postcondition > 0):
            self.std_at_start_postcondition =  math.sqrt(float(total_at_start_postcondition)/self.durative_actions)
        else:
            self.std_at_start_postcondition = 0
        if(self.std_at_end_postcondition > 0):
            self.std_at_end_postcondition = math.sqrt(float(total_at_end_postcondition)/self.durative_actions)
        else:
            self.std_at_end_postcondition = 0
        
    def getValues(self):
        value = str(self.assignment) + "," + str(self.durative_actions)  + "," +\
        str(self.type_numeric_duration) + "," + str(self.type_function_duration) +\
        ","+str(round(self.avg_numeric_duration,4))+ ","+str(self.min_numeric_duration)+\
        ","+str(self.max_numeric_duration) +\
        ","+str(self.functions) +\
        ","+str(self.avg_arity) +\
        ","+str(self.min_arity) +\
        ","+str(self.max_arity) +\
        "," + str(round(self.avg_at_start_precondition,4)) + "," + str(self.min_at_start_precondition) +\
        "," + str(self.max_at_start_precondition) + "," + str(round(self.std_at_start_precondition,4)) +\
        "," + str(round(self.avg_over_all_precondition,4)) + "," + str(self.min_over_all_precondition) +\
        "," + str(self.max_over_all_precondition) + "," + str(round(self.std_over_all_precondition,4)) +\
        ","+ str(round(self.avg_at_start_postcondition,4)) + "," + str(self.min_at_start_postcondition) +\
        "," + str(self.max_at_start_postcondition) + "," + str(round(self.std_at_start_postcondition,4)) +\
        "," + str(round(self.avg_at_end_postcondition,4)) + "," + str(self.min_at_end_postcondition) +\
        "," + str(self.max_at_end_postcondition) + "," + str(round(self.std_at_end_postcondition,4))
        return value
    def gethead(self):
        value = "assignment,durative_actions,type_numeric_duration," +\
        "type_function_duration,avg_numeric_duration,min_numeric_duration," +\
        "max_numeric_duration,functions,avg_arity," +\
        "min_arity,max_arity,avg_at_start_precondition," +\
        "min_at_start_precondition,max_at_start_precondition," +\
        "std_at_start_precondition,avg_over_all_precondition," +\
        "min_over_all_precondition,max_over_all_precondition," +\
        "std_over_all_precondition,avg_at_start_postcondition," +\
        "min_at_start_postcondition,max_at_start_postcondition," +\
        "std_at_start_postcondition,avg_at_end_postcondition," +\
        "min_at_end_postcondition,max_at_end_postcondition,std_at_end_postcondition"
        return value
    def dump(self):
        print self.type_numeric_duration
        print self.type_function_duration
            
        print self.avg_at_start_precondition
        print self.min_at_start_precondition
        print self.max_at_start_precondition
        print self.std_at_start_precondition
            
        print self.avg_over_all_precondition
        print self.min_over_all_precondition
        print self.max_over_all_precondition
        print self.std_over_all_precondition
            
        print self.avg_at_start_postcondition
        print self.min_at_start_postcondition
        print self.max_at_start_postcondition
        print self.std_at_start_postcondition
            
        print self.avg_at_end_postcondition
        print self.min_at_end_postcondition
        print self.max_at_end_postcondition
        print self.std_at_end_postcondition

