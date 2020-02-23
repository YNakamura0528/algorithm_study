# import numpy as np

def main():

    arr = [35, 3, 5, 1, 10, 7, -3, 4]
    # arr = np.random.rand(200)
    arr = insertion_sort(arr)
    
    print(arr)

def insertion_sort(arr):
    length = len(arr)

    for checked_pos in range(length - 1):
        minimum = arr[0]
        maximum = arr[checked_pos]

        if arr[checked_pos + 1] < minimum:
            tmp = arr[checked_pos + 1]
            arr[1 : checked_pos + 2] = arr[0 : checked_pos + 1]
            arr[0] = tmp
        elif arr[checked_pos] > maximum:
            continue
        else:
            x = arr[checked_pos + 1]
            k = checked_pos
            
            while k >= 0:
                if arr[k] > x:
                    arr[k + 1] = arr[k]
                    k -= 1
                else:
                    break
            arr[k + 1] = x
            
    return arr

if __name__ == "__main__":
    main()