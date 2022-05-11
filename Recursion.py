# Recursion is slow and takes more space
# Is not good when we want algorithm to be fast and take less space
# Good when we can divide problem into smaller problems

# %%
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0, 1]:
        return 1
    return n * factorial(n-1)


print(factorial(6))
# print(factorial(-10))
print(factorial(10))

# %%


def fibonacci(n):
    assert n >= 0 and int(
        n) == n, 'Fibonacci number must be positive integer only!'
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(4))
print(fibonacci(3))
print(fibonacci(5))

# %%


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n == 0:
        return 0
    return int(n % 10) + sumOfDigits(int(n//10))


sumOfDigits(133)

# %%


def powerOfNumber(base, exp):
    assert exp >= 0 and int(
        exp) == exp, 'The exponent must be positive integer only!'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * powerOfNumber(base, exp-1)


# %%
powerOfNumber(5, 4)
powerOfNumber(5.4, 3)
powerOfNumber(-5.4, 3)

# %%


def gcd(x, y):
    assert int(x) == x and int(
        y) == y, 'The exponent must be positive integer only!'
    x, y = abs(x), abs(y)
    if y == 0:
        return x
    return gcd(y, x % y)


gcd(-48, 18)
# %%


def decimalToBinary(n):
    assert int(n) == n, 'The number must be positive integer only!'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


decimalToBinary(13)
# decimalToBinary(13.2)

# %%
