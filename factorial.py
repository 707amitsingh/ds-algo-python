def factorial(n):
    assert n >= 0 and int(n) == n, "number must be positive integer only!"
    if n in [0,1]:
        return 1
    return n*factorial(n-1)

num = input("Enter the number:")
value = factorial(int(num))
print("factorial of {num} is:", value)