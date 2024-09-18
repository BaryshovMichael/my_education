numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = 0

primes = []
not_primes = []
i = 0

for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]

    if n < 2:
        continue
    else:
        k = 2
        j = 0
    while n >= k*k:
        if n % k == 0:
            j = 1
            is_prime = False
            break
        k = k +1
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True

print(primes)
print (not_primes)
