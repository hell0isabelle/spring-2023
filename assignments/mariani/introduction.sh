#!/bin/bash
#this script gives you a message
# To run this file, type ./joke.sh from this folder. 
JOKE=$(curl -sS https://icanhazdadjoke.com | tail -n 1)

echo "$JOKE"
echo
exit 0
