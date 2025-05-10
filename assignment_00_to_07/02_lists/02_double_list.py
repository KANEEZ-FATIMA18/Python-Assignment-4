def main():

    single_list :list[int] = [1, 2, 3, 4, 5]


    for i in range(len(single_list)):
        single_list[i] = single_list[i] * 2

    print(single_list)

if __name__ == "__main__":
    main()