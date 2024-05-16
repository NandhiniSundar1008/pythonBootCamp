def printUpto(n):  #function Definition
#    for i in range (n):
#        print (i)

#    i=0
#    while i<n:
#        print (i)
#        i=i+1
    
    if n==0:
        return
    printUpto(n-1)  # funtion call ---> This function call run from n==0. Then jump to print(n-1)
    print(n-1)
    return  

printUpto(5)  # Main function call      
'''
printupto(5) ---> printUpto(4),  4
printUpto(4) ---> printUpto(3),  3
printUpto(3) ---> printUpto(2),  2
printUpto(2) ---> printUpto(1),  1
printUpto(1) ---> printUpto(0),  0
printUpto(0) ---> nothing to do return
'''

