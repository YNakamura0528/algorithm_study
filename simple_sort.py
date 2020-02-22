

def main():
    arr = [35, 3, 5, 1, 10, 7, -3, 4]
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
    
    print(arr)

if __name__ == "__main__":
    main()