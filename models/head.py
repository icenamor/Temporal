#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Portfolio Project Features"
__email__ = "icenamor@inf.uc3m.es, 	I.Cenamor@hud.ac.uk"
# -----------------------------------------------------------------------------
## Class store the weka head
# -----------------------------------------------------------------------------
class Head:
    def __init__(self, list_head):	
        "store the Weka head"
        self.head = list_head
        self.set_values()
        
        
    def set_values(self):
        self.head.append("@relation problem\n\n")
        self.head.append("@attribute domain string\n")
        self.head.append("@attribute task_name string\n")
        self.head.append("@attribute requirements numeric\n")
        self.head.append("@attribute types numeric\n")
        self.head.append("@attribute objects numeric\n")
        self.head.append("@attribute predicates numeric\n")
        self.head.append("@attribute init numeric\n")
        self.head.append("@attribute goal numeric\n")
        self.head.append("@attribute actions numeric\n")
        self.head.append("@attribute axioms numeric\n")
        self.head.append("@attribute durative_actions numeric\n")
        self.head.append("@attribute axiom_counter numeric\n")
        self.head.append("@attribute function_symbols numeric\n")
        self.head.append("@attribute function_administrator numeric\n")
        self.head.append("@attribute generated_rules numeric\n")
        self.head.append("@attribute final_queue_length numeric\n")
        self.head.append("@attribute translator_variables numeric\n")
        self.head.append("@attribute translator_derived_variables numeric\n")
        self.head.append("@attribute translator_facts numeric\n")
        self.head.append("@attribute translator_operators numeric\n")
        self.head.append("@attribute mutex_key numeric\n")
        self.head.append("@attribute strips_to_sas numeric\n")
        self.head.append("@attribute ranges numeric\n")
        self.head.append("@attribute goal_list numeric\n")
        self.head.append("@attribute task_init numeric\n")
        self.head.append("@attribute translator_act numeric\n")
        self.head.append("@attribute translator_durative_act numeric\n")
        self.head.append("@attribute translator_axiom numeric\n")
        self.head.append("@attribute translator_num_axioms numeric\n")       
        self.head.append("@attribute translator_num_axioms_by_layer  numeric\n")
        self.head.append("@attribute translator_max_num_layer  numeric\n")
        self.head.append("@attribute translator_num_axiom_map numeric\n")
        self.head.append("@attribute translator_const_num_axioms numeric\n")
        self.head.append("@attribute translator_reachable numeric\n")      
        self.head.append("@attribute translator_groups numeric\n")
        self.head.append("@attribute translator_mutex_group numeric\n")
        self.head.append("@attribute translator_translation_key numeric\n") 
        
        
        self.head.append("@attribute numberVariablesCG numeric\n")
        self.head.append("@attribute highLevelVariablesCG numeric\n")     
        self.head.append("@attribute totalEdgesCG numeric\n")
        self.head.append("@attribute totalWeightCG numeric\n")
        self.head.append("@attribute veRatio numeric\n")
        self.head.append("@attribute weRatio numeric\n")
        self.head.append("@attribute wvRatio numeric\n")
        self.head.append("@attribute hvRatio numeric\n")
        self.head.append("@attribute inputEdgeCGMax numeric\n")
        self.head.append("@attribute inputEdgeCGAvg numeric\n")
        self.head.append("@attribute inputEdgeCGStd numeric\n")
        self.head.append("@attribute outputEdgeCGMax numeric\n")
        self.head.append("@attribute outputEdgeCGAvg numeric\n")
        self.head.append("@attribute outputEdgeCGStd numeric\n")
        self.head.append("@attribute inputWeightCGMax numeric\n")
        self.head.append("@attribute inputWeightCGAvg numeric\n")
        self.head.append("@attribute inputWeightCGStd numeric\n")
        self.head.append("@attribute outputWeightCGMax numeric\n")
        self.head.append("@attribute outputWeightCGAvg numeric\n")
        self.head.append("@attribute outputWeightCGStd numeric\n")
        self.head.append("@attribute inputEdgeHVMax numeric\n")
        self.head.append("@attribute inputEdgeHVAvg numeric\n")
        self.head.append("@attribute inputEdgeHVStd numeric\n")
        self.head.append("@attribute outputEdgeHVMax numeric\n")
        self.head.append("@attribute outputEdgeHVAvg numeric\n")
        self.head.append("@attribute outputEdgeHVStd numeric\n")
        self.head.append("@attribute inputWeightHVMax numeric\n")
        self.head.append("@attribute inputWeightHVAvg numeric\n")
        self.head.append("@attribute inputWeightHVStd numeric\n")
        self.head.append("@attribute outputWeightHVMax numeric\n")
        self.head.append("@attribute outputWeightHVAvg numeric\n")
        self.head.append("@attribute outputWeightHVStd numeric\n")
        self.head.append("@attribute numberVariablesDTG numeric\n")
        self.head.append("@attribute totalEdgesDTG numeric\n")
        self.head.append("@attribute totalWeigthDTG numeric\n")
        self.head.append("@attribute edVaRatioDTG numeric\n")
        self.head.append("@attribute weEdRatioDTG numeric\n")
        self.head.append("@attribute weVaRatioDTG numeric\n")
        self.head.append("@attribute inputEdgeDTGMax numeric\n")
        self.head.append("@attribute inputEdgeDTGAvg numeric\n")
        self.head.append("@attribute inputEdgeDTGStd numeric\n")
        self.head.append("@attribute outputEdgeDTGMax numeric\n")
        self.head.append("@attribute outputEdgeDTGAvg numeric\n")
        self.head.append("@attribute outputEdgeDTGStd numeric\n")
        self.head.append("@attribute inputWeightDTGMax numeric\n")
        self.head.append("@attribute inputWeightDTGAvg numeric\n")
        self.head.append("@attribute inputWeightDTGStd numeric\n")
        self.head.append("@attribute outputWeightDTGMax numeric\n")
        self.head.append("@attribute outputWeightDTGAvg numeric\n")
        self.head.append("@attribute outputWeightDTGStd numeric\n")
        
        self.head.append("@attribute avg_level numeric\n")
        self.head.append("@attribute avg_duration numeric\n")
        self.head.append("@attribute str_level numeric\n")
        self.head.append("@attribute str_duration numeric\n")
        self.head.append("@attribute global_num_type_start numeric\n")
        self.head.append("@attribute global_num_type_end numeric\n")
        self.head.append("@attribute global_num_type_compressed numeric\n")
        self.head.append("@attribute global_num_type_ax_red numeric\n")
        self.head.append("@attribute global_total_level numeric\n")
        self.head.append("@attribute global_min_level numeric\n")
        self.head.append("@attribute global_max_level numeric\n")
        self.head.append("@attribute global_total_duration numeric\n")
        self.head.append("@attribute global_min_duration numeric\n")
        self.head.append("@attribute global_max_duration numeric\n")
        self.head.append("@attribute planner string\n") ##TODO
        self.head.append("@attribute class {true,false}\n\n")
        self.head.append("@data\n\n")

