#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features - Temporal issue"
__email__ = "icenamor@inf.uc3m.es"
import os               # path and process management
import sys              # argv, exit
from Store import Store

def readFile(name, datos):
    fd = open(name,'r')
    datos = fd.readlines()
    fd.close()
    return datos

def writeFile(value, store, name):
    fd = open(name, 'w')
    fd.write(store.gethead()+"\n")
    fd.write(value)
    fd.close()

def countDurativeAction(domain, num_durative):
    string ="(:durative-action "
    for line in domain:
        line = line.strip()
        if line.find(string)>=0 and (line.find(";") < 0 or line.find(";") > len(line)/2):
            num_durative = num_durative + 1
    return num_durative

def getStadisticsAction(action):
    duration_type = -1 ## type = 0 - numeric type = 1 - function
    at_start_precondition = 0
    over_all_precondition = 0
    at_start_postcondition = 0
    at_end_postcondition = 0
    precondition = 0
    postcondition = 0
    name = ""
    total_duration = 0
    for line in action:
        if(line.find("(:durative-action ")>= 0):
            aux = line.strip()
            name = aux[18:].strip()
        if line.find(":condition")>= 0:
            precondition = 1
        if precondition == 1:
            if line.find("at start")>= 0:
                at_start_precondition = at_start_precondition + 1
            if line.find("over all")>= 0:
                over_all_precondition = over_all_precondition + 1
        if line.find(":effect")>= 0:
            precondition = 0
            postcondition = 1
        if postcondition == 1:
            if line.find("at start")>= 0:
                at_start_postcondition = at_start_postcondition + 1
            if line.find("at end")>= 0:
                at_end_postcondition = at_end_postcondition + 1
        if line.find(":duration")>= 0:
            n_o = line.find("?duration")
            linea = line[n_o+9:]
            n_o = linea.find(")")
            number = 0
            try:
                linea = linea[:n_o].strip()
                number = int(linea)
                duration_type = 0
                total_duration = total_duration  + number
            except:
                number = -1
                duration_type = 1
    return [name, duration_type, at_start_precondition, over_all_precondition, at_start_postcondition,at_end_postcondition, total_duration]
    
def getInformationProblem(problem):
    assignment = 0
    for line in problem:
        if(line.find("=")>=0):
            assignment = assignment + 1
    return assignment
            
def getInformationDomain(domain):
    actions = []
    string ="(:durative-action "
    value = 1
    newAction = []
    valuesActions = []
    for line in domain:
        if line.find(string)>=0  and (line.find(";") < 0 or line.find(";") > len(line)/2):
            value = 0
            if len(newAction) > 0:
                actions.append(newAction)
                valuesActions.append(getStadisticsAction(newAction))
            newAction = []
        if value == 0  and (line.find(";") < 0 or line.find(";") > len(line)/2) and len(line.strip()) > 0:
            newAction.append(line)
    actions.append(newAction)
    valuesActions.append(getStadisticsAction(newAction))
    return valuesActions

def getValueArity(domain):
    ##(:functions 
    functions = 0
    save = []
    for line in domain:
        if(line.find("(:functions ")>= 0):
            functions = 1
        elif(line.find("(:predicates")>= 0 or line.find("(:durative-action")>= 0 or line.find("(:types")>= 0):
            functions = 0
        if(functions == 1):
            line = line.strip()
            if (line.find(";") < 0 or line.find(";") > len(line)/2):
                save.append(line)
    funtions = 0
    tarity = 0
    max_arity =  float("-inf")
    min_arity = float("inf")
    for i in save:
        funtions = funtions + i.count(')')
        arity =  i.count('?')
        if(max_arity < arity):
            max_arity = arity
        if(min_arity > arity):
            min_arity = arity
        tarity = tarity + arity
    funtions = funtions - 1
    avg_arity = float(tarity) / funtions
    return [funtions, avg_arity, max_arity,min_arity]
if __name__ == '__main__':
    if (len(sys.argv) == 4):
        ##Because need the problem and the domain
        problem = []
        domain = []
        num_durative_actions = 0
        problem = readFile(sys.argv[2], problem)
        domain = readFile(sys.argv[1], domain)
        num_durative_actions = countDurativeAction(domain, num_durative_actions)
        stadistics = []
        stadistics = getInformationDomain(domain)
        store = Store()
        store.calculateStatistics(stadistics, num_durative_actions)
        store.assignment  = getInformationProblem(problem)
        news = getValueArity(domain)
        store.functions = news[0]
        store.avg_arity = news[1]
        store.min_arity = news[2]
        store.max_arity = news[3]
        value = store.getValues()
        ##print store.gethead()
        ##print value
        if(sys.argv[3].find(".csv")>= 0):
            writeFile(value, store, sys.argv[3])
        else:
            writeFile(value, store, sys.argv[3]+ ".csv")
        ##store.dump()
    else:
        print "Need more arguments ./parse.py <domain> <problem> <output>"
