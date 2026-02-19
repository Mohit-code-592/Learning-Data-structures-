# bubble sort
def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [2,4,1,3,5,10,7,9,8,6]
result = bubble_sort(arr,len(arr))
print(result)
