# Probability Simulations

This Python program simulates and calculates probability. 
It includes four main tasks: simulating coin tosses, rolling a die, drawing cards, and calculating the probability of compound events. 
The program also includes test cases to validate the correctness of each task.

## Requirements

- Python 3.x
- matplotlib library

## Installation

1. Ensure Python is installed.
2. Install the required `matplotlib` library:
   ```bash
   python3 install matplotlib
   ```
   
## Usage

1. Save code in a file named probability.py
2. Open terminal or command prompt.
3. Navigate to the directory with the probability.py file:
```bash
cd path_to_directory
```
4. Run the program:
   ```bash
   python3 probability.py
   ```

Program Tasks:

Task 1: Simulating Coin Tosses
Simulates tossing a coin 100 times.
Counts occurrences of heads and tails.
Plots results on a bar chart.

Task 2: Rolling a Die
Simulates rolling a 6 sided die 60 times.
Counts the frequency of each outcome.
Plots distribution of die rolls.

Task 3: Drawing Cards
Simulates drawing a card from deck 20 times.
Counts whether cards are red or black.
Plots count of red vs. black.

Task 4: Probability of Compound Events
Simulates flipping 2 coins 50 times.
Counts outcomes of both heads and at least one head.
Plots both scenarios.

Test Cases:

Each task includes 3 normal test cases and 3 edge cases. 

Task 1: Coin Tosses
Edge cases:
0 tosses
1 toss
2 tosses
Normal cases:
100 tosses
500 tosses
1000 tosses

Task 2: Rolling a Die
Edge cases:
0 rolls
1 roll
2 rolls
Normal cases:
60 rolls
100 rolls
500 rolls

Task 3: Drawing Cards
Edge cases:
0 draws
1 draw
2 draws
Normal cases:
20 draws
52 draws
30 draws

Task 4: Two Coin Tosses
Edge cases:
0 tosses
1 toss
2 tosses
Normal cases:
50 tosses
100 tosses
200 tosses

## License

This project is licensed under the MIT License.
