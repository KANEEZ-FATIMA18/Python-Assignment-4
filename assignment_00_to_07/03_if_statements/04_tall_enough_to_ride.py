min_height:int = 50
def main():
  user:int = int(input("How tall are you? "))
  if user >= min_height:
    print("you are tall enough to ride")
  else:
    print("you are not tall enough to ride.May be next year.")

if __name__ == "__main__":
  main()