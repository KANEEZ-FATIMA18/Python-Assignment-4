Peturksbouipo:int = 16
Stanlau:int = 25
Mayengua:int = 48
age:int = int(input("How old are you?"))

def main():

  if age >= Peturksbouipo:
    print(f"Your age is {age}.you are eligible to vote in Peturksbouipo!")
  else:
    print(f"Your age is {age}.you are not eligible to vote in Peturksbouipo!")


if age >= Stanlau:
      print(f"Your age is {age}.you are eligible to vote in Stanlau!")
else:
      print(f"Your age is {age}.you are not eligible to vote in Stanlau!")


if age >= Mayengua:
      print(f"Your age is {age}.you are eligible to vote in Mayengua!")
else:
      print(f"Your age is {age}.you are not eligible to vote in Mayengua!")

if __name__ == "__main__":
  main()