#data types in python
#numeric data types are mainly three types int, float, complex numbers
#numeric data types are also called as primitive data types
#example
"""a=17 #integer is a numeric value without any decimal or fraction
b=17.00 #floating point is a numeric value with decimal or fraction
c=17+15j #complex data type is combination of real and imaginary values
print(type(a),"value of a:",a)
print(type(b),"value of b:",b)
print(type(c),"value of c:",c)"""

#sequence data types 
#these are also called as non-primitive data types and it contain string, list, tuple, dictionary, and set
"""a="vinay"
list=["vinay",19,"student"]
tuple=("vinay",19,"student")
dict={'name':'vinay','age':19,'standard':'3rd year'}
set={1,2,3,"vinay",19,"student"}"""
"""print(type(a),"the data on variable name a: ",a)
print(type(list),"the data on variable name list: ",list)
print(type(tuple),"the data on variable name tuple:",tuple)
print(type(dictionary),"the data on variable name dictionary:",dictionary)
print(type(set),"the data on variable name set:",set)"""

#indexing
"""
print(list[0]) #by using indexing we can return output vinay
print(a[-1]) #it returns last word of the variable a
print(tuple[-1]) #it returns the reverse order of the variable tuple
del a # by using del we can delete the variable a 
# dictionarys and sets does not support indexing
print(dict["age"]) # in dictionary we are not able to return wanted number by using index instead we use key of the data ,so it returns the age on the variable dict
for _ in set:
    print(_)"""