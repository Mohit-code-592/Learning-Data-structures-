# search inseret postion

def search_insert_postion(nums, target):
    n = len(nums)
    start = 0
    end = n - 1
    index = n

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            index = mid
            end = mid - 1
        
    return index
