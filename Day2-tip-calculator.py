#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = int(input("Total bill"))
People = int(input("Amount of people"))
tip = int(input("tip"))
per_person = (bill / People) * (tip / 100) + (bill / People)
print(f"Total amount per person is {per_person:.2f}")
