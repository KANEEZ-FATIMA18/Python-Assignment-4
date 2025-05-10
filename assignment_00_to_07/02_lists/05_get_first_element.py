def get_first_element(lst):
    print(lst[0])  


lst = []
while True:
    element = input("Enter an element (or 'done' to finish): ")
    if element == 'done':
        break
    lst.append(element)

# Function call
get_first_element(lst)



