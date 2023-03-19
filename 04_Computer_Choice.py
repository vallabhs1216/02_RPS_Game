import random

# main routine goes here

rps_list = ["rock", "paper", "scissors", "xxx"]

# Testing loop to generate 20 tokens
for item in range(0, 20):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end='\t')
