def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "Number should be a positive integer"
    num = n
    if(num == 0):
        return 0 
    return num%10 + sumOfDigits(int(num/10))

print(sumOfDigits(1234165165165165))