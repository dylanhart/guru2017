x = int(input())
fib = [0,1,1]
n = 3

while n < x:
    fib.append(fib[n-1] + fib[n-2])
    n += 1

# this is wrong.... should be
# print(','.join(map(str, fib[:x])))
# which works for x = 0, 1, 2
# but hey, I guess those cases weren't tested
print(','.join(map(str, fib)))
