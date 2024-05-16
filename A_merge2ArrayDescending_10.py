# PSEUDOCODE:
'''
Compare arr1 and arr2, 4th index and 0th index value.
if arr1[4] < arr2[0], than largest element arr2[0] moved in arr3.
arr2[0] increment to the next element arr1[1].
Else arr1[4] > arr2[0], then largest element arr1[4] moved in arr3.
arr2[4] decrement to the next element arr2[3].

Compare arr1 and arr2, 3d index and 1st index value.
if arr1[3] < arr2[1], than largest element arr2[1] moved in arr3.
arr2[1] increment to the next element arr1[2].
Else arr2[1] > arr1[3], then largest element arr1[3] moved in arr3.
arr2[1] decrement to the next element arr2[2].
# ...
# array 1 and array 2 all elements moved in array 3.
'''

# MAIN PSEUDDOCODE:
# Objective: Merge two sorted arrays into a single sorted array.
'''
Create new array to store the new sorted elements.(arr3)
Create i and j variables to consider the arr1 and arr2 index values.(i=len(arr)-1, j=0)
Compare the values in both arrays and store the largest value to the new array(arr3).
Compare the values upto length of the arrays.
    if arr1[4] > arr2[0] (arr1 4th index value less than of arr2 0th value). ---> arr1[i] > arr2[j]
    Store the arr1[4] to new array(arr3).
    Move to next element of arr1 ---> i = i - 1 ---> i = 4 - 1
    else: (arr1 4th index value greater than of arr2 0th value).
    Store the arr2[0] to the new array(arr3).
    Move to next element of arr2 ---> j = j + 1 ---> j = 0 + 1.
Continue this loop in i in greater than or equal to 0 and j len(arr2).

If there any elements remaining in arr1 or arr2 then add this also in new array.
    while i>0:
        stored the arr1[i] to the new array.(arr3)
        arr3.append(arr1[i])
    While j<len(arr2):
        stored the arr2[j] to the new array.(arr3)
        arr3.append(arr2[j])
'''

arr1 = [3,6,7,8,9]
arr2 = [10,5,4,2,1]
arr3 = []

i = len(arr1) - 1
j = 0

# Merge arr1 and arr2 while maintaining their orders
while i >= 0 and j < len(arr2):
    if arr1[i] > arr2[j]:
        arr3.append(arr1[i])
        i -= 1
    else:
        arr3.append(arr2[j])
        j += 1

# Add remaining elements from arr1
while i >= 0:
    arr3.append(arr1[i])
    i -= 1

# Add remaining elements from arr2
while j < len(arr2):
    arr3.append(arr2[j])
    j += 1
print(arr3)
