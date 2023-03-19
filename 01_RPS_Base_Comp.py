import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please enter an integer above 0 or <enter> for infinite rounds"

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


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

    # Main routine goes here


# Main routine goes here


# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'no' show instructions

show_instructions = choice_checker("Welcome to Rock Paper Scissors,"
                                   "is This Your First Time Playing? ", yes_no_list,
                                   "Please Enter yes (y) or no (n)")
print()

# if 'no' show instructions
if show_instructions == "yes":
    statement_generator("How To Play", "=")
    print()
    print("Choose a number of rounds to play or press <Enter> for Endless mode")
    print("Each round pick from Rock / Paper / Scissors (Or xxx To End The Program)")
    print("You Can Type r / p / s  as a short cuz")
    print()
    statement_generator("Rules", "~", )
    print("- Rock Beat Scissors")
    print("- Scissors Beats Paper")
    print("- Paper Beats Rock")
    print()
    print("Good Luck")
    print()

statement_generator("Please pick how many rounds "
                    "you want to play,"
                    " or press <enter> for endless mode", "-")

#  Rounds scoring
rounds_played = 0
rounds_drawn = 0
rounds_lost = 0

mode = "regular"

game_history = []

# Ask user for # of rounds or <enter> for infinite rounds
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:

    # Rounds Heading
    print()

    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of " \
                  f"{rounds}"
    print(heading)
    choose_instruction = "Please choose rock (r), paper (p) " \
                         "or scissors (s): "
    choose_error = "Please choose from rock / paper / " \
                   "scissors (or 'xxx' to quit)"

    # Ask user for R/P/S
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # Get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # Compare choices
    if user_choice == "rock" and comp_choice == "scissors":
        result = "win"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "win"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "win"
    elif user_choice == comp_choice:
        result = "tie"
        rounds_drawn += 1
    else:
        result = "lose"
        rounds_lost += 1

    feedback = f"You chose: {user_choice} - Computer chose: {comp_choice} | You {result}"

    print(feedback)
    round_outcome = f'Round {rounds_played + 1}: {feedback}'
    game_history.append(round_outcome)

    # Exit code
    if user_choice == "xxx":
        break

    # Rest of loop

    rounds_played += 1


# Ask user if they want to see their game history.
# If 'yes' show game history


rounds_won = rounds_played - rounds_drawn - rounds_lost

# *** Calculate % of times won, loss, and tied
percent_won = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tied = rounds_drawn / rounds_played * 100

print()
print("******** Game history ********")
for game in game_history:
    print(game)

print()

print("******** Game Statistics ********")
print(f"Won: {rounds_won}, ({percent_won:.0f}%)\n"
      f"Loss:{rounds_lost}, ({percent_lost:.0f}%)\n"
      f"Tied: {rounds_drawn}, ({percent_tied:.0f}%)")

# End of game
print()
print("***** End Game Summary *****")
print(f"Won:{rounds_won} \t|\t Lost:{rounds_lost} \t|\t Drawn:{rounds_drawn}")
print()
print("Thanks for playing")
