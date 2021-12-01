def part1(f):
    start = -1
    # set to -1 since the first will always be larger, provided its positive
    increase = -1
    for i in f:
        i = int(i)
        if i > start:
            increase += 1
        start = i
    return increase

def part2(f):
    start = -1
    # set to -1 since the first will always be larger, provided its positive
    increase = -1
    for i in range(2, len(f)):
        summ = int(f[i]) + int(f[i-1]) + int(f[i-2])
        if summ > start:
            increase += 1
        start = summ
    return increase


f = open("input.txt", "r")
# last line is ""
f = f.read().split("\n")[:-1]


print(part1(f))
print(part2(f))
