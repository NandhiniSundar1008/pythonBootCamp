'''Comapre the first 2 element found the minimum number.
Found the minimum number store in new varialble.(minimum)
Check minimum with 3d number. if 3d number is less then minimum set 3d number to minimum number.'''




arr = [4,6,3,12,7]
minimum = arr[0]     # First value (4)
mini_index = 0       # First value index (0)
i = 1                # Running variable
while i<len(arr):

    if minimum>arr[i]:
        minimum=arr[i]
        mini_index = i
    i=i+1
print(mini_index,minimum)
