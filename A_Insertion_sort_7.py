'''
2,9,5,1,7,6,3
1,2,9,5,7,6,3
1,2,3,9,5,7,6
1,2,3,5,9,7,6
1,2,3,5,6,9,7
1,2,3,5,6,7,9
'''
'''
array = [2,9,5,1,7,6,3]
1) minimum = 1 ; index = 3
move 2nd index ---> 3d index : 2,9,5,5,7,6,3
move 1st index ---> 2nd index : 2,9,9,5,7,6,3
move 0th index ---> 1 index : 2,2,9,5,7,6,3
move minimum ---> 0th index : 1,2,9,5,7,6,3
 after 1st loop array = [1,2,9,5,7,6,3]

2) minimum = 2 ; index = 1
move 1st index ---> 1st index : 1,2,9,5,7,6,3
    after 2nd loop array = [1,2,9,5,7,6,3]

3) minimum = 3 ; index = 6
move 5th index ---> 6th index : 1,2,9,5,7,6,6
move 4th index ---> 5th index : 1,2,9,5,7,7,6
move 3d index ---> 4th index : 1,2,9,5,5,7,6
move 2nd index ---> 3nd index : 1,2,9,9,5,7,6
move minimum ---> 2 nd index : 1,2,3,9,5,7,6
  after 3d loop array = [1,2,3,9,5,7,6]

4) minimum = 5 ; index = 4
move 3d index ---> 4th index : 1,2,3,9,9,7,6
move minimum ---> 3d index : 1,2,3,5,9,7,6
  after 4th loop array = [1,2,3,5,9,7,6]

5) minimum = 6 ; index = 6
move 5th index ---> 6th index : 1,2,3,5,9,7,7
move 4th index ---> 5th index : 1,2,3,5,9,9,7
move minimum ---> 4th index : 1,2,3,5,6,9,7
   after 5th loop array = [1,2,3,5,6,9,7]

minimum = 7 ; index = 6
move 5th index ---> 6th index : 1,2,3,5,6,9,9
move minimum ---> 5th index : 1,2,3,5,6,7,9
   Final output array = [1,2,3,5,6,7,9]
'''
# Objective: To sort a given array in ascending order
# To find a minimum value.
  # Consider the 0th index(start_index) as the minimum value.
  # Compare this minimum value with next element(j).
  # If the minimum value is greater than next element change this minimum value as j. Else do nothing.
  # update the j value increment by 1.(j=j+1).
  # Continue this process till j reach upto len(arr)-1.
  # Store the minimum value(minimum), minimum index(mini_index).
# Right shift the unsorted elements before the minimum value.
  # arr[min_index]=arr[min_index-1]
  # arr[min_index-1]=arr[min_index-2]
  # ...
  # arr[start_index+1]=arr[start_index]
  # min_index = min_index-1
  # min_index>start_index
# start_index = start_index+1
  # Continue this process till start_index reach upto len(arr)-1.

arr = [2,9,5,1,7,6,3]
start_index = 0
while start_index<len(arr):
  min_index = start_index
  j = start_index+1
  minimum = arr[min_index]
  while j<len(arr):
    if arr[min_index]>arr[j]:
      min_index = j
    else:
      min_index = min_index
    j=j+1
    minimum = arr[min_index]
  while min_index>start_index:
    arr[min_index]=arr[min_index-1]
    min_index = min_index-1
  arr[start_index] = minimum
  start_index = start_index+1
print(arr)
  