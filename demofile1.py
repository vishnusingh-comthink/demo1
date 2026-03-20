
import math

def reva(n):
    while(n):
        print(n%10, end = '')
        n = n//10

# reva(1729)

def ispal(n):
    if n < 0:
        return False
    digs = 0
    num = n
    while(num):
        digs += 1
        num = num // 10
    
    num = n
    f = 1

    while(num):
        a = num // (10**(digs - 1))
        b = num % 10
        if a != b:
            f = 0
        num = num % (10**(digs - 1)) # removes 1st digit
        num = num // 10 # removes last digit
        digs = digs - 2

    if f:
        return True
    else:
        return False
    
# print(ispal(3479743))
# print(ispal(19791))
# print(ispal(212))
# print(ispal(2917))
# print(ispal(9))
# print(ispal(-5))
# print(ispal(0))


def primes(n):
    isp = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            isp = False
    return isp

def allp(n):
    for i in range(2, n + 1):
        if primes(i):
            print(i)

allp()

def tad(g):
    for i in range(len(g) - 1, 0,  )
