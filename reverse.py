def reverse(str):
    if(len(str) == 0):
        return ''
    return str[-1] + reverse(str[:-1])

print(reverse("python"))