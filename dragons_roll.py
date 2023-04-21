import random

def roll_dice():
    """Simulates rolling a twenty-sided dice and returns the result."""
    return random.randint(1, 20)

print("Welcome to Dragon's Roll - The Ultimate D&D Dice Rolling Simulator!\n")

while True:
    input("Press Enter to roll the dice...")

    result = roll_dice()
    print(f"\nYou rolled a {result}!\n")

    choice = input("Roll again? (y/n): ")
    if choice.lower() != 'y':
        print("Thanks for playing!")
        break
