records = input().split('|')

valid = {}
fake = {}
n_reads = 0
n_fake = {}
n_valid = {}

for record in records:
    _, name, stat = record.split(',')

    if name not in valid:
        valid[name] = 0
        fake[name] = 0
        n_fake[name] = 0
        n_valid[name] = 0

    if stat == '-1':
        n_reads += 1
        if fake[name] / (fake[name] + valid[name]) >= .75:
            n_fake[name] += 1
        else:
            n_valid[name] += 1
    elif stat == '0':
        valid[name] += 1
    elif stat == '1':
        fake[name] += 1

tr = 0
fr = 0

for name in valid.keys():
    if fake[name] / (fake[name] + valid[name]) >= .75:
        tr += n_fake[name]
        fr += n_valid[name]
    else:
        fr += n_fake[name]
        tr += n_valid[name]

print("Total User Reads:{}".format(n_reads))
print("True Reads:{}%".format(round(100*tr/n_reads)))
print("Fake Reads:{}%".format(round(100*fr/n_reads)))

