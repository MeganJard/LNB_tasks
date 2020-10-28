from random import shuffle, randint

li = []
it = 0
n, m, k = randint(2, 10), randint(2, 10), randint(2, 10)
for i in range(n):
    li1 = []
    for j in range(m):
        li2 = []
        for l in range(k):
            li2.append(str(it).rjust(len(str(n*m*k)), ' '))
            it += 1
        li1.append(li2)
    li.append(li1)

shuffle(li)
print('\n'.join(['  '.join([str(' '.join([i for i in j])) for j in l]) for l in li]))
li = sorted(li, key= lambda x: x[0][1])
print()
print()
print('\n'.join(['  '.join([str(' '.join([i for i in j])) for j in l]) for l in li]))