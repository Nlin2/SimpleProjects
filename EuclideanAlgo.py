# Find the GCD
# Nick Lin
print('This algorithm finds the greatest common denominator of two positive integers')
n = int(input('Enter the first number: '))
m = int(input('Enter the second number: '))
assert isinstance(n, int) and isinstance(m, int)
assert n > 0 and m > 0

# n to be the greater of the two numbers
if m > n:
    n, m = m, n

# Special case - n == m
if n == m:
    print(n)
else:
    # r = remainder
    r = n % m
    # if m is a denominator of n
    if r == 0:
        print(m)
    else:
        while r > 0:
            previous = r
            r = n % m
            n = m
            m = r
        print(previous)


