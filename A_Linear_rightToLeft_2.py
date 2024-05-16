'''def linear_LR(arr,value):             # Output comes from True or False
    i=0
    while i<len(arr):
        if arr[i] == value:
            return True
        i = i - 1
    return False
arr = [1,4,7,9,13]
value = int(input(": "))
result = linear_LR(arr,value)
print(result)'''

def linear_LR(arr,value):             # Output comes from True or False
    i=0
    while i<len(arr):
        if arr[i] == value:
            return i
        i = i - 1
    return False
arr = [3,4,7,9,13]
value = int(input(": "))
result = linear_LR(arr,value)
print(result)