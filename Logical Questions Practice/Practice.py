# challenge = 'thirty'
# print(challenge[::-1])

def square_sum(numbers):
    #your code here
    for i in numbers:
        sum_total = i**i + i*i + i*i
        return sum_total

square_sum(1, 2, 2)