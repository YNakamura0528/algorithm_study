import sys


def main():
    arr = [11, 13, 18, 19, 23, 26, 32, 49, 50, 90, 129, 149]
    target = int(sys.argv[1])
    print("arr is", arr)
    pos = binary_search(arr, target)
    if pos:
        print(target, "is at index", pos)
    else:
        print("no answer")

def binary_search(arr, target):
    lower, upper = 0, len(arr) - 1
    pos = len(arr) // 2
    while lower <= upper:
        if arr[pos] == target:
            return pos
        elif arr[pos] > target:
            upper = pos - 1        
        else:
            lower = pos + 1

        pos = (lower + upper) // 2
        
    else:
        return False

if __name__ == "__main__":
    main()