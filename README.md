# Temporal
Features extraction for temporal domains

--------------
Temporal planning is a research discipline that addresses
the problem of generating a totally or a partially ordered
sequence of actions that transform the environment from
some initial state to a desired goal state, while taking into
account time constraints and actions' duration. For its ability to describe and address temporal constraints, 
temporal planning is of critical importance for a wide range of
real-world applications. Predicting the performance of temporal planners
 can lead to significant improvements in the
area, as planners can then be combined in order to boost
the performance on a given set of problem instances.
This paper investigates the predictability of the
state-of-the-art temporal planners by introducing a new
set of temporal-specific features and exploiting them for
generating classification and regression empirical performance models (EPMs) of considered planners.
 EPMs are also tested with regard to their ability to select the most
promising planner for efficiently solving a given temporal
planning problem.
Our extensive empirical analysis indicates that the
introduced set of features allows to generate EPMs that
can effectively perform algorithm selection, and the use of
EPMs is therefore a promising direction for improving the
state of the art of temporal planning, hence fostering the
use of planning in real-world applications.

---
This source code is done 2014:

Ubuntu 14.04 and gcc version
	python2.7


----
./plan <domainFile> <problemFile> <solutionFile>