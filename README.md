# black_gold_slot_machine
Python script simulating the Black Gold Slot Machine game

```markdown
# Slot Machine Simulation

This Python script simulates a slot machine game based on the PAR sheet of the Black Gold slot machine. Players can input their starting balance and bet multiplier, spin the reels, and win or lose money based on the results. The game continues until the player decides to quit or runs out of money.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/barbieboy6k/black_gold_slot_machine.git
    ```
2. Navigate to the project directory:
    ```sh
    cd black_gold_slot_machine
    ```

## Usage

Run the script:
```sh
python black_gold_slot_machine.py
```

### Example

1. The game will prompt you to enter your starting balance:
    ```plaintext
    Enter the amount of money you want to start with: $100
    ```
2. Then, enter your bet multiplier (between 1 and 500):
    ```plaintext
    Enter your bet multiplier (1-500): 50
    ```
3. Type 'Spin' to spin the reels or 'Exit' to quit:
    ```plaintext
    Type 'Spin' to spin the reels or 'Exit' to quit: Spin
    ```
4. The result of the spin and your updated balance will be displayed:
    ```plaintext
    Reel 1: SINGLE BAR, Reel 2: BLANK, Reel 3: DOUBLE BAR
    Current Balance: $50.00
    ```

## Code Explanation

### Reel Data

The slot machine has three reels, each represented by a list of symbols with different frequencies.

### Payouts

The payouts are defined in a dictionary with keys as tuples representing the symbols on the reels and values as the payout multipliers.

### Spin Function

This function spins the reels and returns the symbols at random positions using secure random number generation.

### Calculate Winnings

This function calculates the winnings based on the result of the spin and the bet multiplier.

### Main Game Loop

This function handles the main game loop where the player can spin the reels or exit the game.

## PAR Sheet

The simulation is based on the PAR sheet of the Black Gold slot machine. The PAR (Paytable and Reel) sheet defines the symbols, their frequencies on the reels, and the payout structure. You can view the full PAR sheet [here](http://web.archive.org/web/20051215075607/http://ballygaming.com:80/media_library/pcsheets/6999.pdf).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the included LICENSE file for details.
