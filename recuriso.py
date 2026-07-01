for i in range(5, 0, -1):
    print(i)


for i in range(1, 6):
    print(i)


def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)
print(sum_numbers(6))


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(5))


word = "Hello"

for i in range(5):
    print(word)