def SieveofEratosthenes(n):
    visited = [False] * (n + 2)
    for i in range(2, n + 2):
        if visited[i] == False:
            for j in range(i * i, n + 2, i):
                visited[j] = True
    return visited

def specialPrimeNumbers(n, k):
    visited = SieveofEratosthenes(n)
    primes = []
    for i in range(2, n + 1):
        if visited[i] == False:
            primes.append(i)
    count = 0
    for i in range(len(primes)):
        for j in range(i - 1):
            if primes[j] + primes[j + 1] + 1 == primes[i]:
                count += 1
                break
        if count == k:
            return primes[:i + 1]
    return []

n = 100000000
k = 1
special_primes = specialPrimeNumbers(n, k)
