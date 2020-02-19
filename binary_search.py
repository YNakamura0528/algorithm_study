import sys

arr = [11, 13, 18, 19, 23, 26, 32, 49, 50, 90, 129, 149]

pos = len(arr) // 2
ans = int(sys.argv[1])

lower, upper = 0, len(arr) - 1

while lower <= upper:
    if arr[pos] == ans:
        print(ans, "is at", pos)
        break
    elif arr[pos] > ans:
        upper = pos - 1        
    else:
        lower = pos + 1

    pos = (lower + upper) // 2
    
else:
    print("no answer")


