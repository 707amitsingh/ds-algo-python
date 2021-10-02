def power(n,p):
    assert p >= 0 and int(p) == p, "Power should be a positive integer"
    if(p == 0):
        return 1
    return n*power(n,p-1)

print(power(25,1))