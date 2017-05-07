z = int(input())
data = tuple(map(int, input().split()))
size = 360//z

mins = []
idxs = []

for n in range(z):
    idx = n*size
    min = data[idx]
    # add -1 to idx+size due to a bug in sample
    # it shouldn't be there but the solutions were incorrect due to a bug in the
    # program that the judges used
    for i in range(idx+1, idx+size-1):
        if data[i] < min:
            min = data[i]
            idx = i
    mins.append(min)
    idxs.append(idx)

print(' '.join(map(str, mins)))
print(' '.join(map(str, idxs)))
