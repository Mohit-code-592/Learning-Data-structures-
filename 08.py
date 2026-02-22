# Find First and Last Position of Element in Sorted Array
def brute_force(nums, n, target):
    is_present = False
    first_occurence = -1
    last_occurence = -1
    for index, val in enumerate(nums):
        if val == target:
            first_occurence = index
            is_present = True
            break
    
    if is_present:
        for j in range(n - 1, -1, -1):
            if nums[j] == target:
                last_occurence = j
                break
        
    return [first_occurence, last_occurence]

def using_binary_search(nums, n, target):
    start , end = 0, n - 1
    first_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            first_index = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    last_index = -1
    start , end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            last_index = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1    
        
    return [first_index, last_index]
    

nums = [5, 7, 7, 8, 8, 10]
result = brute_force(nums, len(nums), 8) 
result1 = using_binary_search(nums, len(nums), 8)  
print(result1)


