'''
Created on Apr 12, 2024

@author: DraculaVenom
'''

#problem 7: https://projecteuler.net/problem=7
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def max_prime_below(limit):
    for num in range(limit - 1, 1, -1):
        if is_prime(num):
            return num
    return None

def getNprime(n):
    primes = [2, 3, 5]
    i = 7;
    while len(primes) < 10001:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes[len(primes) - 1]

#limit = 10001
#max_prime = getNprime(limit)
#print("The largest prime number below", limit, "is", max_prime)



#problem 9: https://projecteuler.net/problem=9
import math
def isPythagoreanTriplet(a, b, c):
    if a*a + b*b == c*c:
        return True
    return False

def getC(a, b):
    try:
        c = math.sqrt(a*a + b*b)
    except:
        c = 0
        #print(a)
        #print(b)
    return round(c)

a = 1
b = a
c = getC(a, b)
flag = False
#for x in range(0, 1000):
while(a <= 1000 and not flag):
    while(b <= 1000 and not flag):
        #print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
        flag = isPythagoreanTriplet(a, b, c)
        if(flag and (a + b + c == 1000)):
            print("found")
            print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c) + ", sum: " + str(a+b+c))
        b += 1
        c = getC(a, b)
    if(not flag):
        b = a
        a += 1
        c = getC(a, b)
    else:
        if(a + b + c == 1000):
            print("found")
            print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
        else:
            flag = False
    
a= 200
b= 375
c= 425
ans = isPythagoreanTriplet(a, b, c)
print(ans)
print("product: " + str(a*b*c))