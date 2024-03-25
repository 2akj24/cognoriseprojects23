import random

def roll_dice(num_sides, num_rolls):
    print(f"Rolling {num_rolls} {num_sides}-sided dice:")
    for i in range(num_rolls):
        result = random.randint(1, num_sides)
        print(f"Roll {i+1}: {result}")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            if num_sides < 2:
                raise ValueError("Number of sides must be at least 2.")
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls < 1:
                raise ValueError("Number of rolls must be at least 1.")
            roll_dice(num_sides, num_rolls)
        except ValueError as ve:
            print(f"Error: {ve}")
        again = input("Do you want to roll again? (yes/no): ").lower()
        if again != "yes" :
            break

if __name__ == "__main__":
    main()
