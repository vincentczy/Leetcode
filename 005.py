s = "babad"
length = len(s)
tup = (0, 0, 0)
for i in range(length):
    if i + 1 < length and s[i] == s[i + 1]:
        offset = 1
        while i - offset >= 0 and i + 1 + offset < length:
            if s[i - offset] == s[i + 1 + offset]:
                offset += 1
            else:
                break
        offset -= 1
        length_of_sub = offset * 2 + 2
        if length_of_sub > tup[0]:
            tup = (length_of_sub, i - offset, i + 1 + offset)
    offset = 1
    while i - offset >= 0 and i + offset < length:
        if s[i - offset] == s[i + offset]:
            offset += 1
        else:
            break
    offset -= 1
    length_of_sub = offset * 2 + 1
    if length_of_sub > tup[0]:
        tup = (length_of_sub, i - offset, i + offset)
print s[tup[1]:tup[2] + 1]
