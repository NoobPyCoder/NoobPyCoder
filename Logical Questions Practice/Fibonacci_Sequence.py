# def fibonacci_sequence(n): #defining the function
#     a = 0 #value intialization
#     b = 1 #value intialization
#     if n == 1: # limiting the n value to 0 if someone want only the first number of fibonacci
#         print(a)
#     else: #using else to delimit the upper statement
#         print(a)
#         print(b)
#         for i in range (2, n): #using for loop to iterate the numbers to get added and swaped when needed
#             c = a + b
#             a = b
#             b = c
#             print (c)

# fibonacci_sequence(5)

#using recursive method
def fibonacci_of(n):
        if n in (0, 1):
            return n
        return fibonacci_of(n-1) + fibonacci_of(n-2) 

[fibonacci_of(n) for n in range (5)]