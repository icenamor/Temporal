BASEDIR="$(dirname "$0")"
if [ $# != 3 ] ; then
    echo "Usage: plan <domainFile> <problemFile> <solutionFile>"
else

    domain2="${1##*/}"
    problem2="${2##*/}"
    echo "estoy aqui" "$domain2", "$problem2"
    domain="${domain2%.*}"
    problem="${problem2%.*}"
    echo "$domain" "$problem"
    ##echo 
    ulimit -t 20; ulimit -v 2097152; ./tempo-sat-itsat/plan $domain2 $problem2 -cnf -t1 2 -t2 2 -limit 10 -dontsolve > cnf-$domain-$problem-$3
    echo "finish part1"
   ## ulimit -t 20;./parseTemporal/parse.py $1 $2 temporal-PDDL-"$3"-$problem
    echo "finish part2"
    ulimit -t 10; ulimit -v 2097152;./SATparse/parse.py  cnf-$domain-$problem-$3 . features-SAT-$domain-$problem-$3
    echo "finish part3"
    rm cnf-$domain-$problem-$3
    rm *.cnf
    rm *.xls
   	##ulimit -t 50;./plan $1 $2 $3
    ##echo "Features extract"
    ##./models/join3Files.py $BASEDIR temporal-PDDL-"$3"-$problem  $3-$domain-$problem.arff
    ./cleanOutput.sh
fi
