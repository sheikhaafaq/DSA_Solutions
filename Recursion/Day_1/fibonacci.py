# -----------------   FIBONACII USING LOOP-----------------------

def fibonacci_loop(n):
    
    # Initialize basic two terms
    first = 0   
    second = 1

    # Base  condition
    if n <= 1:
        print("Enter value greater than 1")
        return n
    else:
        print(f"{first}, {second}", end=", ")

        # Loop runs untill next reach to n 
        for i in range(2, n):
            next = first + second
            first = second
            second = next
            print(next,end= ', ')

# Function call
fibonacci_loop(int(input("Enter the Value of nth term >> ")))


# -----------------   FIBONACII USING RECURSION  ----------------------

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

nthTerm  = int(input("\nEnter the Value of nth term >> "))
for i in range(nthTerm):  
   print(fibonacci_recursion(i), end=", ")
