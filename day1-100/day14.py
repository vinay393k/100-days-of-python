#Arguments
#arguments are generally to types keyword (*kwargs) arguments and none keyword arguments(*args)
#example for *args and *kwargs arguments
#args example:
def fun(*args):
    return(sum(args))
print(fun(10,15,5))

#kwargs example:
def fun(**kwargs):
    for k, value in kwargs.items():
        print(k, value)
fun(age=19,name="vinay")

#*args using for loop
def fun(*args):
    for num in args:
        print(num)
fun("vinay","sai","sagar")#args collects argument in the form of tuple

#*kwargs example
def introduce(**kwargs):
    details=[]
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="vinay", Age=19, City="vijayawada"))

#also we can us both *args and *kwargs in one program to write both positional and keyword arguments at once.
def fun(*args,**kwargs):
    print("names=",args)
    print("detais=",kwargs)
fun("hardik","vijay",hardik="cricketer",vijay="actor")