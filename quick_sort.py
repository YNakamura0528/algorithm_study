# import numpy as np

def main():

    arr = [35, 3, 5, 1, 10, 7, -3, 4]
    # arr = np.random.rand(200)
    arr = quick_sort(arr)
    
    print(arr)

def quick_sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    
    if left >= right: return arr

    i = left + 1
    j = right

    while i < j:
        # print(arr, i, j)
        while arr[i] < arr[left] and i < right:
            i += 1
        while arr[j] > arr[left] and j > left:
            j -= 1
        
        if i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    if arr[left] > arr[j]:
        tmp = arr[left]
        arr[left] = arr[j]
        arr[j] = tmp

    arr = quick_sort(arr, left, j - 1)
    arr = quick_sort(arr, j + 1, right)

    return arr

if __name__ == "__main__":
    main()