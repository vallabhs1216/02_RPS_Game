# Compare user choice and computer choice to give output
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for iten in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options
        if user_choice == "rock" and comp_choice == "scissors":
            result = "win"
        elif user_choice == "paper" and comp_choice == "rock":
            result = "win"
        elif user_choice == "scissors" and comp_choice == "paper":
            result = "win"
        elif user_choice == comp_choice:
            result = "tie"
        else:
            result = "lose"

        if result == "tie":
            feedback = f"You chose: {user_choice} - Computer chose: {comp_choice} | You tied"
        else:
            feedback = f"You chose: {user_choice} - Computer chose: {comp_choice} | You {result}"

        print(feedback)

    comp_index += 1
    print()
    