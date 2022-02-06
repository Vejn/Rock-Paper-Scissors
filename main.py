rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇

#Taking the player choice
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if player_choice == '0' or player_choice.lower() == 'rock':
  player = "Rock"
  print(rock)
elif player_choice == '1' or player_choice.lower() == 'paper':
  player = "Paper"
  print(paper)
else:
  player = "Scissors"
  print(scissors)

#Randomizing computer choice
computer_choice = random.randint(0,2)
if computer_choice == 0:
  computer = "Rock"
  print(rock)
elif computer_choice == 1:
  computer = "Paper"
  print(paper)
else:
  computer = "Scissors"
  print(scissors)

#Determining the winner

if player == computer:
  print("It's tie!")
elif player == "Rock" and computer == "Scissors":
  print("Player wins!")
elif player == "Paper" and computer == "Rock":
  print("Player wins!")
elif player == "Scissors" and computer == "Paper":
  print("Player wins!")
else:
  print("Computer wins!")



