#!/bin/bash

modified_file=$(git ls-files -m | awk 'NR == 1') ;

git diff $modified_file;