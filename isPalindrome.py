def isPalindrome(str):
    if(len(str) == 1 or len(str) == 0):
        return True
    if(str[0] == str[-1]):
        return isPalindrome(str[1:-1])
    return False

print(isPalindrome('cattac'))