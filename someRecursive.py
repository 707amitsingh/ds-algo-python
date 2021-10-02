def someRecursive(arr,cb):
    if(len(arr) == 0):
        return False
    lastElement = arr.pop()
    if(cb(lastElement) == True):
        return True
    else:
        return someRecursive(arr, cb)

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(someRecursive([4,6,8,10], isOdd))
    
