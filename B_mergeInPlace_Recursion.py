'''Objective: Write a function to merge both subarrays in place.
Take a array
Split in left and right side.
Left side first element take the "first"
Right side first element take the "second"
Compare the first and second.
    first <= second
    Increment the first.
    call the function "mergeInplace(arr, first+1, second, end)".
Otherwise first > second.
else:
    Store the second value in temp.
    Right shift all values present before the temp.
    arr[i]=arr[i-1]
    arr[i-1]=arr[i-2]
    ...
    arr[first+1]=arr[first]
    assign arr[first] = temp
    Increment first and second.
    call the function "mergeInplace(arr, first+1, second+1, end)"
Break the recursion in "Left array reached or overtaken the right array" or "end is greater than second"
    if first>=second or second>end.
    return array'''


'''def mergeInplace(arr, first, second, end):
    if first >= second or second > end:   # left subarray reached or overtaken the right subarray or second greater than to end
        return arr
    if arr[first] <= arr[second]:
        mergeInplace(arr, first+1, second, end)    # function call
    else:
        temp = arr[second]
        i = second
        while i > first:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[first] = temp
        mergeInplace(arr, first+1, second+1, end)  # function call
arr = [5,18,30,12,24,36]
mergeInplace(arr, 0, 3, len(arr)-1)
print(arr)'''

'''5,18,30,12,24,36
5,12,18,30,24,36
5,12,18,30,24,36
5,12,18,24,30,36
5,12,18,24,30,36'''




def mergeInplace(arr, first, second, end):
    while first < second and second <= end:
        if arr[first] <= arr[second]:
            first = first + 1
        else:
            temp = arr[second]
            i = second
            while i > first:
                arr[i] = arr[i - 1]
                i = i - 1
            arr[first] = temp
            first = first + 1
            second = second + 1

arr = [5,18,30,12,24,36]
mergeInplace(arr, 0, 3, len(arr)-1)
print(arr)

'''Examples:
    9,12,15,2,5,7
    5,18,30,12,24,36
    2,4,6,1,3,5
    1,3,5,2,4,6'''