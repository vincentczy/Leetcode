x = 123212
if x < 0 or (x > 0 and x % 10 == 0):
    print False
rev = 0
while x > rev:
    rev = rev * 10 + x % 10
    x //= 10
print x == rev or x == rev // 10