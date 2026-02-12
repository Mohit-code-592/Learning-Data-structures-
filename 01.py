# Find Unique Element
def find_single_ele(arr):
    ans = 0
    for i in arr:
        ans = ans ^ i
    print(ans)

arr = [1,2,3,1,4,3,2]



"""
Description:

Given an array where every element appears twice except one, find that single element using XOR.

🔹 Approach:
We use the property of XOR:

a ^ a = 0

a ^ 0 = a

By XOR-ing all elements of the array, duplicate elements cancel out and the unique element remains.

⏱ Time Complexity: O(n)
💾 Space Complexity: O(1)
"""
