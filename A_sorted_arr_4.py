'''arr = [7,10,5,8,2,28]
temp = []
# 7,10; 10,5; 5,8; 8,2; 2,28
i=0
minimum = arr[i]
while i<len(arr)-1:
    if minimum>arr[i]:
        minimum=arr[i]
        temp = temp + [minimum]
    i=i+1
print(temp)'''

arr = [7, 10, 5, 8, 2, 28]
sort_ = []
i = 0

while len(arr) > 0:
    minimum = min(arr)  # Find the minimum value in the arr list
    sort_ = sort_ + [minimum]  # Add the minimum value to the temp list
    arr.remove(minimum)  # Remove the minimum value from arr

print(sort_)

