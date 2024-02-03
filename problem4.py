my_list = ["", "", None] # A list that has two empty string and a None value

if my_list[0] and my_list[2]: # Check if first [index 0] and third [index 2] element has true
    print("January has flown by")
elif len(my_list) > 1: # If above condition is not met, check length of the list greater than one
    print("2024 still my year")
else: # If none of the condition is not met, exclude the following code.
    print("GitHub is loading")


# o/p : 2024 still my year