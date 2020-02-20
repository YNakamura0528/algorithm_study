import sys


def main():
    arr = [11, 13, 18, 19, 23, 26, 32, 49, 50, 90, 129, 149]
    print("input arr :", arr)

    hash_list = get_hash_list(arr)
    print("hash_list :", hash_list)
    
    target = int(sys.argv[1])
    print("target :", target)

    pos = hash_search(hash_list, target)
    if pos:
        print(target, "is at index", pos)
    else:
        print("no answer")

def get_hash_list(arr):
    hash_list = [0] * len(arr) * 2
    hash_len = len(hash_list)
    
    # hash_listに格納する
    for i in range(len(arr)):
        temp_pos = arr[i] % hash_len
        while hash_list[temp_pos] != 0:
            temp_pos += 1
            if temp_pos > hash_len:
                temp_pos = 0
        hash_list[temp_pos] = arr[i]
    return hash_list
    
def hash_search(hash_list, target):
    hash_len = len(hash_list)
    #探索する
    temp_pos = target % hash_len
    while hash_list[temp_pos] != 0:
        if hash_list[temp_pos] == target:
            return temp_pos
        else:
            temp_pos += 1
    else:
        return False


if __name__ == "__main__":
    main()