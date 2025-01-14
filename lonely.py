def lonely_integer(arr):
    store = {}
    
    for element in arr:
        if element in store:
            store[element] += 1
        else:
            store[element] = 1
        

    for key,value in store.items():
        if value == 1:
            return key
        
arr = [1,2,3,4,3,2,1]
print(lonely_integer(arr))