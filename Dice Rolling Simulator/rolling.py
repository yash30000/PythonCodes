import random

while True:
    input("Press Enter to roll dice...")
    print("Dice shows:", random.randint(1,6))
    if input("Roll again? (y/n): ") == "n":
        break
