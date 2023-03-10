# Functions go here

def rps_checker(question):

    error = "Please choose between Rock / Paper / " \
            "Scissors (or xxx to quit)."
    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"

        elif response == "p" or response == "paper":
            return "paper"

        elif response == "s" or response == "scissors":
            return "scissors"

        elif response == "xxx":
            return response
        else:
            print(error)


# Main routine goes here

# loop for testing
user_choice = ""
while user_choice != "xxx":
    # Ask user for R/P/S
    user_choice = rps_checker("Choose Rock / Paper /"
                              " Scissors: ")

    # prints choice
    print(f'You chose {user_choice}')