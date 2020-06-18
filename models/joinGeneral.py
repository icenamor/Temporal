#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Temporal Portfolio Project Features"
__email__ = "icenamor@inf.uc3m.es, 	I.Cenamor@hud.ac.uk"

import sys
import string
import os

##PDDL-domain-p01-crewplanning --> Parse temporal
##domain-p01.arff --> Preprocess-tranlate-process
def readFile(name):
    fd = open(name,'r')
    datos = fd.readlines()
    fd.close()
    return datos

def splitWekaFormat(FD):
    head = []
    body = []
    control = 0
    for line in FD:
        if(line.find("@data")>=0):
            control = 1
        if(control == 0):
            if (len(line) > 2):
                head.append(line)
        if(control == 1):
            if (len(line) > 2):
                body.append(line)
    return [head, body]

def changeWekaHead(dataOne, ntype):
    headNew = []
    attributes =  dataOne.split(',')
    for i in attributes:
        name = "@attribute " +str(ntype)+ "_"+ str(i.strip()) + "  numeric\n"
        headNew.append(name)
    return headNew
    
def appendValues(values, source):
     att_value =  source.split(',')
     for val in att_value:
        if(val.find("-inf")>=0 or val.find("inf")>=0):
            values.append(-1)
        elif(val.find(".00")>= 0):
            values.append(int(val[:val.find(".")]))
        elif(val.find("0.0")>=0):
            values.append(0)
        elif(val.find(".")>= 0):
            values.append(round(float(val),4))
        else:
            values.append(val)
     return values

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    if(len(sys.argv) == 5):
        PDDL = readFile(sys.argv[1])
       ## SAT = readFile(sys.argv[2])
        FD =  readFile(sys.argv[2])
        weka = splitWekaFormat(FD)
        values = []
        head1 = changeWekaHead(PDDL[0], "PDDL")
      ##  head2 = changeWekaHead(SAT[0], "SAT")
        weka[0].pop()
        weka[0].pop()
        values = appendValues(values, weka[1][1])
        values.pop()
        values.pop()
        values = appendValues(values, PDDL[1])
        values = appendValues(values, SAT[1])
        name_output = (sys.argv[3])
        if(name_output.find(".arff")< 0):
            name_output = name_output  + ".arff"
        fd = open(name_output, 'w')
        for i in weka[0]:
            fd.write(i)
        for i in head1:
            fd.write(i)
        fd.write("\n@data\n\n")
        generalValues = ""
        for i in values:
            generalValues = generalValues + str(i) + ","
        generalValues = generalValues[:-1]
        fd.write(generalValues)
        fd.close()
    else:
        print "./joinGeneral.py <PDDL> <FD> <output>"
        sys.exit(-1)

