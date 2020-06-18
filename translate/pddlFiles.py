#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Isabel Cenamor"
__copyright__   = "Copyright 2014, Temporal Portfolio Project -- Features translate"
__email__ = "icenamor@inf.uc3m.es"

##Create file with features
class PddlFile(object):
	def __init__(self, domain_name, task_name, requirements, types, objects, predicates, init, goal, actions, axioms):
	    ##Previous version		self.strips_to_sas = -1
		self.ranges = -1
		self.goal_list = -1 
		self.task_init = -1
		self.act = -1
		self.durative_Act = -1
		self.axi = -1
		self.num_axioms = -1
		self.num_axioms_by_layer = -1
		self.max_num_layer = -1 
		self.num_axiom_map = -1
		self.const_num_axioms = -1
		self.reachable = -1
		self.groups = -1
		self.mutex_group = -1
		self.translation_key = -1
		
		self.domain_name = domain_name
		self.task_name = task_name
		self.requirements = requirements
		self.types = types
		self.objects = objects
		self.predicates = predicates
		self.init = init
		self.goal = goal
		self.actions = actions
		self.axioms = axioms
		self.durative_actions = -1
		self.axiom_counter =-1
		self.function_symbols = -1
		self.function_administrator = -1
		self.generated_rules = -1
		self.final_queue_length  = -1
		self.translator_variables = -1
		self.translator_derived_variables =  -1
		self.translator_facts =  -1
		self.translator_operators = -1
		self.mutex_key = -1
        
		
	def printObject(self, name):
		f = open(name, "w")
		values = str(self.domain_name) + "," + str(self.task_name) + "," +  str(self.requirements) + "," + \
		str(self.types) + "," + str(self.objects) + "," +  str(self.predicates) + "," + \
		str(self.init) + "," +  str(self.goal) + "," + \
		str(self.actions) + "," + str(self.axioms) + "," +\
		str(self.durative_actions) + "," +\
		str(self.axiom_counter) + "," + \
		str(self.function_symbols) + "," + \
		str(self.function_administrator) + "," + \
		str(self.generated_rules) + "," +\
		str(self.final_queue_length ) + "," + \
		str(self.translator_variables) + "," + str(self.translator_derived_variables) + "," + \
		str(self.translator_facts) + "," + \
		str(self.translator_operators) + "," +\
		str(self.mutex_key) + "," +str(self.strips_to_sas) + "," +\
		str(self.ranges) + "," +str(self.goal_list) + ","+str(self.task_init) +\
	    "," +str(self.act) + "," +str(self.durative_Act) + "," +str(self.axi) +\
	    "," +str(self.num_axioms)+ ","+str(self.num_axioms_by_layer) + "," +\
	    str(self.max_num_layer)+","+ str(self.num_axiom_map) + "," +\
	    str(self.const_num_axioms) + "," +str(self.reachable) + "," +\
	    str(self.groups) + "," +str(self.mutex_group) + "," +str(self.translation_key)
		
		f.write(values)
		f.close()
	
	def printObjectSimply(self, name):
		f = open(name, "w")
		values = str(self.types) + "," + str(self.objects) +"," + \
		str(self.goal) + "," + \
		str(self.translator_facts)
		f.write(values)
		f.close()
	
			
	def dump(self):
		values = str(self.domain_name) + "," + str(self.task_name) + "," +  str(self.requirements) + "," + \
		str(self.types) + "," + str(self.objects) + "," +  str(self.predicates) + "," + \
		str(self.init) + "," +  str(self.goal) + "," + \
		str(self.actions) + "," + str(self.axioms) + "," +\
		str(self.durative_actions) + "," +\
		str(self.axiom_counter) + "," + \
		str(self.function_symbols) + "," + \
		str(self.function_administrator) + "," + \
		str(self.generated_rules) + "," +\
		str(self.final_queue_length ) + "," + \
		str(self.translator_variables) + "," + str(self.translator_derived_variables) + "," + \
		str(self.translator_facts) + "," + \
		str(self.translator_operators) + "," +\
		str(self.mutex_key) + "," +str(self.strips_to_sas) + "," +\
		str(self.ranges) + "," +str(self.goal_list) + ","+str(self.task_init) +\
	    "," +str(self.act) + "," +str(self.durative_Act) + "," +str(self.axi) +\
	    "," +str(self.num_axioms)+ ","+str(self.num_axioms_by_layer) + "," +\
	    str(self.max_num_layer)+","+ str(self.num_axiom_map) + "," +\
	    str(self.const_num_axioms) + "," +str(self.reachable) + "," +\
	    str(self.groups) + "," +str(self.mutex_group) + "," +str(self.translation_key)

		print(values)
		
	def dumpSimply(self):
		values = str(self.types) + "," + str(self.objects) +"," + \
		str(self.goal) + "," + \
		str(self.translator_facts)
		print(values)
