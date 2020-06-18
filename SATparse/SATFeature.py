#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features  - Temporal issue"
__email__ = "icenamor@inf.uc3m.es"
import os               # path and process management
import sys              # argv, exit
# -----------------------------------------------------------------------------
## Class store the SAT Features of temporal domains and problems
# -----------------------------------------------------------------------------
class SATFeature:
    def __init__(self):
        "store the values"
        self.NumberFiles = -1
        self.nameFile = -1

    def dump(self):
        print self.NumberFiles
        print self.nameFile
    
    def readDirectory(self, name):
        if(os.path.isdir(name)):
            dirs = os.listdir(name)
            cont = 0
            # This would print all the files and directories
            final_name = ""
            for n in dirs:
                 if (n.find(".cnf")>=0):
                    cont = cont + 1
                    if(n.find("all")>= 0):
                        final_name = n
            print "final cont: ", cont/2, final_name
            self.NumberFiles = cont/2
            self.nameFile = final_name
        else:
            print "Error there is not a directory to check"
