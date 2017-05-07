# this solution is really gross, don't judge

a, b = sorted([float(input()), float(input())])

diffa = b - a
diffb = (360-b + a)
av2 = (a + diffa/2)
av = b + diffb/2
if av >= 360:
    av = (av - 360)

if diffa < diffb:
    print('{:.2f}'.format(av2))
elif diffa == diffb:
    print('{:.2f}'.format(min(av, av2)))
else:
    print('{:.2f}'.format(av))
