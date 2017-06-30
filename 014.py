strs = ["abc", "ab", "acdd"]
print(min(strs))

for index, item in enumerate(zip(*strs)):
    if len(set(item)) > 1:
        print(strs[0][:index])
else:
    print(min(strs))


# if strs is None or len(strs) == 0:
#     print ""
# if len(strs) == 1:
#     print strs[0]
# for i in range(len(strs[0])):
#     for j in range(len(strs) - 1):
#         if strs[j][i] != strs[j + 1][i]:
#             print strs[0][:i-1]
#             break
# print ""
