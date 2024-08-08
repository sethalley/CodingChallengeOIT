# CodingChallengeOIT
Coding challenge for BYU OIT developers

!!*** DEPENDENCIES ***!!
pip install colorama


This tic tac toe game functions directly in the terminal and was written in python.

For the alotted time that I was given to complete this challenge I spent the first hour and a half writing the main logic and functions of the game. The next 30 minutes were spent handling potential errors caused by the user. 
Unfortunately I ran into a couple bugs that I had to dedicate some time towards debugging along the way. 
I then used StackOverflow to learn how to use the 'colorama' library to color the inputs within the terminal. 
The remainder of my time was spent organizing the code, cleaning it, and adding comments for clarity. In total it was close to 3.5 hours.

My main flow of logic as developing the game was to first design the simple game board by writing the 'print_board' function. I then spent time developing the function for users to take their turn, ensuring that the board was properly updated. A similar function was made for the computer to be able to take a turn. This required some trial and error to ensure valid inputs and properly updating the board.
The next challenge was to write within the main game logic to find a way to allow the user to alternate turns with the computer, making sure that a max of 9 turns were allowed. I ended up using a boolean variable called 'playerTurn' that can be toggled.
Then it just came down to analyzing the board for game ending situations and handling them accordingly, as well as using the coloring package to display the colors in the terminal. (If somehow missed the only dependency is 'pip install colorama')

I enjoyed this challenge! Thank you for considering me for the position!

