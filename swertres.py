from random import randint  # Import the randint function from the random module

# Generate a random 3-digit winning number
winning_numbers = f"{randint(0, 3):03}"  # Generate a random number between 0 and 999, then format it as a 3-digit string

# Mag try ang  player to enter their bet
player_bet = input("Enter a 3-digit number: ")  # Will Ask the player to input a 3-digit number

# Validate the player's input
while not (player_bet.isdigit() and len(player_bet) == 3):  # Continue looping if the input is not a 3-digit number
    player_bet = input("Enter a valid 3-digit number: ")  # Prompt again for a valid 3-digit number

# Display the winning numbers
print(f"Winning numbers are: {winning_numbers}")  # Print the randomly generated winning numbers

# Determine the result and print the appropriate message
if player_bet == winning_numbers:  # Check if the player's bet matches the winning numbers exactly
    print("You win!")  # Print "You win!" if the player has won exactly the number
elif sorted(player_bet) == sorted(winning_numbers):  # Check if the digits of the player's bet match the winning numbers in any order
    print("You Partially Won!")  # Print "You Partially Won!" if the player has the correct digits in a different order
else:  # If neither condition is met
    print("You lose, better luck next time!")  # Print "You lose, better luck next time!" if the player did not win
