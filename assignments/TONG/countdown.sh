#!/bin/bash

# this script will iterate 10 times from a for loop and print all values of the variable counter in a single line
# the counter variable will decrement once in each iteration, from 10 to 1

# to run this file, type ./countdown.sh from this folder
# ./countdown.sh is located in the TONG folder


for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"

# Date : February 22, 2023 at 3:10PM
