#!/bin/bash

modified_file=$(git ls-files -m | awk "NR == ${1}") ;

git add $modified_file;

printf "Staged modified file '$modified_file' \n"