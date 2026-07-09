#pass function
#pass is used for execute the code without any error
"""def fun():
    print("vinay")
fun()"""

#pass function in conditional statement 
"""x=10
if x>=5:
    pass
else:
    print("5 or lessthan 5")"""

#pass function in loops
"""for i in range(5):
    if i==3:
        pass
    else:
        print(i)"""

#2) loop
"""for i in range(5):
    if i<=3:
        pass # if we use pass in if statement no matter what the above expression on the if will skiped
    print(i)"""

#pass function in classes
"""class new:
    pass #no methods or attributes yet
class person:
    def details(self, name, age):
        self.name=name
        self.age=age
        def greet(self):
            pass #placeholder for greet method
        #creating instance of class
        p=person("vinay",19)"""

#given number is odd or even
def check_even_or_odd(num):
    if num%2==0:
        pass
    else:
        print("odd")
        print("Done")
check_even_or_odd(7)