#conditional statements
#if statements
"""a=17
if age<=18:
    print("Eligible for vote")"""

#if else statement
"""age=10
if age<=12:
    print("Eligible for free ticket")
else:
    print("not eligible for free ticket")"""

#if elif else statement
"""age=19
if age<=12:
    print("child")
elif age <=19:
    print("young")
elif age <=35:
    print("adult")
else: 
    print("old man")"""

#nested if statement
"""age=65
is_person=True 
if age>=60:
    if is_person:
        print("Eligible for 20% senior citizen discount")
    else:
        print("Eligible for 30% senior citizen discount")
else:
    print("not eligible for senior citizen discount")"""

#conditional expression (ternary operator)
#if the give condition is true it return the first value of the expression otherwise it returns second value of the expression
"""age=19
s="adult" if age >=18 else "minor"
print(s)"""

#match-case statement
"""number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")"""