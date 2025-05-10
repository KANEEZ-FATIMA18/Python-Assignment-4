MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)


def main():
    sample_list = [1, 2, 3, 4, 5]
    shorten(sample_list)
    print("Final list:", sample_list)

if __name__ == "__main__":
    main()

