import random

NUM_SIDES = 6

def roll_dice():
   dice1 = random.randint(1, NUM_SIDES)
   dice2 = random.randint(1, NUM_SIDES)

   total= dice1 + dice2
   print(f"Die 1: {dice1} Die 2: {dice2} Total: {total}")
    
def main():
   
   dice1 = 10

   print(f"dice1 in main strat as {dice1}")

   for _ in range(3):
      roll_dice()
      print(f"dice1 in main is still {dice1}")

if __name__ == "__main__":
   main()      
