#liner search
def search(arr, x):
    # code here
    for index,val in enumerate(arr):
        if val == x:
            return index
        return -1
