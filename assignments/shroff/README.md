# Tic Tac Toe Game
The Tic Tac Toe game is a two-player game played on a 3x3 grid. 
Players take turns marking an empty cell on the grid with their symbol (X or O). 
The first player to get three of their symbols in a row, either horizontally, vertically, or diagonally, wins the game. 
If all cells are filled and no player has won, the game ends in a tie.

## Script Description
The `tic-tac-toe.py` script is a Python implementation of the Tic Tac Toe game. 
It uses a simple command line interface to prompt players for their moves and display the current state of the game board.

The script defines a `main()` function that runs the game loop, alternating between player X and player O. 
Each player is prompted to enter a number from 1-9 corresponding to the cell they want to mark on the grid. 
The script validates the input and updates the game board accordingly. 
After each move, the script checks for a winner or a tie, and ends the game if necessary.

## Building the Container Image
If you want to build the container image yourself, you can use the Dockerfile provided in this directory itself. 
In Terminal, navigate to `assignments/shroff` and use the following command:
```
docker build -t my_image .
``` 
Note: Make sure to replace `my_image` with a name of your choice, for example, `tic-tac-toe-game`.

## Running the Container Image
To run the container image for the Tic Tac Toe game, you can use the following command:
```
docker run -it my_image
```
This command runs the container in interactive mode with a TTY allocated, allowing the script to prompt players for input and display the game board. 
<mark>The `-it` flag is required to ensure proper input and output.</mark>

## Alternative: Running the Pre-Built Container Image
To build and run the Tic Tac Toe game using the pre-built container image, you can use the following commands:
```
docker pull prathamshroff/my_image
docker run -it prathamshroff/my_image
```
The `docker pull` command downloads the [pre-built image from Docker Hub](https://hub.docker.com/r/prathamshroff/my_image) at `prathamshroff/my_image`, 
and the `docker run` command runs the container in interactive mode with a TTY allocated, 
allowing the script to prompt players for input and display the game board.
