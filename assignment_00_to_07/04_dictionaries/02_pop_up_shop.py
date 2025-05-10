def calculate_total_cost():
  fruits_price = {
      "apple":5.0,
      "mango":15.0,
      "kiwi":8.0,
      "pear":12.0,
      "banana":6.0,
      "orange":10.0
  }

  total_cost = 0

  for fruit,price in fruits_price.items():
    while True:
      try:
        quantity = int(input(f'How many {fruit} do you want?: '))
        if quantity < 0:
          print("Invalid input. Please enter a non-negative number.")
          continue
        total_cost += price * quantity
        break
      except ValueError:
        print("Invalid input. Please enter a valid number.")

    print(f"\n Your total cost is: ${total_cost:.2f}")

if __name__ == "__main__":
  calculate_total_cost()
