'''
arr = [2,5,9,13,18,21,25,29,35,39,41]
value = 39
Find the mid value in array.
    formula = mid = (start+end)//2
    mid = (0+10)//2
    mid index = 5
    mid value = 21
    left = 0(2); Right = 10(41); mid = 5(21)
Compare value and mid value ---> 39>21
    21 and 21 left side elements are not consider(2,5,9,13,18,21)
Now array = [25,29,35,39,41]
value = 39
    mid = (6+10)//2 ---> 8
    mid index = 8
    mid value = 35
    left = 6(25); Right = 10(41); mid = 8(35) 
Compare value and mid value ---> 39>35
    35 and 35 left side elements are removed(25,29,35).
Now array = [39,41]
value = 39
    mid = (9+10)//2--->9
    mid index = 9
    mid value = 39
Compare value and mid value ---> 39 == 39
return mid
    Left = 9(39); Right = 10(41); mid = 9(39)
'''





def binarySearch(arr, value):
    # write code to search for the value and return index in which it is found.
    # if not found return -1
    start = 0 # Set the starting index.
    end = len(arr)-1 # Set the ending index in len(arr)-1.
    while start<=end: # Continue this loop in start index is less than or equal to the end index.
        mid = (start + end) //2 # Calculate the midpoint index of the current search range.
        if arr[mid]==value: # If the value and the midpoint is equal then return the mid.
            return mid 
        elif arr[mid]<value: #If the value and the midpoint is less than the value, update the start index to search in the right half of the array.
            start = mid + 1
        else:
            end = mid - 1 # If the value and the midpoint is greater than the value, update the end index to search in the left half of the array.
    return -1 # value is not present in array return -1.

arr = [2,5,9,13,18,21,25,29,35,39,41]
value = 39
print(binarySearch(arr, value))
