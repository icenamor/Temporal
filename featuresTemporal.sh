#! /bin/bash
BASEDIR="$(dirname "$0")"
if [ $# != 3 ] ; then
    echo "Usage: plan <domainFile> <problemFile> <solutionFile>"
else
    domain=0;
    read -a domain_list <<< `ls $1`
    mkdir $3-csv
    mkdir $3
    for problem in $(ls $2); do
        cp "$2"/"$problem" "$BASEDIR"
        tLen=${#domain_list[@]}
        echo "$tLen"
        if [ $tLen = 1 ]; then
            echo "one domain " "$1"/"${domain_list[$domain]}"
            cp "$1"/"${domain_list[$domain]}" "$BASEDIR"
            echo "${domain_list[$domain]}" "$problem" "$3"
            ./featuresUnique.sh "${domain_list[$domain]}" "$problem" "$3"
            echo "here"
        else
            echo "more than domain " "$2"/"${domain_list[$domain]}"
            cp "$1"/"${domain_list[$domain]}" "$BASEDIR"
            ./featuresUnique.sh "${domain_list[$domain]}" $problem $3
            domain=`expr $domain + 1`
        fi
    done
    mv *.csv $3-csv
    mv *.arff $3
    rm *.PDDL
    ##rm *.csv
fi

