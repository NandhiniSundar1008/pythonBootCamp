def print_table(table,row):
    #print first 10 lines of table
    i=1
    while i<=row:
        print(i,"x",table,"=",i*table) #1*5=5
        i=i+1
    print("table has been printed")
    

table=int(input("Which table do you want?"))
rows=int(input("How many rows do you want to print?"))
a=print_table(table,rows)
print(a)
