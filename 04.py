# Selection Sort

def selection_sort(arr, n):
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    
    return arr

arr = [2,4,1,3,5,10,7,9,8,6]
result = selection_sort(arr,len(arr))
print(result)


            

