#
#
#
# Seth Alley
# Coding Challenge -- Tic Tac Toe submission

import random
from colorama import Fore, Style, init #from stack overflow
init()  # Initialize colorama

#FUNCTIONS

def print_board(board):
    """Display the game board with color formatting."""
    print('\n')
    # Print each row of the board with the right colors
    print(f"{color_format(board[0])} | {color_format(board[1])} | {color_format(board[2])}")
    print("----------")
    print(f"{color_format(board[3])} | {color_format(board[4])} | {color_format(board[5])}")
    print("----------")
    print(f"{color_format(board[6])} | {color_format(board[7])} | {color_format(board[8])}")
    print('\n')

def color_format(value):
    """Return color formatted string for board values."""
    #makes user input green and computer input red
    if value == 'X':
        return f"{Fore.GREEN}{value}{Style.RESET_ALL}"
    elif value == 'O':
        return f"{Fore.RED}{value}{Style.RESET_ALL}"
    else:
        return value



def turn(board):
    """Logic for the user's turn"""
    #loop to ensure that a valid spot it chosen before moving on
    turnComplete = False
    while turnComplete == False:
        # prompt user for input
        selection = input(f"Which space do you choose? \n")
        
        # check if the input is a digit
        if not selection.isdigit():
            print("Invalid input, please enter a number.")
            continue
        
        # convert the input to an integer
        selection = int(selection)
        
        # check if the number is within the valid range
        if selection > 9 or selection < 1:
            print("Invalid input, please choose a number between 1 and 9.")
            continue
        
        # check if the selected space is available and update the board
        index = selection - 1
        if board[index].isdigit():
            board[index] = 'X'
            break
        else:
            print("Space already taken, please try again.")
    
def simTurn(board):
    """Logic for the computer's turn"""
    # loop to ensure the game doesn't continue until a valid spot is chosen and updated
    turnComplete = False
    while turnComplete == False:
        #generate random integer
        selection = random.randint(1, 9)
        #check to see if spot is available, and update the board
        index = selection - 1
        if board[index].isdigit():
            board[index] = 'O'
            break
        else:
            print("Space already taken, please try again.")
    print(f"\n Computer thinking... \n Computer move:")
    print_board(board)

def checkWinner(board):
    """Function to check to see if the updated board has a winner by analyzing all possible win combinations"""
    winner = False
    # Horizontal win scenarios
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8]):
        winner = True
    # Vertical win scenarios
    elif (board[0] == board[3] == board[6] or
          board[1] == board[4] == board[7] or
          board[2] == board[5] == board[8]):
        winner = True
    # Diagonal win scenarios
    elif (board[0] == board[4] == board[8] or
          board[2] == board[4] == board[6]):
        winner = True
    return winner


def game():
    """Function to run the game"""
    #initialize and label the playing board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    winner = False

    #prompt the user and handle input to begin the game
    while True:
        starter = input(f"\nWould you like to go first? (Y/N) \n")
        starter = starter.upper()
        if starter.startswith("Y"):
            playerTurn = True
            break
        elif starter.startswith("N"):
            playerTurn = False
            break
        else:
            print("Invalid input. Yes or No.")
    print_board(board)

    #loop to alternate user turns with the computer until there is a winner or spaces are filled
    for x in range(9):
        if playerTurn:
            turn(board)
        else:
            simTurn(board)
        #logic to determine if there is a winenr, and how to properly handle the outcome
        if checkWinner(board) and playerTurn == True:
            print_board(board)
            print(f"\n * * * You Win! * * * \n")
            winner = True
            break
        elif checkWinner(board) and playerTurn == False:
            print(f" \n You lose! (and this computer is pretty bad so that's embarrassing) \n")
            break
        playerTurn = not playerTurn
         
    #if all spaces are full and winner is false
    if winner == False:
        print(" ---- We have a draw ---- \n")
    
    #prompt user to see if they would like to play again
    repeat = input(f"Would you like to play again? (Y/N) \n")
    repeat = repeat.upper()
    if repeat.startswith("Y"):
        game()



#Run the program!
game()
