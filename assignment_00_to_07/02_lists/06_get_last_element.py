def get_last_element(lst):
    print(lst[-1])  # last element ko print karte hain

# List input lena user se
lst = []
while True:
    element = input("Enter an element (or 'done' to finish): ")
    if element == 'done':
        break
    lst.append(element)

# Function call
get_last_element(lst)
