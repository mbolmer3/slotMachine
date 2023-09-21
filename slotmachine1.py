import random



MAX_LINES = 3
MAX_BET = 10000
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
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}

def checking_winnings(columns, lines, betAmount, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * betAmount
            winning_lines.append(line + 1)
    return winnings, winning_lines
            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end = " | ")
            else:
                print(col[row], end = "")
                
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit?  ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be a positive number.  ")
        else:
            print("Please enter a number.  ")
            
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ")  ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number.  ")
            
            
    return lines

def get_bet_amount():
    while True:
        betAmount = input("How much would you like to gamble per line? ($" + str(MIN_BET) + "-$" + str(MAX_BET) + ")  ")
        if betAmount.isdigit():
            betAmount = int(betAmount)
            if MIN_BET < betAmount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet amount between ${MIN_BET} and ${MAX_BET}."  )
        else:
            print("Please enter a number.  ")
            
            
    return betAmount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        betAmount = get_bet_amount()
        totalBet = lines * betAmount
        
        
        if totalBet > balance:
            print(f"You do not have the funds to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are gambling ${betAmount} on {lines} lines. Your total bet is ${totalBet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = checking_winnings(slots, lines, betAmount, symbol_value)
    if winnings > 0:
        print(f"You won ${winnings}.")
    else:
        print("You lost.")
    return winnings - totalBet


def main():
    balance = deposit()
    while True:
        if balance == 0:
            print("You have no remaining funds.")
            break
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin again (press q to quit).  ")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance} in your account")
        
        
main()