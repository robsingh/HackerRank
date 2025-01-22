def countingSort(arr):
    freq = [0] * 100

    for num in arr:
        freq[num] += 1
    return freq


arr = [1,1,3,2,1]
print(countingSort(arr))