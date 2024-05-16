a=str(input("In which word is need to check palindrome or Not?"))   # refer
start=0     # starting letter of the string  
end=len(a)-1    # Ending letter of the string, end=4
while start<=end:   # Set condition - Start greater than end, stop the loop
    if a[start] != a[end]: # start not equal to end
        print("False")
        break # Break the condition when if condition is passed.
    else:
        start=start+1
        end=end-1
else: 
    print("True")
    