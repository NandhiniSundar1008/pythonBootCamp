'''1) Given array find the mid value.
    mid_index = len(arr)//2
2) Divide by two array in minimum of the value(left and right)
    left_half = arr[:mid_index]--->[10,6,2,4]
    right_half = arr[mid_index:]--->[8,5,3,1]
3) Use merge_sort function store the sorted elements in left and right side.
4) Use merge function merge left and right side element in sorted.'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_index = len(arr)//2     # Find the mid value
    left_half = arr[:mid_index]
    right_half = arr[mid_index:]
    left_half = merge_sort(left_half)   #  level 1[10,6,2,4]---level 2[2,4] level 3[2]
    right_half = merge_sort(right_half) # level 3[4]---[6,10]
    print(left_half)
    print(right_half)
    return merge(left_half,right_half)   # Function call
def merge(left_half,right_half):
    result = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

# Add remaining elements from arr1
    while i < len(left_half):
        result.append(left_half[i])
        i += 1

# Add remaining elements from arr2
    while j < len(right_half):
        result.append(right_half[j])
        j += 1
    return result

arr = [10,6,2,4,8,5,3,1]
sorted_arr = merge_sort(arr)
print(sorted_arr)