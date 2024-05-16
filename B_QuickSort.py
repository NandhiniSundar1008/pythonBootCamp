'''
4,9,3,1,7,8,6,2,10   Find the pivot number
L       P        R 
Step 1:
Condition L<P ; P<R. If the condition break swap L and R

4,2,3,1,7,8,6,9,10
  L     P     R
4,2,3,1,6,8,7,9,10
        L   R
4,2,3,1,6,7,8,9,10
          L R
4,2,3,1,6,7,8,9,10
          L
          R
          P
Step 2:
4,2,3,1,6   7    8,9,10
L   P   R        L P R 
1,2,3,4,6   7    8,9,10
L   P R            L
1,2,3,4,6          P 
    L              R
    R
    P
Step 3:
1,2,3,4,6,7,8,9,10'''

'''
Objective : Quick sort the given array.
Rearrange values before pivot as smaller and values after pivot as larger elements.
Assign arr[len(arr)//2] as pivot.
Store the L and R in i and j variables.
Loop the condition i<j.
    while arr[i] less than pivot, increment the i(i = i +1)
    While arr[j] greater than pivot decrement the j(j = j+1)
    If arr[i]>P and arr[j]<P then swap the i and j.
    Loop continue in break the condition.
Recursion
    
    Sort the left side (arr(left side array), L(0), P_index-1)
    Sort the right side (arr(right side array), P_index+1, R(len(arr)-1))
    Break the recursion if L>=R

'''
def quickSort(arr,L,R,level):
    # Find the pivot value andrearrange small element to left and large to right
    # Sort the left left array in ascending
    # Sort the right side array in ascending
    print('level',level)
    print('arr',arr[L:R+1])
    # Rearrange values before pivot as smaller and values after pivot as larger elements.
    # Assign arr[len(arr)//2] as pivot.
    if L>=R:
        return
    P = arr[(L+R)//2] # Pivot element for rearrangement
    i = L
    j = R
    while i<j:
        # find the first left index that needs to be swapped
        while arr[i]<P:
            i=i+1
        # find the first right index that needs to be swapped
        while arr[j]>P:
            j=j-1
        arr[i],arr[j]=arr[j],arr[i]
    print('New',arr[L:R+1])

    P_index = i # Store the pivot index to handle function call for left and right
    # Sort left side
    quickSort(arr,L,P_index-1,level+1) # left side recursion function call
    print('back to level', level)
    quickSort(arr,P_index+1,R,level+1) # right side recursion function call
    print('completed level', level)


arr=[4,9,3,1,7,8,6,2,10]
quickSort(arr,0, len(arr)-1,0)  # Main call function
print(arr)









'''arr =[4,9,3,1,7,8,6,2,10]
p = arr[len(arr)//2]
left = 0
right = len(arr)-1
while left<right:
# find the first left index that needs to be swapped
    while arr[left]<p:
        left = left +1
# find the first right index that need to be swapped
    while arr[right]>p:
        right = right -1
    else:
        arr[left],arr[right]=arr[right],arr[left]
    #print(left,arr[left])
    #print(right,arr[right])
    #print(arr)'''
