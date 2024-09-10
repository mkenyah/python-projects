import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What amount do you want to deposit: KSH  ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("OOPS! 🙄Amount must be greater than 0")
        else:
            print("Please enter a number😉")
    return amount

def get_the_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("OOPS! 🙄 Enter a valid number of lines")
        else:
            print("Please enter a number😉")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? KSH  ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between KSH {MIN_BET} - KSH {MAX_BET}")
        else:
            print("Please enter a number😉")
    return amount

def main():
    balance = deposit()
    lines = get_the_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds, your current balance is KSH {balance}")
        else:
            balance -= total_bet
            print(f"You are betting KSH {bet} on {lines} lines. Total bet is equal to KSH {total_bet}")
            print(f"Remaining balance is KSH {balance}")
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won 😂 ksh{winnings}")
    print(f"You won on lines:", *winnings_lines)

main()
