game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in range(0, 5):
    result = input("choose result: ")

    outcome = f"Round {item}: {result}"

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_drawn - rounds_lost
# *** Calculate % of times won, loss, and tied
percent_won = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tied = rounds_drawn / rounds_played * 100

print()
print("******** Game history ********")
for game in game_summary:
    print(game)

print()

print("******** Game Statistics ********")
print(f"Won: {rounds_won}, ({percent_won:.0f}%)\n"
      f"Loss:{rounds_lost}, ({percent_lost:.0f}%)\n"
      f"Tied: {rounds_drawn}, ({percent_tied:.0f}%)")