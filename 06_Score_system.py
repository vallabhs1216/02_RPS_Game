# Rps Component - Used to track scores

# Rounds calculatiuon
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purpose
test_results = ["won", "won", "lose", "lose", "tie" ]

# Play game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item
    if result == "tie":
        result = "It's a tie"
        rounds_drawn += 1
    elif result == "lose":
        rounds_lost += 1

#  Calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

# End of game
print()
print("***** End Game Summary *****")
print(f"Won:{rounds_won} \t|\t Lost:{rounds_lost} \t|\t Drawn:{rounds_drawn}")
print()
print("Thanks for playing")
