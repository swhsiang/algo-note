# Implement insertion sort
def sort(arr=[]):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr


def main():
    test_arr = [1, 34, 51, 100, 31, 51, 16, 56]
    print(test_arr)
    test_arr = sort(test_arr)
    print(test_arr)


main()
