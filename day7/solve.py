from math import inf


def part2(A):
    minfuel = inf
    for n in range(max(A) + 1):
        fuel = 0
        for crab in A:
            nyn = abs(n - crab)
            #triangle numbers
            fuel += (nyn*(nyn+1))//2
        if fuel < minfuel:
            minfuel = fuel
    return minfuel

def part1(A):
    minfuel = inf
    for n in range(max(A) + 1):
        fuel = 0
        for crab in A:
            fuel += abs(n - crab)
        if fuel < minfuel:
            minfuel = fuel
    return minfuel

def parse(file):
    return [int(i.strip()) for i in open(file).read().split(",")]

# file = "test.txt"
file = "input.txt"
inp = parse(file)
print("part1: ",part1(inp))
print("part2: ", part2(inp))

