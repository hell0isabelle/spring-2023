
# This script downloads and prints a joke from the public site "https://icanhazdadjoke.com"
# To run this file, type ./joke.sh from this folder. 

JOKE=$(curl -sS https://icanhazdadjoke.com | tail -n 1)

echo "$JOKE"
echo
exit 0
