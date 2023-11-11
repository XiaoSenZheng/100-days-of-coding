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

#Write your code below this line 👇
import random
print("Let's play Rock, Paper, Scissors!")
user_choice = input("Type your choice:")
if user_choice == "rock":
  print(rock)
elif user_choice == "paper":
  print(paper)
elif user_choice == "scissors":
  print(scissors)
else:
  print("Please input: rock, paper oor scissors")
computer_choice = random.choice(["rock", "paper", "scissors"])
print(computer_choice)
if computer_choice == "rock":
  print(rock)
elif computer_choice == "paper":
  print(paper)
elif computer_choice == "scissors":
  print(scissors)
if user_choice == computer_choice:
  print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
  print("You lose!")
else:
  print("You won!")
