#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features  - Temporal issue"
__email__ = "icenamor@inf.uc3m.es"
import math
# -----------------------------------------------------------------------------
## Class store the SAT screem of temporal domains and problems
# -----------------------------------------------------------------------------
class SATStore:
    def __init__(self):
        "store the values"
        self.RationofRelevantActions = -1
        self.NumberofActon =  -1
        self.NumberofPropositions = -1
        self.NumberofRelevantActons = -1
        self.NumberofRelevantPropositions = -1
        self.VariablesEnd = -1
        self.propEnd = -1
        self.actionEnd = -1
        self.TotalMutexClauses = -1
        self.ratio = -1
        self.TotalEventClauses = -1
        self.TotalClauses = -1    

    def dump(self):
        print self.RationofRelevantActions
        print self.NumberofActon
        print self.NumberofPropositions
        print self.NumberofRelevantActons 
        print self.NumberofRelevantPropositions
        print self.VariablesEnd
        print self.propEnd
        print self.actionEnd
        print self.TotalMutexClauses
        print self.ratio
        print self.TotalEventClauses
        print self.TotalClauses
        
    def getInformation(self, file_name):
        fd = open(file_name,'r')
        datos = fd.readlines()
        fd.close()
        for line in datos:
            line = line.strip()
            if(line.find("Ration of Relevant Actions: ")>=0):
                self.RationofRelevantActions = float(line[28:])
            if(line.find("Number of Actons: ")>= 0):
                index = line[18:].find("Number")
                aux = line[18:18+index].strip()
                self.NumberofActon = int(aux)
            if(line.find("Number of Propositions: ")>= 0):
                self.NumberofPropositions = int(line[(line.find("Number of Propositions: ")+24):])
            if(line.find("Number of Relevant Actons: ")>= 0):
                index = line[27:].find("Number")
                aux = line[27:27+index].strip()
                self.NumberofRelevantActons = int(aux)
            if(line.find("Number of Relevant Propositions: ")>= 0):
                self.NumberofRelevantPropositions = int(line[(line.find("Number of Relevant Propositions: ")+33):])
        ##PART TWO FILES
            if(line.find("Variables: total=")>=0):
                index = line.find("\t")
                aux = line[17:index].strip()
                self.VariablesEnd = int(aux)
            if(line.find("prop=")>=0):
                index = line[line.find("prop="):].find("\t")
                index = index + line.find("prop=")
                aux = line[line.find("prop=")+5:index]
                self.propEnd = int(aux)
            if(line.find("action= ")>=0):
                aux = line[line.find("action= ")+8:]
                self.actionEnd = int(aux)
            if(line.find("Total Mutex Clauses=")>=0):
                index = line.find("\t")
                aux = line[20:index].strip()
                self.TotalMutexClauses = int(aux)
            if(line.find("ratio=")>=0):
                aux = line[line.find("ratio=")+7:]
                self.ratio = float(aux)
            if(line.find("Total Event Clauses=")>=0):
                index = line.find("\t")
                aux = line[20:index].strip()
                self.TotalEventClauses = int(aux)
            if(line.find("Total Clauses=")>=0):
                aux = line[line.find("Total Clauses=")+14:]
                self.TotalClauses = int(aux)
    def printFile(self, name_file):
        fd = open(name_file,'w')
        line_start = "RationofRelevantActions,NumberofActon,NumberofPropositions,NumberofRelevantActons,NumberofRelevantPropositions,VariablesEnd,propEnd,actionEnd,TotalMutexClauses,ratioEnd,TotalEventClauses,TotalClauses\n"
        fd.write(line_start)
        values = str(self.RationofRelevantActions) + "," +str(self.NumberofActon) + "," +\
        str(self.NumberofPropositions) + "," +str(self.NumberofRelevantActons) + "," +\
        str(self.NumberofRelevantPropositions) + "," +str(self.VariablesEnd) + "," +\
        str(self.propEnd) + "," +str(self.actionEnd) + "," +str(self.TotalMutexClauses) + "," +\
        str(self.ratio) + "," +str(self.TotalEventClauses) + "," +str(self.TotalClauses)+ "\n"
        fd.write(values)
        fd.close()
    def satLine(self):
        values = str(self.RationofRelevantActions) + "," +str(self.NumberofActon) + "," +\
        str(self.NumberofPropositions) + "," +str(self.NumberofRelevantActons) + "," +\
        str(self.NumberofRelevantPropositions) + "," +str(self.VariablesEnd) + "," +\
        str(self.propEnd) + "," +str(self.actionEnd) + "," +str(self.TotalMutexClauses) + "," +\
        str(self.ratio) + "," +str(self.TotalEventClauses) + "," +str(self.TotalClauses)
        return values
