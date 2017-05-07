digit, high = input().split(',')
high = int(high)

ints = []
for n in range(high+1):
    ints.extend(int(nn) for nn in str(n).split(digit) if nn != '')

print(sum(ints))
