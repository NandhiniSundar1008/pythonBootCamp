'''
9,3,5,7,8,1,2
1,3,5,7,8,9,2
1,2,5,7,8,9,3
1,2,3,7,8,9,5
1,2,3,5,8,9,7
1,2,3,5,7,9,8
1,2,3,5,7,8,9
1,2,3,5,7,8,9
'''
# Objective: To sort a given array in ascending order.
# Find the minimum number in given array.
    # Consider the 0th index(i) as the minimum value.
    # Compare this minimum value with next element(j).
    # If the minimum value is greater than next element change this minimum value as j. Else do nothing.
    # update the j value increment by 1.(j=j+1).
    # Continue this process till j reach upto len(arr)-1(n).
# Swap values in the first index of search array with a value in mininum index.
# incremanet the start value by 1.(i=i+1).
# Continue this process upto end of the array.
arr = [9,3,5,7,8,1,2]
i = 0
n = len(arr)-1  # len(arr)-7, len(arr)-1-6
print(arr)
while i<n:
    mini = i  # set a mini value as i
    j = i + 1 
    print(arr[mini])
    print(arr[j])
    while j<=n: # Compare the j value with mini upto n.
        if arr[mini]>arr[j]: # When the mini value is greater then remaining numbers.
            mini = j
        j=j+1
    arr[i],arr[mini]=arr[mini],arr[i] # Replace the mini and i index values.
    print(arr[i],arr[mini])
    i=i+1
print(arr)

print("Helloworld")