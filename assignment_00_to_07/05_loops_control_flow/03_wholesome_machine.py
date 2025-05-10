correct_affermation = "I am capable of doing anything. I put my mind too."

def main():
  print("Welcome to the Wholesome Machine")
  while True:
    user_input = input("Please type the following affermation:" + correct_affermation)
    if user_input == correct_affermation:
      print("That\'s right! ")
      break
    else:
      print("Hmmm That was not the affermation. Please Try Again!")

if __name__ == "__main__":
  main()