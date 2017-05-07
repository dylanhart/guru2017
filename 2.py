
# THIS SOLUTION IS INCORRECT!

# I thought it was the sum of the prime factors, not the sum of the _digits_ of
# the prime factors

primes = [2]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

for n in range(3, 42, 2):
    if is_prime(n):
        primes.append(n)

def gen(s):
    for p in primes:
        if p == s:
            yield p
        elif p < s:
            for o in gen(s - p):
                yield p * o
        else:
            break

nums = []
for n in gen(42):
    s = sum(int(d) for d in str(n))
    if s == 42:
        print(n)
        nums.append(n)

print(min(nums))
