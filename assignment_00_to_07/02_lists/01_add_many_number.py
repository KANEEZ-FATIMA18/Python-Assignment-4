def main():

    numbers: list[int] = [87, 23, 45, 67, 89, 12]

    sum_of_numbers: int = 0
    for number in numbers:
        sum_of_numbers += number
    print(f"The sum of the numbers is: {sum_of_numbers}")


if __name__ == "__main__":
    main()