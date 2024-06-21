from random import randint # Import the randint function from the random module

def fold_unfold(choice): # Define a function to convert a number to "fold" or "unfold"
    return "fold" if choice == 1 else "unfold" # Return "fold" if the choice is 1, otherwise return "unfold"


p1 = input("Fold/Unfold: ").lower()  # Convert input to lowercase to ensure consistency

# Generate random choices for Computer 2 and Computer 3
c2, c3 = fold_unfold(randint(1, 2)), fold_unfold(randint(1, 2))

# Print the choices of Player 1, Computer 2, and Computer 3
print("Player 1:", p1)
print("Computer 2:", c2)
print("Computer 3:", c3)

#This determine the winner based on the combinations of choices
if (p1, c2, c3) in [("fold", "unfold", "unfold"), ("unfold", "fold", "fold")]: 
    print("Player 1 wins!") # Si Player 1 wins if the choice match the combination

elif (p1, c2, c3) in [("unfold", "fold", "unfold"), ("fold", "unfold", "fold")]:
    print("Computer 2 wins!")  # Si Computer 2 wins if the choice match the combination

elif (p1, c2, c3) in [("unfold", "unfold", "fold"), ("fold", "fold", "unfold")]: 
    print("Computer 3 wins!") # Si Computer 3 wins if the choices match the combination

else: 
    print("NO ONE WINS!") # otherwise no one will wins if the choices do not match any winning combination 
