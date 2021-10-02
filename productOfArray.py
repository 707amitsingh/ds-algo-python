def productOfArray(arr):
    if(len(arr) == 0):
        return 1
    lastElement = arr.pop()
    return lastElement*productOfArray(arr)

print(productOfArray([1,2,3,4,5,5]))