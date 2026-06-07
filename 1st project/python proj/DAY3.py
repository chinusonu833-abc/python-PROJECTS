# Right Triangle
def right_triangle():
    for i in range(1, 6):
        print("*" * i)

# Hollow Square
def hollow_square():
    n = 5
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Inverted Triangle
def inverted_triangle():
    for i in range(5, 0, -1):
        print("*" * i)

#pyramid 
def pyramid():
    n=10
    for i in range(1,n+1):
        print(" " *(n-i) +"*"*(2*i-1) )
#inverted pyramid 



# Run only one pattern
right_triangle()
hollow_square()
inverted_triangle()
pyramid()