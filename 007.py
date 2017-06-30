x = -123
s = cmp(x, 0)
r = int(`s*x`[::-1])
print s*r*(r < 2 ** 31)