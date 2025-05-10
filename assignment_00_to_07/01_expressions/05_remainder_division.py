def reminder():
  num1:int = int(input("Enter an integer to be divided: "))
  num2:int = int(input("Enter an integer to divide by: "))
  quotient:int = num1 // num2
  remainder:int = num1 % num2
  print(f'The result of following division is {quotient} with the reminder of {remainder}')

if __name__ == "__main__":
  reminder()
