year = int(input("Enter the year: "))  # This line prompts the user to enter a year and converts the input to an integer using the int() function.
if (year%4) == 0:  # If it is divisible by 4, the code enters the first if block.
    if(year%100) ==0: # Inside the first if block, the code further checks whether the year is divisible by 100 with no remainder:
        if(year%400) ==0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    else:
        print("The year is a leap year")
else:
    print("The year is not a leap year")


    '''year = int(input("Enter the year: ")): This line prompts the user to enter a year and converts the input (which is initially a string) to an integer using the int() function. It then assigns the integer value to the variable year.

2) The code then checks whether the input year is divisible by 4 with no remainder:
       If it is divisible by 4, the code enters the first if block.
3) Inside the first if block, the code further checks whether the year is divisible by 100 with no remainder:
       If it is divisible by 100, the code enters the nested if block.
4) Inside the nested if block, the code checks whether the year is divisible by 400 with no remainder:
      If it is divisible by 400, the code prints "The year is a leap year" because a year divisible by 400 is a leap year.
      If it is not divisible by 400, the code prints "The year is not a leap year" because even though it's divisible by 4 and 100, it doesn't meet the criteria for a leap year.
5) If the year is divisible by 4 but not by 100, the code prints "The year is a leap year" because any year divisible by 4 is a leap year, except for years that are divisible by 100 but not by 400.
6) If the year is not divisible by 4, the code prints "The year is not a leap year" because non-divisible years are not leap years.'''


