#! /usr/bin/env python
# -*- coding: utf-8 -*-
##Extract Selection Process -- Temporal
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Temporal Portfolio Project Features"
__email__ = "icenamor@inf.uc3m.es"

import sys
import string
import os

from head import Head
##translateFile --> translate
##features.arff --> preprocess
def readFile(name):
	fd = open(name,'r')
	linea = fd.readlines()
	return linea[len(datos)-1]

def writeFile(name, data, head):
	fd = open(name,'w')
	for i in head.head:
		fd.write(i)
	for i in data:
		fd.write(i)
	fd.close()

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    if(len(sys.argv) == 3):
        print sys.argv, os.path.basename(sys.argv[1]), sys.argv[1]
        pathname = os.path.basename(sys.argv[1])
        print pathname
        problems = os.listdir(pathname)
        featuresProblems = []
        head = Head([])
        for l in problems:
            if l.find(".arff")>=0:
                datos = []
                name = pathname + "/" + l
                datos = readFile(name)
                featuresProblems.append(datos)
        if sys.argv[2].find(".arff")>=0:
            writeFile(sys.argv[2], featuresProblems, head)
        else:
            n_file = sys.argv[2] + ".arff"
            writeFile(n_file, featuresProblems, head)
    else:
        print "Error: Number of parameters wrong"
        sys.exit(-1)

