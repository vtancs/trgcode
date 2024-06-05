from collections import Counter
from itertools import product

# Calculate all possible outcomes of rolling three dice
all_rolls = list(product(range(1, 7), repeat=3))

def calculate_probabilities():
    total_outcomes = len(all_rolls)
    
    # Probabilities for each type of bet
    sum_probabilities = Counter()
    specific_triple_probabilities = Counter()
    any_triple_count = 0
    double_probabilities = Counter()
    single_probabilities = Counter()
    
    for roll in all_rolls:
        roll_sum = sum(roll)
        sum_probabilities[roll_sum] += 1
        
        if roll[0] == roll[1] == roll[2]:
            specific_triple_probabilities[roll[0]] += 1
            any_triple_count += 1
            
        for num in range(1, 7):
            count_num = roll.count(num)
            if count_num >= 2:
                double_probabilities[num] += 1
            single_probabilities[num] += count_num
    
    # Convert counts to probabilities
    for key in sum_probabilities:
        sum_probabilities[key] /= total_outcomes
        
    for key in specific_triple_probabilities:
        specific_triple_probabilities[key] /= total_outcomes
        
    any_triple_probability = any_triple_count / total_outcomes
    
    for key in double_probabilities:
        double_probabilities[key] /= total_outcomes
        
    for key in single_probabilities:
        single_probabilities[key] /= total_outcomes
    
    return {
        'sum_probabilities': dict(sum_probabilities),
        'specific_triple_probabilities': dict(specific_triple_probabilities),
        'any_triple_probability': any_triple_probability,
        'double_probabilities': dict(double_probabilities),
        'single_probabilities': dict(single_probabilities)
    }

probabilities = calculate_probabilities()

print("Sum Probabilities:")
for key in sorted(probabilities['sum_probabilities']):
    print(f"Sum {key}: {probabilities['sum_probabilities'][key]:.2%}")

print("\nSpecific Triple Probabilities:")
for key in sorted(probabilities['specific_triple_probabilities']):
    print(f"Triple {key}{key}{key}: {probabilities['specific_triple_probabilities'][key]:.2%}")

print(f"\nAny Triple Probability: {probabilities['any_triple_probability']:.2%}")

print("\nDouble Probabilities:")
for key in sorted(probabilities['double_probabilities']):
    print(f"Double {key}: {probabilities['double_probabilities'][key]:.2%}")

print("\nSingle Probabilities:")
for key in sorted(probabilities['single_probabilities']):
    print(f"Single {key}: {probabilities['single_probabilities'][key]:.2%}")
