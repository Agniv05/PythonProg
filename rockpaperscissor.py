import random

def check_win(player_choice, computer_choice):
    # Define winning conditions
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissor') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissor' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun():
    # Choices available in the game
    choices = ['rock', 'paper', 'scissor']
    
    # Take player input and randomize computer's choice
    player_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    if player_choice not in choices:
        print("Invalid choice! Please choose either rock, paper, scissor.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the result
    result = check_win(player_choice, computer_choice)
    print(result)

# Run the game
snake_water_gun()
num1 = float(input("Enter first number: "))
