'''
Concept of the program
    Write a file(number.txt) One number in each line
    Import the values in list format
    Read the file
    Sort the numbers in ascending order
    After the sorting read(save) the numbers in new file(sort.txt)
'''

'''
Pseudocode:
Write a numbers in new text file(number.txt):
    The open() function is used with the "w" mode to open a file named "number.txt" for writing.
    Use variable "numbers" given the numbers in string format using "\n".
    Print the many lines so used writelines.
    Close the file a.
Read a file:
    Opens the "number.txt" file for reading using the open() function.
    It reads all lines from the file using the readlines() method.
    Close the file a.
Read and convert the numbers(number.txt):
    Create a empty list(store the numbers read from the file)
    The open() function is used with the "r" mode to open a file named "number.txt" for reading.
    Using for loop (for line in b: line-variable name, b-function name)
    Using line.strip() Remove the whitespace in the line and convert the integer then store in num.
    The converted integers are appended to the numbers list.
    Close the file b.
Sort the list:
    using bubble sort method and sort the numbers.
Storing Sorted Numbers in "sort.txt":
    The open() function is used with the "w" mode to open a file named "sort.txt" for writing.
    Using for loop (for each_num in numbers: each_num-variable name, numbers-function name)
    The write() method writes each number to the file as a string, followed by a newline character "\n"
    Close the file c.
'''
# Write a number in new text file(number.txt)
'''a = open("number.txt","w")
numbers=["3\n","114\n","20\n","630\n","21\n","735\n","16\n","4949\n","27\n","4823\n","28\n","33\n","1243\n","19\n","27\n","457\n","34\n","2054\n","29\n","2\n","973\n","8\n","949\n","31\n","45"]
a.writelines(numbers)
#print(numbers)
a.close()'''

# Read a numbers
a = open("number.txt","r")
a.readlines()
#print(numbers)
a.close()

# Read and convert the numbers(number.txt):
numbers = []
b = open("number.txt","r")
for line in b:
    num = int(line.strip())
    numbers.append(num)
print(numbers)
b.close()

# Sort the list
#number = [3,114,20,630,21,735,16,4949,27,4823,28,33,1243,19,27,457,34,2054,29,2,973,8,949,31,45]
n = len(numbers)
end = n-1
while end >= 1:
    first = 0
    while first < end:
        if numbers[first] > numbers[first + 1]:
            numbers[first], numbers[first + 1] = numbers[first + 1], numbers[first]
        first = first + 1
    end = end - 1

# Store a sorted number in "sort.txt" file
c = open("sort.txt","w")
for each_num in numbers:
    c.write(str(each_num)+"\n")
print(type(numbers))
c.close()
print("Completed")









# write a number in new file.
    # variable name = open(given 2 parameters: filename and mode(r-read,w-write))
        # a = open("number.txt","w")
    # add a numbers in list format output comes from line by line so end of the number given "\n"
        # number=[given number in "\n"]
    # use a default method in "writelines-more numbers are added so use writelines"
        # a.writelines(number)
'''a = open("number.txt","w")
number=["3\n,","114\n","20\n","630\n","21\n","735\n","16\n","4949\n","27\n","4823\n","28\n","33\n","1243\n","19\n","27\n","457\n","34\n","2054\n","29\n","2\n","973\n","8\n","949\n","31\n","45"]
a.writelines(number)'''

'''for each_line in number: # use loop function 
    a.write(each_line+"\n")
a.close()'''

# Read a file
    # variable name = open(given 2 parameters: filename and mode)
        # a = open("number.txt","r")
'''a = open("number.txt","r")
print(a.read())
a.close()'''
