def xthBiggest(arr,x):
    for i in range(1,x):
        arr.remove(max(arr))
    return max(arr)   

print(xthBiggest([1,2,3,4,5,6,7],1)) 