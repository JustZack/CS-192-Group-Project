import random
import matplotlib.pyplot as plt
import rps


def instructions(response):
    # Add to instruction_string so that it contains information on
    # how to play rock-paper-scissors
    instruction_string = ""

    # Use a string method to make response all one case

    # Use an if statement to check if the response is "yes"
    
    # If the user does want instructions pass instruction_string to
    # rps.print_instructions





# Name requirements: must be at least two characters, must be no more than 10 characters, must only be 
# one name (i.e. no spaces), must start with an upper case letter.
# Return requirement: name
def check_name(name):

    error = "Somethings wrong"

    if len(name) > 30:
        rps.quit_game(error)

    # Use if statements, as above, to check if 'name' meets the requirements listed above. If it fails
    # any condition call rps.quit_game with an appropriate error message.

    # return the variable name once have checked all name requirements





# Num requirements: must be more than two and less than 21.
# Return requirement: num
def check_times_to_play(num):
    error = "Number is not correct"

    # Check that 'num' meets the requirements above.

    # If 'num' does not meet requirements call rps.quit_game with an error 
    # message (the variable 'error.')
    # Note: use function int, to convert num to integer when using it to compare to another integer, i.e. int(num)

    # return the variable num once have checked requirements





def play_game(name):
    
    # This gets the move from a player when they push a button.
    player_move = rps.get_player_move()

    # Use the random library to chose a random move for the player.

    # Use if statements to check who won. Set who_won equal to 'Computer', 'Player', or 'Tie'
    who_won = ""

    # After determines who won, build a results string.
    # The next 3 lines partially builds this string. Complete for computer, add for tie, and add line for winner
    results = "Player played " + player_move
    results += "\n"
    results += "Computer played "

    # Use rps.display_results to display the results string for the game.


    # return the variable who_won
  


def play_match():

    # Call rps.ask_instructions() to see if player wants instructions


    # Call rps.get_name() to get a string of the players name
    # Be sure to save return value, i.e. player_name = rps.get_name()
    player_name = ""


    # Call rps.get_num_play to get the number of games to play
    # Be sure to save return value, i.e. num_times = rps.get_num_play()
    num_times = 0

    
    # Use these variables to keep track of who won
    ties = 0
    player_wins = 0
    computer_wins = 0


    # Use a while or for loop to call play_game the correct amount of times
    count = 0
    while count < num_times:
        game_winner = play_game(player_name)
        # Now use an if statement to increment total for winner
        # i.e. will increment either ties, player_wins, or computer_winds
        count = count + 1

    # Call make_graph using the variables for win counts above.
    make_graph(player_name, player_wins, computer_wins, ties)




# Create a graph as we did in the previous lab
def make_graph(name, player_wins, comp_wins, ties):
    print "Not implemented yet"



