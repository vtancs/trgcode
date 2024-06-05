from itertools import product
import random

# Calculate all possible outcomes of rolling three dice
all_rolls = list(product(range(1, 7), repeat=3))

def is_big(roll):
    roll_sum = sum(roll)
    return 11 <= roll_sum <= 17 and len(set(roll)) != 1

def is_small(roll):
    roll_sum = sum(roll)
    return 4 <= roll_sum <= 10 and len(set(roll)) != 1

total_outcomes = len(all_rolls)
big_count = 0
small_count = 0

for roll in all_rolls:
    if is_big(roll):
        big_count += 1
    elif is_small(roll):
        small_count += 1

big_probability = big_count / total_outcomes
small_probability = small_count / total_outcomes

print(f"Big Probability: {big_probability:.2%}")
print(f"Small Probability: {small_probability:.2%}")

def simulate_sic_bo_games(num_games):
    outcomes = []
    
    for _ in range(num_games):
        roll = tuple(random.randint(1, 6) for _ in range(3))
        if is_big(roll):
            outcomes.append('Big')
        elif is_small(roll):
            outcomes.append('Small')
        else:
            outcomes.append('Other')
    
    consecutive_counts = {key: [0] * 10 for key in ['Big', 'Small']}
    current_consecutive = {key: 0 for key in ['Big', 'Small']}
    
    for result in outcomes:
        if result in ['Big', 'Small']:
            current_consecutive[result] += 1
        else:
            current_consecutive = {key: 0 for key in ['Big', 'Small']}
        
        for key in ['Big', 'Small']:
            for i in range(1, 10):
                if current_consecutive[key] >= i:
                    consecutive_counts[key][i] += 1
    
    return consecutive_counts

# Simulate a large number of games
num_games = 100000
consecutive_counts = simulate_sic_bo_games(num_games)

print("Consecutive Counts:")
for key in ['Big', 'Small']:
    print(f"{key}:")
    for i, count in enumerate(consecutive_counts[key][1:], start=1):
        print(f"Consecutive {i}: {count / (num_games - 1):.2%}")
