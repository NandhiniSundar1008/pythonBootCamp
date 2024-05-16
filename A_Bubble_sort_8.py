'''
samples: 2,9,5,1,7,6

Step 0:
    compare 2 and 9 ---> 2<9. No swap.
    compare 9 and 5 ---> 9>5. Swap both elements [2,5,9,1,7,6]
    compare 9 and 1 ---> 9>1. Swap both element [2,5,1,9,7,6]
    compare 9 and 7 ---> 9>7. Swap both element [2,5,1,7,9,6]
    compare 9 and 6 ---> 9>6. Swap both element [2,5,1,7,6,9]
    After the step 1 largest element (9) is stroed in correct position. Freeze (9).
Step 1:[2,5,1,7,6,9]
    compare 2 and 5 ---> 2<5. No swap.
    compare 5 and 1 ---> 5>1. Swap both element. [2,1,5,7,6,9]
    compare 5 and 7 ---> 5<7. No swap.
    compare 7 and 6 ---> 7>6. Swap both element. [2,1,5,6,7,9]
    After the step 2, 2nd largest element(7) is stored in correct position. Freeze (7,9)
Step 2:[2,1,5,6,7,9]
    compare 2 and 1 ---> 2>1. Swap both element. [1,2,5,6,7,9]
    compare 2 and 5 ---> 2<5. No Swap
    compare 5 and 6 ---> 5<6. No Swap.  Freeze (6,7,9)
    Now array is [1,2,5,6,7,9]
Step 3:[1,2,5,6,7,9]
    compare 1 and 2 ---> 1<2. No Swap.
    compare 2 and 5 ---> 2<5. No Swap.    Freeze (5,6,7,9)
Step 4: [1,2,5,6,7,9]
    compare 1 and 2 ---> 1<2 No Swap.
'''

# pseudocode

# unsorted array -> [0 - n-1]
# compare first two numbers
# if first number > second number , then swap the two numbers, else do nothing
# compare next two numbers (second and third number), swap if second > third
# continue till last two numbers of unsorted array are checked and swapped
# highest number of unsorted array has come to the last position (n-1)

# unsorted array -> [0 - n-2]
# compare first two numbers
# if first number > second number , then swap the two numbers, else do nothing
# compare next two numbers (second and third number), swap if second > third
# continue till last two numbers are checked and swapped
# highest number of unsorted array has come to the last position (n-2)

# unsorted array -> [0 - n-3]
# ....
# unsorted array -> [0 - 1]
'''
        0,1  1,2  2,3  3,4  4,5
        0,1  1,2  2,3  3,4
        0,1  1,2  2,3
        0,1 1,2
        0,1
'''

'''
Objective: To sort a given array in ascending order.
Move largest number to right side and smallest element to left side of array.
    Set the variable n to the length of the array.(n=len(arr)).
    Assign the variable to end of the array.(end = n-1).
    Compare each two elements in array and move large number to the right side, small element to left side.
    if first element(first) is greater than 2nd element(first+1) then swap it. Else do nothing.
    Increse the first element by 1.(first=first+1).
    Continue this process till end of the array.(first<end)
Decrese the end by 1.(end = end - 1)
Continue this process upto end greater than or equal to 1.(end>=1)
'''


arr = [3,114,20,630,21,735,16,4949,27,4823,28,33,1243,19,27,457,34,2054,29,2,973,8,949,31,45]
n = len(arr)
end = n-1
while end >= 1:
    first = 0
    while first < end:
        if arr[first] > arr[first + 1]:
            arr[first], arr[first + 1] = arr[first + 1], arr[first]
        else:
            arr[first],arr[first+1]=arr[first],arr[first+1]
        first = first + 1
        print(arr)
    end = end - 1
print(arr)
# [2, 9, 5, 1, 7, 6]