#recursive in python
#generally recursion is a funtion calling itself either directly or indirectly
#structure of recursion 
"""def recursive_function():
    if base_case condition:
        return base_return
    else:
        return recursive_function(modified_parameters)""" 

#write  program to find the n factorial by using recursion in python
"""def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))"""

#write a program to get fibonacci number using recursion in python
"""def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))"""

#recursion is mainly two types. they are tail recursion and non-tail recursion
def tail_fact(n,acc=1):
    if n==0:
        return acc
    else:
        return tail_fact(n-1,acc*n)
def nontail_fact(n):
    if n==0:
        return 1
    else:
        return n* nontail_fact(n-1)
print(tail_fact(5))
print(nontail_fact(5))