def recursiveRange(num):
    assert num >= 0 and int(num) == num, "Number should be a positive integer"
    if(num == 0):
        return 0
    return num + recursiveRange(num-1)

print(recursiveRange(10))