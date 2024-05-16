'''def binarySearch(arr,value):     # Basic program output comes from True or False
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start + end) //2
        if arr[mid]==value:
            return True
        elif arr[mid]<value:
            start = mid + 1
        elif arr[mid]>value:
            end = mid - 1
            return False'''
        
def binarySearch(arr,value):
    start = 0 # Set the starting index of the search range to the beginning of the array.
    end = len(arr)-1 # Set the ending index of the search range to the end of the array.
    while start<=end: # Continue searching as long as the start index is less than or equal to the end index.
        mid = (start + end) //2 # Calculate the midpoint index of the current search range.
        if arr[mid]==value: # If the value at the midpoint is equal to the target value, return the index of the midpoint.
            return mid 
        elif arr[mid]<value: #If the value at the midpoint is less than the target value, update the start index to search in the right half of the array.
            start = mid + 1
        else:
            end = mid - 1 # If the value at the midpoint is greater than the target value, update the end index to search in the left half of the array.
    return False # If the target value is not found in the array, return False.
arr = [8,10,18,55,108,111,204,607,1008]
value = int(input(": "))
result = binarySearch(arr,value) # function call
print(result)