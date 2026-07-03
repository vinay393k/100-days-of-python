#arithmetic operators
"""a=10
b=3
print("add:",a+b)
print("sub:",a-b)
print("multiple",a*b)
print("division",a/b)#by division we get coeficient
print("floor division",a%b)#by floor division we get reminder 
print("exponentaiation",a**b)"""

#relational operators
#in relational or compair operator it returns output in ture or false format
"""a=3
b=7
print(a==b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a!=b)"""

#logical operators
#in logical operator it precedence of execution in for left to right thats why we get a value in or operator
"""a=6
b=2
print(a or b)
print(a and b)
print(not b)
"""
#bitwise operation
"""a=10
b=4
#by using truth tables to get the output
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a<<2)
print(a>>2)"""

#assignment operators
"""a=10
b=a
print(b)
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
b<<=a
print(b)"""

#identity operator
"""a=10
b=20
c=a
print(a is not b)
print(a is c)"""

#membership operator
#membership operator are used to check the operand a present in operand n are not by using  "in"  and "in not" operators
"""a=20
b=[10,20,30]#here i am taking list in varible b
if(a in b):
    print("a is present in b")#the space i give here is indentation in java we use "{}" this as indentation
else:
    print("a is not present in b")
"""

#ternary operator it is also known as conditional expression
"""a,b=10,20
min=a if a>b else b # if the given expression is true it returns a otherwise it returns b
print(min)"""

#precedence operator 
"""exp=10+20*30
print(exp)"""
#in precedence operator it execute the operation as per the rules of precedence operators
#even if we have the same precedence value operator it print left to right (or) right to left as per the associativity
