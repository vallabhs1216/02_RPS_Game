import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please enter an integer above 1 or <enter> for infinite rounds"

        # Checks for response if infinite mode is not chosen
        # Integer must be > 0
        if response != "":
            try:
                response = int(response)

                #  If response is < 1 it restarts loop
                if response < 1:
                    print(round_error)
                    continue
            # If response is not integer restart loop
            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(choose_instruction, rps_list, choose_error):

    valid = False
    while not valid:
        # Ask user for choice
        response = input(choose_instruction).lower()

        for item in rps_list:
            if response == item[0] or response == item:
                return item

        print(choose_error)
        print()


# Main routine goes here

# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'no' show instructions


# ask user for # of rounds then loop...
rounds_played = 0


# Ask user for # of rounds or <enter> for infinite rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of " \
                  f"{rounds}"
    print(heading)
    choose_instruction = "Please choose rock (r), paper (p) " \
                         "or scissors (s)"
    choose_error = "Please choose from rock / paper / " \
                   "scissors (or 'xxx' to quit)"

    # Ask user for R/P/S
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # Exit code
    if choose == "xxx":
        break

    # Rest of loop
    print(f"You chose {choose}")

    rounds_played += 1
    # End game if round limit is reached
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history.
# If 'yes' show game history

# Show results
