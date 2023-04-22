# Initialize the board
board = [' ' for i in range(9)]

# Define the function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Define the function to check if the board is full
def is_board_full():
    if ' ' in board:
        return False
    else:
        return True

# Define the function to check if there's a winner
def is_winner(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

# Define the main function to play the game
def main():
    print_board()
    while True:
        # Player X's turn
        while True:
            move = input("Player X's turn (enter a number from 1-9): ")
            if not move.isdigit():
                print("Invalid input. Please enter a number from 1-9.")
                continue
            move = int(move) - 1
            if not 0 <= move < 9:
                print("Invalid input. Please enter a number from 1-9.")
                continue
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is already taken. Try again.")

        print_board()
        if is_winner('X'):
            print("Player X wins!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

        # Player O's turn
        while True:
            move = input("Player O's turn (enter a number from 1-9): ")
            if not move.isdigit():
                print("Invalid input. Please enter a number from 1-9.")
                continue
            move = int(move) - 1
            if not 0 <= move < 9:
                print("Invalid input. Please enter a number from 1-9.")
                continue
            if board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("That spot is already taken. Try again.")

        print_board()
        if is_winner('O'):
            print("Player O wins!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
