def multiply_digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product
def reduce_number(n):
    while n > 9:
        n = multiply_digits(n)
    return n
user_input = int(input('Enter a number: '))

if user_input == 0:
    print('The number must be a non-negative integer.')
else:
    print(reduce_number(user_input))
