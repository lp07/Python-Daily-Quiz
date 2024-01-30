for x in [1, 2]:
    for y in [1, 4]:
        if x!=y:
            print((y,x), end=" ")

# o/p: (4, 1) (1, 2) (4, 2)

# Explanation :
""" 
-> When x = 1 and y = 1, the condition x! = y is false (1 is equal to 1), so nothing is printed.
-> When x = 1 and y = 4, the condition x! = y is true, so it prints the tuple (4,1).
   Then the outer loop moves to the next value of x:
-> When x = 2 and y = 1, the condition x! = y is true, so it prints the tuple (1, 2).
-> When x = 2 and y = 4, the condition x! = y is true, so it prints the tuple (4, 2).

"""