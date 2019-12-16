#!/bin/bash

branch_name=$(git branch | grep '*' | awk '{printf "%s", $2}');

printf $branch_name | pbcopy;

printf "Copied current git branch name '$branch_name' to clipboard. \n"