def hcf(num1, num2):
    assert num1 >= 0 and int(num1) == num1, "Numbers should be a positive integer"
    assert num2 >= 0 and int(num2) == num2, "Numbers should be a positive integer"
    smallerNum = min(num1, num2)
    if(smallerNum <= 1):
        return 1
    divisor = 2
    while(True):
        if(num1%divisor == 0 and num2%divisor == 0):
            return divisor*hcf(num1/divisor, num2/divisor)
        if(divisor == smallerNum):
            break
        divisor += 1
    return 1

print(hcf(48,18))