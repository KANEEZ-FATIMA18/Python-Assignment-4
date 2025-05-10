import random

def main():
  secret_number = random.randint(1,10)
  print("I am thinking of a number between 1 and 10....")

  guess = int(input("Enter a guess: "))

  while guess != secret_number:
    if guess < secret_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")
    guess = int(input("Enter a guess: "))

  print(f"Congratulation! The number was {secret_number}")


if __name__ == "__main__":
  main()
     