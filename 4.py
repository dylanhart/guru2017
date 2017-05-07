a = 'abcdefghijklmnopqrstuvwxyz'

cnt = int(input())
for _ in range(cnt):
    b, n = map(int, input().split())

    s = []
    while n > 0:
        n -= 1
        s.append(a[n%b])
        n //= b
    print(''.join(reversed(s)))
