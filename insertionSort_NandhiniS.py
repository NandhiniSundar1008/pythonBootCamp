'''
5,1,9,3,6,2,10
1,5,9,3,6,2,10
1,2,5,9,3,6,10
1,2,3,5,9,6,10
1,2,3,5,9,6,10
1,2,3,5,6,9,10
1,2,3,5,6,9,10
'''
'''
Pesudocode:
To find a minimum value.
    Consider the 0th index(start_idx) as a minimum value.
    Compare this minimum value with next element(j).
    If the minimumvalue is greater than next element then change this minimum value as j.
    Else do nothing.
    update the j value increment by 1. (j=j+1)
    Continue this process till j reach uptolen(arr)-1.
    Store the minimum value(mini), minimum index(mini_index).
Right shift the unsorted element before the minimum value.
    arr[mini_index] = arr[mini_index-1]
    arr[mini_index-1] = arr[mini_index-2]
    ...
    arr[start_idx+1] = arr[start_idx]
    mini_index = mini_index-1
    mini_index>start_idx+1
start_idx = start_idx+1
    Continue this process till start_idx reach upto len(arr)-1.
'''





def insertionSort(arr):
    # function to do insertion sort
    start_index = 0 # Set the start index in 0 (start value = 5, index = 0)
    while start_index<len(arr): # Continue this loop in start_index less than length of array (0<6)
        mini_index = start_index # Find the minimum value index, so in first step, first value is minimum number. so take the mini_index = 0(0 already assign in start_index). So mini_index = start_index
        j = start_index + 1 # Compare the elements. Create a j variable. j = 0 + 1.
        mini = arr[mini_index] # store a minimum value in mini. first step(mini = 5)
        while j<len(arr): # Continue this loop in j less than length of array.(1<6).
            if arr[mini_index]>arr[j]: # 5>1
                mini_index = j # mini_index = 1
            else:
                mini_index = mini_index # j is greater than mini_index then mini_index = mini_index
            j = j + 1 # Increment the j
            mini = arr[mini_index] # Store the minimum value in mini
        while mini_index>start_index: # Right shift the unsorted array. mini_index greater than start_index.
            arr[mini_index] = arr[mini_index-1]
            mini_index = mini_index-1
        arr[start_index] = mini # start index value stored in mini.
        start_index = start_index + 1 # Move to the next position.
    return arr

arr = [5,1,9,3,6,2,10]
print(insertionSort(arr))