# import numpy as np

def main():

    arr = [35, 3, 5, 1, 10, 7, -3, 4]
    # arr = np.random.rand(200)
    arr = bubble_sort(arr)
    
    print(arr)

def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        # 対象とする範囲内での最小値を求める
        for j in range(length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = tmp
    
    return arr

if __name__ == "__main__":
    main()