def first(A):
    depth = 0
    breadt = 0
    for i in A:
        number = int(i.split(" ")[1])
        if "forward" in i:
            breadt += number
        elif "down" in i:
            depth += number
        else:
            depth
            depth -= number
    return depth * breadt

def second(A):
    depth = 0
    aim = 0
    breadt = 0
    for i in A:
        number = int(i.split(" ")[1])
        if "forward" in i:
            breadt += number
            depth += aim * number
        elif "down" in i:
            aim += number
        else:
            aim -= number
    return depth * breadt

file = open("input.txt", "r")
A = [i for i in file.readlines()]
print(first(A))
print(second(A))

