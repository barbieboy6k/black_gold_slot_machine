import secrets

# def reel data order
reel1 = (
    ["SINGLE BAR"] * 16 +
    ["DOUBLE BAR"] * 13 +
    ["TRIPLE BAR"] * 6 +
    ["BLACK GOLD"] * 1 +
    ["BLANK"] * 36
)

reel2 = (
    ["SINGLE BAR"] * 18 +
    ["DOUBLE BAR"] * 7 +
    ["TRIPLE BAR"] * 4 +
    ["BLACK GOLD"] * 1 +
    ["BLANK"] * 42
)

reel3 = (
    ["SINGLE BAR"] * 20 +
    ["DOUBLE BAR"] * 4 +
    ["TRIPLE BAR"] * 3 +
    ["BLACK GOLD"] * 1 +
    ["BLANK"] * 44
)

# def payouts
payouts = {
    ("BLACK GOLD", "BLACK GOLD", "BLACK GOLD"): 1000,
    ("TRIPLE BAR", "TRIPLE BAR", "TRIPLE BAR"): 229,
    ("DOUBLE BAR", "DOUBLE BAR", "DOUBLE BAR"): 13,
    ("SINGLE BAR", "SINGLE BAR", "SINGLE BAR"): 16,
    # Double reel payouts
    ("BLACK GOLD", "BLACK GOLD"): 100,
    ("TRIPLE BAR", "TRIPLE BAR"): 10,
    ("DOUBLE BAR", "DOUBLE BAR"): 5,
    ("SINGLE BAR", "SINGLE BAR"): 2,
}

# spin function
def spin_reels():
    reel1_pos = secrets.randbelow(72)
    reel2_pos = secrets.randbelow(72)
    reel3_pos = secrets.randbelow(72)
    return (reel1[reel1_pos], reel2[reel2_pos], reel3[reel3_pos])

# winning calculation function
def calculate_winnings(result, bet_multiplier):
    # check for triple reel payouts
    if result in payouts:
        return payouts[result] * bet_multiplier
    # check for double reel payouts
    if (result[0], result[1]) in payouts:
        return payouts[(result[0], result[1])] * bet_multiplier
    if (result[0], result[2]) in payouts:
        return payouts[(result[0], result[2])] * bet_multiplier
    if (result[1], result[2]) in payouts:
        return payouts[(result[1], result[2])] * bet_multiplier
    # No payout, return negative of bet
    return -bet_multiplier

# Main game loop
def play_slot_machine():
    balance = float(input("Enter the amount of money you want to start with: $"))
    bet_multiplier = int(input("Enter your bet multiplier (1-500): "))

    wins = 0
    total_input = balance
    total_won = 0

    while balance >= bet_multiplier:
        print(f"Current Balance: ${balance:.2f}")
        spin_input = input("Type 'Spin' to spin the reels or 'Exit' to quit: ")

        if spin_input.lower() == "exit":
            break

        if spin_input.lower() != "spin":
            print("Invalid input. Type 'Spin' to spin the reels or 'Exit' to quit.")
            continue

        result = spin_reels()
        win_amount = calculate_winnings(result, bet_multiplier)
        
        # spin result display
        print(f"Reel 1: {result[0]}, Reel 2: {result[1]}, Reel 3: {result[2]}")

        # balance updater of winnings
        balance += win_amount
        total_won += max(win_amount, 0)  # Only add to total_won if there's a positive win
        wins += 1 if win_amount > 0 else 0

        # winnings display
        if win_amount > 0:
            print(f"You won ${win_amount:.2f}!")

    # when player exits or runs out of money display results
    print("\nGame over.")
    if total_input > 0:
        print(f"Total amount inputted: ${total_input:.2f}")
        print(f"Total amount won: ${total_won:.2f}")
        print(f"Number of wins: {wins}")
    else:
        print("You didn't play any rounds.")

if __name__ == "__main__":
    play_slot_machine()