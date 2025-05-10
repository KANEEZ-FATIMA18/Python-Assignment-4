import math

def triangle():
  ab:float = float(input("Enter the length of the side ab. "))
  ac:float = float(input("Enter the length of the side ac. "))
  bc:float = math.sqrt(ab**2 + ac**2)
  print(f'The length of bc (the hypothenuse is : {bc})')

if __name__=="__main__":
  triangle()