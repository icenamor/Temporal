#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features - Temporal issue"
__email__ = "icenamor@inf.uc3m.es"
import os               # path and process management
import sys              # argv, exit
from SATparse import SATStore
from SATFeature import SATFeature
def readFile(name, datos):
    try:
        fd = open(name,'r')
        datos = fd.readlines()
        fd.close()
    except:
        pass
    return datos

def joinFeatures(store, feature,folder  ,output):
    data = []
    print "\tISA::::", folder +"/" + str(feature.nameFile)
    data = readFile(folder +"/" +feature.nameFile, data)
    line_start = "RationofRelevantActions,NumberofActon,NumberofPropositions,NumberofRelevantActons,NumberofRelevantPropositions,VariablesEnd,propEnd,actionEnd,TotalMutexClauses,ratioEnd,TotalEventClauses,TotalClauses"
    if(len(data) > 0):
        line_start =  line_start + ",numberFiles," + data[0]
        values = store.satLine() + ","+ str(feature.NumberFiles) + "," +data[1]
    else:
        line_start =  line_start + ",numberFiles," +\
        "nvarsOrig,nclausesOrig,nvars,nclauses,reducedVars,reducedClauses,Pre-featuretime,vars-clauses-ratio,POSNEG-RATIO-CLAUSE-mean,POSNEG-RATIO-CLAUSE-coeff-variation,POSNEG-RATIO-CLAUSE-min,POSNEG-RATIO-CLAUSE-max,POSNEG-RATIO-CLAUSE-entropy,VCG-CLAUSE-mean,VCG-CLAUSE-coeff-variation,VCG-CLAUSE-min,VCG-CLAUSE-max,VCG-CLAUSE-entropy,UNARY,BINARY+,TRINARY+,Basic-featuretime,VCG-VAR-mean,VCG-VAR-coeff-variation,VCG-VAR-min,VCG-VAR-max,VCG-VAR-entropy,POSNEG-RATIO-VAR-mean,POSNEG-RATIO-VAR-stdev,POSNEG-RATIO-VAR-min,POSNEG-RATIO-VAR-max,POSNEG-RATIO-VAR-entropy,HORNY-VAR-mean,HORNY-VAR-coeff-variation,HORNY-VAR-min,HORNY-VAR-max,HORNY-VAR-entropy,horn-clauses-fraction,VG-mean,VG-coeff-variation,VG-min,VG-max,KLB-featuretime,CG-mean,CG-coeff-variation,CG-min,CG-max,CG-entropy,cluster-coeff-mean,cluster-coeff-coeff-variation,cluster-coeff-min,cluster-coeff-max,cluster-coeff-entropy,CG-featuretime,DIAMETER-mean,DIAMETER-coeff-variation,DIAMETER-min,DIAMETER-max,DIAMETER-entropy,DIAMETER-featuretime,cl-num-mean,cl-num-coeff-variation,cl-num-min,cl-num-max,cl-num-q90,cl-num-q10,cl-num-q75,cl-num-q25,cl-num-q50,cl-size-mean,cl-size-coeff-variation,cl-size-min,cl-size-max,cl-size-q90,cl-size-q10,cl-size-q75,cl-size-q25,cl-size-q50,cl-featuretime,SP-bias-mean,SP-bias-coeff-variation,SP-bias-min,SP-bias-max,SP-bias-q90,SP-bias-q10,SP-bias-q75,SP-bias-q25,SP-bias-q50,SP-unconstraint-mean,SP-unconstraint-coeff-variation,SP-unconstraint-min,SP-unconstraint-max,SP-unconstraint-q90,SP-unconstraint-q10,SP-unconstraint-q75,SP-unconstraint-q25,SP-unconstraint-q50,sp-featuretime,vars-reduced-depth-1,vars-reduced-depth-4,vars-reduced-depth-16,vars-reduced-depth-64,vars-reduced-depth-256,unit-featuretime,LP_OBJ,LPSLack-mean,LPSLack-coeff-variation,LPSLack-min,LPSLack-max,lpIntRatio,lpTIME,saps_BestSolution_Mean,saps_BestSolution_CoeffVariance,saps_FirstLocalMinStep_Mean,saps_FirstLocalMinStep_CoeffVariance,saps_FirstLocalMinStep_Median,saps_FirstLocalMinStep_Q.10,saps_FirstLocalMinStep_Q.90,saps_BestAvgImprovement_Mean,saps_BestAvgImprovement_CoeffVariance,saps_FirstLocalMinRatio_Mean,saps_FirstLocalMinRatio_CoeffVariance,ls-saps-featuretime,gsat_BestSolution_Mean,gsat_BestSolution_CoeffVariance,gsat_FirstLocalMinStep_Mean,gsat_FirstLocalMinStep_CoeffVariance,gsat_FirstLocalMinStep_Median,gsat_FirstLocalMinStep_Q.10,gsat_FirstLocalMinStep_Q.90,gsat_BestAvgImprovement_Mean,gsat_BestAvgImprovement_CoeffVariance,gsat_FirstLocalMinRatio_Mean,gsat_FirstLocalMinRatio_CoeffVariance,ls-gsat-featuretime,lobjois-mean-depth-over-vars,lobjois-log-num-nodes-over-vars,lobjois-featuretime\n"
        values = store.satLine() + ","+ str(feature.NumberFiles) + ","
        for i in range(138):
            values = values +"?,"
        values = values[:-1]
        
    fd = open(output,'w')
    fd.write(line_start)
    fd.write(values)
    fd.close()
    
    
if __name__ == '__main__':
    if (len(sys.argv) == 4):
        store = SATStore()
        fname = sys.argv[2] + "/" +sys.argv[1]
        print "fname\n", fname, "\n"
        if(os.path.isfile(fname)):
            store.getInformation(fname)
            feature = SATFeature()
            feature.readDirectory(sys.argv[2])
            print "file::", sys.argv[3]
            if(sys.argv[3].find(".csv")>=0):
                ##store.printFile(sys.argv[3])
                joinFeatures(store, feature, sys.argv[2],  sys.argv[3])
            else:
                ##store.printFile(sys.argv[3]+ ".csv")
                joinFeatures(store, feature, sys.argv[2], sys.argv[3]+ ".csv")

    else:
        print "Need the file SAT screem"
        print "./parse.py <cnf-parse-XXX> <folder> <output>"
