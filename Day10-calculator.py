from art import logo
print(logo)

def calculator(nu1, nu2, operator):
  if operator == "+":
    return nu1 + nu2
  elif operator == "-":
    return nu1 - nu2
  elif operator == "*":
    return nu1 * nu2
  elif operator == "/":
    return nu1 / nu2
  else:
    return "Invalid operator"

print("Welcome to the Calculator App")
while True:
  nu1 = float(input("Enter the first number: "))
  nu2 = float(input("Enter the second number: "))
  operator = input("Enter the operator: +,-,*,/")
  print(calculator(nu1, nu2, operator))
  choice = input("Do you want to continue? (y/n): ")
  if choice == "n":
    break