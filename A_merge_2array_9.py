'''
USED IN POINTERS
Sample:
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = []

Step 1:
Compare arr1[0] and arr2[0] = 2>1. small element 1(arr2[0]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1]

Step 2:
Compare arr1[0] and arr2[1] = 2<3. small element 2(arr1[0]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2]

Step 3:
Compare arr1[1] and arr2[1] = 5>3. small element 3(arr2[1]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3]

Step 4:
Compare arr1[1] and arr2[2] = 5>4. small element 4(arr2[2]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4]

Step 5:
Compare arr1[1] and arr2[3] = 5<8. small element 5(arr1[1]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5]

Step 6:
Compare arr1[2] and arr2[3] = 6<8. small element 6(arr1[2]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,6]

Step 7:
Compare arr1[3] and arr2[3] = 7<8. small element 7(arr1[3]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,6,7]

Step 8:
Compare arr1[4] and arr2[3] = 9>8. small element 8(arr2[3]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,6,7,8]

Step 9:
Compare arr1[4] and arr2[4] = 9<11. small element 9(arr1[4]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,7,8,9]

Step 10:
Compare arr1[5] and arr2[4] = 10<11. small element 10(arr[5]) moved to arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,6,7,8,9,10]

Step 11:
In arr1 no comparison elements but arr2 as remaning 2 elements. arr2 elements added in arr3.
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2,3,4,5,6,7,8,9,10,11,13]
'''
# PSEUDOCODE:
'''
Compare arr1 and arr2, 0th index value.
if arr1[0] < arr2[0], than minimum element arr1[0] moved in arr3.
arr1[0] increment to the next element arr1[1].
Else arr1[0] > arr2[0], then minimum element arr2[0] moved in arr3.
arr2[0] increment to the next element arr2[1].

Compare arr1 and arr2, 1st index value.
if arr1[1] < arr2[1], than minimum element arr1[1] moved in arr3.
arr1[1] increment to the next element arr1[2].
Else arr1[1] > arr2[1], then minimum element arr2[1] moved in arr3.
arr2[1] increment to the next element arr2[2].
# ...
# array 1 and array 2 all elements moved in array 3.
'''

# MAIN PSEUDDOCODE:
# Objective: Merge two sorted arrays into a single sorted array.
'''
Create new array to store the new sorted elements.(arr3)
Create i and j variables to consider the arr1 and arr2 index values.(i=0, j=0)
Compare the values in both arrays and store the minimum value to the new array(arr3).
Compare the values upto length of the arrays.
    if arr1[0] < arr2[0] (arr1 0th index value greater than of arr2 0th value).
    Store the arr1[0] to new array(arr3).
    Move to next element of arr1 ---> i = i + 1 ---> i = 0 + 1
    else: (arr1 0th index value less than of arr2 0th value).
    Store the arr2[0] to the new array(arr3).
    Move to next element of arr2 ---> j = j + 1 ---> j = 0 + 1.
Continue this loop in i and j len(arr).

If there any elements remaining in arr1 or arr2 then add this also in new array.
    while i<len(arr):
        stored the arr1[i] to the new array.(arr3)
        arr3 = arr3 + arr1[i]
    While j<len(arr):
        stored the arr2[j] to the new array.(arr3)
        arr3 = arr3 + arr2[j]
'''

arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = []
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3 = arr3 + [arr1[i]]
        i = i + 1
        #print(i)
        #print(arr3)
    else:
        arr3 = arr3 + [arr2[j]]
        j = j + 1
        #print(j)
        #print(arr3)

# Add remaining elements from arr1
while i < len(arr1):
    arr3 = arr3 + [arr1[i]]
    i = i + 1

# Add remaining elements from arr2
while j < len(arr2):
    arr3 = arr3 + [arr2[j]]
    j = j + 1

#print(arr1)
#print(arr2)
print(arr3)





'''
USED IN REMOVE FUNCTION.
Sample  arr1 = [2,5,6,7,9,10]
        arr2 = [1,3,4,8,11,13]
        arr3 = []
Step 1:
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = []
Compare arr1[0] and arr2[0] ---> 2>1 small element 1, moved in arr3 and element 1 removed in arr2.

Step 2:
arr1 = [2,5,6,7,9,10]
arr2 = [3,4,8,11,13]
arr3 = [1]
Compare arr1[0] and arr2[0] ---> 2<3 small element 2, moved arr3 and element 2 removed in arr1.

Step 3:
arr1 = [5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = [1,2]
Compare arr1[0] and arr2[0] ---> 5>3 small element 3, moved arr3 and element 3 removed in arr2.

Step 4:
arr1 = [5,6,7,9,10]
arr2 = [4,8,11,13]
arr3 = [1,2,3]
Compare arr1[0] and arr2[0] ---> 5>4 small element 4, moved arr3 and element 3 removed in arr2.

Step 5:
arr1 = [5,6,7,9,10]
arr2 = [8,11,13]
arr3 = [1,2,3,4]
Compare arr1[0] and arr2[0] ---> 5<8 small element 5, moved arr3 and element 5 removed in arr1.

Step 6:
arr1 = [6,7,9,10]
arr2 = [8,11,13]
arr3 = [1,2,3,4,5]
Compare arr1[0] and arr2[0] ---> 6<8 small element 6, moved arr3 and element 6 removed in arr1.

Step 7:
arr1 = [7,9,10]
arr2 = [8,11,13]
arr3 = [1,2,3,4,5,6]
Compare arr1[0] and arr2[0] ---> 7<8 small element 7, moved arr3 and element 7 removed in arr1.

Step 8:
arr1 = [9,10]
arr2 = [8,11,13]
arr3 = [1,2,3,4,5,6,7]
Compare arr1[0] and arr2[0] ---> 9>8 small element 8, moved arr3 and element 8 removed in arr2.

Step 9:
arr1 = [9,10]
arr2 = [11,13]
arr3 = [1,2,3,4,5,6,7,8]
Compare arr1[0] and arr2[0] ---> 9<11 small element 9, moved arr3 and element 9 removed in arr1.

Step 10:
arr1 = [10]
arr2 = [11,13]
arr3 = [1,2,3,4,5,6,7,8,9]
Compare arr1[0] and arr2[0] ---> 10<11 small element 10, moved arr3 and element 10 removed in arr1.

Step 11:
arr1 = []
arr2 = [11,13]
arr3 = [1,2,3,4,5,6,7,8,9,10]
Now, arr1 as empty list. arr2 as 11,13. arr2 elements moved arr3; elements are removed in arr2.

Step 12:
arr1 = []
arr2 = []
arr3 = [1,2,3,4,5,6,7,8,9,10,11,13]
'''

# PSEUDOCODE:
# Compare arr1 and arr2, 0th index value.
# if arr1[0]> arr2[0], than minimum element moved in arr3. Else arr1[0]<arr[0], then minimum element moved in arr3.
# Remove minimum element in array.
# ...
# array 1 and array 2 all elements moved in array 3.

# MAIN PSEUDOCODE:
# Objective: Merge two sorted arrays into a single sorted array.
'''
Create new array to store the new sorted elements.(arr3)
Create i and j variables to consider the arr1 and arr2 index values.(i=0, j=0)
Compare the values in both arrays and store the minimum value to the new array(arr3).
Compare the values upto length of the arrays.
    if arr1[0] < arr2[0] (arr1 0th index value greater than of arr2 0th value).
    Store the arr1[0] to new array(arr3).
    Remove the arr1 0th index value.
    else: (arr1 0th index value less than of arr2 0th value).
    Store the arr2[0] to the new array(arr3).
    Remove the arr2 0th index value.
Continue this loop in i and j len(arr).

If there any elements remaining in arr1 or arr2 then add this also in new array.
    while i<len(arr):
        stored the arr1[i] to the new array.(arr3)
        Removed the element in arr1.
    While j<len(arr):
        stored the arr2[j] to the new array.(arr3)
        Removed the element in arr2.
'''
'''
arr1 = [2,5,6,7,9,10]
arr2 = [1,3,4,8,11,13]
arr3 = []
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3 = arr3 + [arr1[i]]
        arr1.remove(arr1[i])
        print(arr1)
    else:
        arr3 = arr3 + [arr2[j]]
        arr2.remove(arr2[j])
        print(arr2)

# Add remaining elements from arr1
while i < len(arr1):
    arr3 = arr3 + [arr1[i]]
    arr1.remove(arr1[i])
    print(arr3)

# Add remaining elements from arr2
while j < len(arr2):
    arr3 = arr3 + [arr2[j]]
    arr2.remove(arr2[j])
    print(arr3)

#print(arr1)
#print(arr2)
print(arr3)
'''
