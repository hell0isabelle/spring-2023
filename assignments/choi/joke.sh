JOKE=$(curl -sS https://icanhazdadjoke.com | tail -n 1)

echo "$JOKE"
echo
exit 0
