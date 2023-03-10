# Version 3 - checks for response in list
# Functions go here

def rps_checker(question, valid_list, error):

    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Main routine goes here

# response list
rps_list = ["rock", "paper", "scissors", "xxx"]

# loop for testing
user_choice = ""
while user_choice != "xxx":

    # Ask user for R/P/S
    user_choice = rps_checker("Choose Rock / Paper / "
                              "Scissors: ", rps_list,
                              "Please choose between "
                              "Rock / Paper / Scissors "
                              "(or xxx to quit).")

    # prints choice
    print(f'You chose {user_choice}')

