height = [1,3,4]
start = 0
end = len(height) - 1
maxVol = 0
while start < end:
    vol = min(height[start], height[end]) * (end - start)
    maxVol = max(maxVol, vol)
    if height[start] < height[end]:
        start += 1
    else:
        end -= 1
print maxVol
