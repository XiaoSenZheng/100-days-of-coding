from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
clear()
print(logo)
dict = {}
while True:
  name = input("What's your name?")
  bid = input("How much do you want to bid?")
  dict[name] = bid
  more = input("Are there any other bidders? Type 'yes' or 'no'.")
  if more == "yes":
    continue
  elif more == "no":
    highest = 0
    for key,bid in dict.items():
      if int(bid) > highest:
        highest = int(bid)
        winner = key
        print(f"The winner is {winner} with a bid of ${highest}")
  break
