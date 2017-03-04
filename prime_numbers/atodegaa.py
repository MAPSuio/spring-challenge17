def primes(n):
    """Returns a list of all primes p such that 2 <= p < n"""
    #This is a standard prime sieve
    l = [True for _ in xrange(n)]
    i = 2
    while i*i < n:
        for d in xrange(i*i, n, i):
            l[d] = False
        i += 1
        while l[i] == False:
            i += 1
    return [i for i in xrange(2, n) if l[i]]

def isqrt(n):
    """Returns the largest integer i such that i*i <= n"""
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def modified_prime_sieve(start, stop):
    """Returns a list of all primes p such that start <= p < stop"""
    #This builds on the idea that a number n is not a prime number if and only if
    #there is some prime number less than or equal to sqrt(n) which divides n
    #Using a fairly standard sieving technique, this gives us the right answer.
    #Some of the difficulty lies in finding out where to start for a given prime number.
    l = [True for _ in xrange(start, stop)]
    prime_list = primes(isqrt(stop)+1)
    for p in prime_list:
        if start % p == 0:
            first = start
        else:
            first = (start//p)*p + p
        for i in xrange(first-start, stop-start, p):
            l[i] = False
    return [start+i for i in xrange(stop-start) if l[i]]

def answer():
    #Using the prime number theorem, one can get an approximation that there are
    #about 1.3 million primes between 10**16 and 10**16+5*10**7
    return sum(modified_prime_sieve(10**16, 10**16+5*10**7)[:10**6])

print answer()
print 10**6*10**16
