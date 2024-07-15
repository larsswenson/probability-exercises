import random
import matplotlib.pyplot as plt

# Coin toss
def simulate_coin_tosses(num_tosses):
    heads = 0
    tails = 0
    for _ in range(num_tosses):
        if random.choice(['H', 'T']) == 'H':
            heads += 1
        else:
            tails += 1
    return heads, tails

def plot_coin_tosses(heads, tails):
    labels = ['Heads', 'Tails']
    counts = [heads, tails]
    plt.bar(labels, counts, color=['blue', 'green'])
    plt.title('Coin Toss Simulation')
    plt.ylabel('Count')
    plt.show()

# Die roll
def simulate_die_rolls(num_rolls):
    outcomes = [0] * 6
    for _ in range(num_rolls):
        outcome = random.randint(1, 6)
        outcomes[outcome - 1] += 1
    return outcomes

def plot_die_rolls(outcomes):
    labels = ['1', '2', '3', '4', '5', '6']
    plt.bar(labels, outcomes, color='purple')
    plt.title('Die Roll Simulation')
    plt.ylabel('Count')
    plt.show()

# Card draw
def simulate_card_draws(num_draws):
    deck = ['R'] * 26 + ['B'] * 26 
    random.shuffle(deck)
    reds = 0
    blacks = 0
    for _ in range(num_draws):
        card = deck.pop()
        if card == 'R':
            reds += 1
        else:
            blacks += 1
    return reds, blacks

def plot_card_draws(reds, blacks):
    labels = ['Red', 'Black']
    counts = [reds, blacks]
    plt.bar(labels, counts, color=['red', 'black'])
    plt.title('Card Draw Simulation')
    plt.ylabel('Count')
    plt.show()

# Compound events
def simulate_two_coin_tosses(num_tosses):
    both_heads = 0
    at_least_one_head = 0
    for _ in range(num_tosses):
        toss1 = random.choice(['H', 'T'])
        toss2 = random.choice(['H', 'T'])
        if toss1 == 'H' and toss2 == 'H':
            both_heads += 1
        if toss1 == 'H' or toss2 == 'H':
            at_least_one_head += 1
    return both_heads, at_least_one_head

def plot_two_coin_tosses(both_heads, at_least_one_head):
    labels = ['Both Heads', 'At Least One Head']
    counts = [both_heads, at_least_one_head]
    plt.bar(labels, counts, color=['blue', 'green'])
    plt.title('Two Coin Toss Simulation')
    plt.ylabel('Count')
    plt.show()

# Test cases 
def run_tests():
    # Edge cases
    print(simulate_coin_tosses(0))  # Expect (0, 0)
    print(simulate_coin_tosses(1))  # Expect (1, 0) or (0, 1)
    print(simulate_coin_tosses(2))  # Expect (2, 0), (1, 1), or (0, 2)
    # Normal cases
    print(simulate_coin_tosses(100))  # Expect ~ (50, 50)
    print(simulate_coin_tosses(500))  # Expect ~ (250, 250)
    print(simulate_coin_tosses(1000))  # Expect ~ (500, 500) 

    # Edge cases
    print(simulate_die_rolls(0))  # Expect [0, 0, 0, 0, 0, 0]
    print(simulate_die_rolls(1))  # Expect one of [1, 0, 0, 0, 0, 0] etc.
    print(simulate_die_rolls(2))  # Expect one of [2, 0, 0, 0, 0, 0] etc.
    # Normal cases
    print(simulate_die_rolls(60))  # Expect ~ [10, 10, 10, 10, 10, 10] 
    print(simulate_die_rolls(100))  # Expect ~ [16.67, 16.67, 16.67, 16.67, 16.67, 16.67] 
    print(simulate_die_rolls(500))  # Expect ~ [83.33, 83.33, 83.33, 83.33, 83.33, 83.33]

    # Edge cases
    print(simulate_card_draws(0))  # Expect (0, 0)
    print(simulate_card_draws(1))  # Expect (1, 0) or (0, 1)
    print(simulate_card_draws(2))  # Expect (2, 0), (1, 1), or (0, 2)
    # Normal cases
    print(simulate_card_draws(20))  # Expect ~ (10, 10) 
    print(simulate_card_draws(52))  # Expect === (26, 26) since entire deck is drawn
    print(simulate_card_draws(30))  # Expect ~ (15, 15) 

    # Edge cases
    print(simulate_two_coin_tosses(0))  # Expect (0, 0)
    print(simulate_two_coin_tosses(1))  # Expect (1, 0) or (0, 1)
    print(simulate_two_coin_tosses(2))  # Expect (2, 0), (1, 1), or (0, 2)
    # Normal cases
    print(simulate_two_coin_tosses(50))  # Expect ~ (12.5, 37.5) 
    print(simulate_two_coin_tosses(100))  # Expect ~ (25, 75)
    print(simulate_two_coin_tosses(200))  # Expect ~ (50, 150)

run_tests()

heads, tails = simulate_coin_tosses(100)
print(f"Heads: {heads}, Tails: {tails}")
plot_coin_tosses(heads, tails)

outcomes = simulate_die_rolls(60)
print(f"Die roll outcomes: {outcomes}")
plot_die_rolls(outcomes)

reds, blacks = simulate_card_draws(20)
print(f"Reds: {reds}, Blacks: {blacks}")
plot_card_draws(reds, blacks)

both_heads, at_least_one_head = simulate_two_coin_tosses(50)
print(f"Both Heads: {both_heads}, At Least One Head: {at_least_one_head}")
plot_two_coin_tosses(both_heads, at_least_one_head)
