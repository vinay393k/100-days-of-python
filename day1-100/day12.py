#local and global variables
#local variable
"""def fun():
    greet="hello vinay!"
    print(greet)
fun()
"""
#trying to access local variable outside the function 
"""
def fun():
    msg="hello!"
    print("inside function",msg)
fun()
print("outside function",msg) #we are using local variable so we are not able to access outside the function
#it returns error that msg is not defined"""
 
#trying the above program with global variable
"""
msg="python!"
def fun():
    print("inside the function:",msg)
fun()
print("outside the function:",msg) """ #it returns the output with any error,why because global variable can access throughout the program

#global variable can accessed everywere the program
"""msg="i love python!"
def fun():
    print("me:",msg)
fun()"""

#using local and global variable
"""def fun():
    s="me too"
    print(s)
s="i love python"
fun()
print(s)"""

#modifing global varible inside a function
#without global (cause error) 
"""
def fun():
    s+="me too"
    print(s)
    s="i love python"
fun()
"""

#with global variable(runs without any error)
"""
s="i love "
def fun():
    global s
    s+="python"
    print(s)
    s="learning python everyday"
    print(s)
fun()
print(s)
"""

#local variable vs global variable with same name
a=1
def f():
    print("f():",a)
def g():
    a=2
    print("g():",a)
def h():
    a=3
    print("h():",a)

print("global:",a)
f()
print("global:",a)
g()
print("glabol:",a)
h()
print("glabol:",a)