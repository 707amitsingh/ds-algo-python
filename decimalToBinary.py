def decimalToBinary(num):
    assert num >= 0 and int(num) == num, "Number should be a positive integer"
    if(num == 0):
        return 0
    return 10*decimalToBinary(int(num/2)) + num%2

print(decimalToBinary(13))