import itertools

for i in itertools.count(start=1, step=2):
    if i > 10:
        break
    print(i)