# insertion sort
def insertion_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1,0,-1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

arr = [2,4,1,3,5,10,7,9,8,6]
insertion_sort(arr, len(arr))
print(arr)     
