# import numpy as np

def main():

    arr = [35, 3, 5, 1, 10, 7, -3, 4]
    # arr = np.random.rand(200)
    arr = simple_sort(arr)
    
    print(arr)

def simple_sort(arr):
    checked_pos = 0
    length = len(arr)

    for i in range(length):
        # 対象とする範囲内での最小値を求める
        m = arr[i]
        min_pos = i
        for j in range(i, length):
            if arr[j] < m:
                m = arr[j]
                min_pos = j
        # print(arr, m, min_pos)
        # 入れ替える
        tmp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = tmp
    
    return arr

if __name__ == "__main__":
    main()