'''
Author: Lucas Burt 
Description: general list of recursive functions create functions for each identity with a menu to support them. 
Sources: Google, W3 Schools, Stack Overflow 
Dates: 5/13/26 
Version: 1.0 
Features: Menu Driven program supporting 9 recursive functions available using menu. 
Graded by Luke Balducci: does not acount for spaces for the first input. 
'''

def factorial(n):
    '''
    description - alculates the product of all positive integers up to "n" 
    args - n  
    returns - n,n-1
    '''
    if  n== 0: 
            return 1 
    return n * factorial(n-1) 
def summation(n): 
    '''
    description - a function that calculates the total of a series of numbers
    args - n
    returns - 0 
    '''
    if n > 0:
        return n + summation(n-1)
    if n ==0: 
        return 0

def powers(a,n):
    '''
    description - calculates a number raised to an exponent by calling itself with smaller values until it reaches a "base case"
    args - a,n 
    returns - 1
    '''
    if n > 0:
         return a*powers(a,n-1)
    elif n ==0: 
         return 1 

def snm(n):
    '''
    description - works by breaking down a number into its last digit and the remaining digits.
    args - n 
    returns - snm mod 
    '''
    if n<10:
        return n 
    else: 
        return n%10 + snm(n//10)
def fib(n):
    '''
    description - sequence is a series of numbers where each number is the sum of the two preceding ones
    args - n 
    returns - 1, fib(n-1), fib(n-2)
    '''
    if n == 0: 
        return 0 
    elif n == 1:
        return 1 
    elif n >1:
        return fib(n-1) + fib(n-2)
     
def GCD(x,y):
    '''
    description - greatest common denominator of two numbers 
    args - x,y 
    returns - GCD(greatest common denominator)
    '''
    if y <= x and x % y == 0:
        return  y
    else: 
        return GCD(y,x % y)
def cib(p,r,t):
    '''
    description - calculates the compound interest balance over time
    args - p,r,t
    returns - CIB --> Finds the compound interest balance after t periods 
    '''
    if t == 0: 
        return p
    elif t>0:
        return (1+r)* cib(p,r,t-1)

def p2wn(a,b):
    '''
    description - calculates the product of two numbers using repeated addition 
    args - a,b
    returns - product of a and b
    '''
    if b > 0: 
        return a +p2wn(a,b-1)
    elif b == 0: 
        return 0 

def sqna(n,p,e): 
    '''
    description - approximates the square root of a number using Newton's method
    args - n,p,e 
    returns - square root approximation of n within precision p
    '''
    if abs(e**2 - n) < p:
        return e 
    else: 
        return sqna(n,p,(e+n/2)/2) 
        

def main():

    while True: 
        """ 
        """
        print("""
    1 factorial  
    2 summation
    3 powers 
    4 snm 
    5 fib 
    6 GCD 
    7 cib
    8 p2wn 
    9 sqna 
            """)
        option = input("what would you like to do?").strip()
        if option == '1':   
                n = input("input any number: ")
                try:
                    print(factorial(int(n)))
                except ValueError:
                    print("invalid input, numbers only")
                continue
        elif option == '2':
                n = input("input any number: ")
                try:
                    print(summation(int(n)))
                except ValueError:
                    print("invalid input, numbers only")
                continue
        elif option == '3': 
            a = input("input any number: ")
            n = input("input another number: ")
            print(powers(int(a), int(n)))
            continue
        elif option == '4': 
            n = input("input any number: ")
            print(snm(int(n)))
            continue
        elif option == '5':
            n = input("input any number: ")
            print(fib(int(n)))
            continue
        elif option == '6': 
            x = input("input any number: ")
            y = input("input another number")
            print(GCD(int(x), int(y)))
            continue
        elif option == '7':
            p = input("input any number: ")
            r = input("input another number: ")
            t = input("input a third number: ")
            print(cib(int(p), int(r), int(t)))
            continue
        elif option == '8':
            a = input("input any number: ")
            b = input("input another number: ")
            print(p2wn(int(a), int(b)))
            continue 
        elif option == '9': 
            n = input("input any number: ")
            p = input("input another number: ")
            e = input("input third number ")
            print(sqna(int(n), int(p), int(e)))
            continue
main() 