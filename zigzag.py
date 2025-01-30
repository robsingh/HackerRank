def findZigZagSequence(arr):
    arr.sort()
    n = len(arr)
    mid = int((n+1)/2) - 1
    arr[mid], arr[n-1] = arr[n-1], arr[mid]
    
    st = mid + 1
    ed = n - 2

    while (st <= ed):
        arr[st], arr[ed] = arr[ed], arr[st]
        st += 1
        ed -= 1
    
    return arr
   
arr = [2,3,5,1,4,7,6]
print(findZigZagSequence(arr))