import random

# Define the values of the cards
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
cards = list(card_values.keys()) * 4  # A single deck of 52 cards

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def hand_value(hand):
    value = sum(card_values[card] for card in hand)
    num_aces = hand.count('A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def play_blackjack():
    deck = cards.copy()
    random.shuffle(deck)

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    # Player's turn
    while hand_value(player_hand) < 17:
        player_hand.append(draw_card(deck))

    # Dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    if player_total > 21:
        return 'dealer'
    elif dealer_total > 21:
        return 'player'
    elif player_total > dealer_total:
        return 'player'
    elif dealer_total > player_total:
        return 'dealer'
    else:
        return 'push'

def simulate_blackjack_games(num_games):
    player_wins = 0
    dealer_wins = 0
    pushes = 0

    for _ in range(num_games):
        result = play_blackjack()
        if result == 'player':
            player_wins += 1
        elif result == 'dealer':
            dealer_wins += 1
        else:
            pushes += 1

    total_games = player_wins + dealer_wins + pushes
    player_win_probability = player_wins / total_games
    dealer_win_probability = dealer_wins / total_games
    push_probability = pushes / total_games

    return player_win_probability, dealer_win_probability, push_probability

# Simulate a large number of games
num_games = 100000
player_win_probability, dealer_win_probability, push_probability = simulate_blackjack_games(num_games)

print(f'Player win probability: {player_win_probability:.2%}')
print(f'Dealer win probability: {dealer_win_probability:.2%}')
print(f'Push probability: {push_probability:.2%}')
