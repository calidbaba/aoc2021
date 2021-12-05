def part1(A):
    mapping = {}
    for i in A:
        temp1 = i.split("->")[0].split(",")
        temp2 = i.split("->")[1].split(",") 
        x1 = int(temp1[0])
        y1 = int(temp1[1])

        x2 = int(temp2[0])
        y2 = int(temp2[1])

        if x1 != x2 and y1 != y2:
            continue
        if x2 == x1:
            if y1 > y2:
                largest = y1
                smallest = y2
            else:
                largest = y2
                smallest = y1
            for i in range(smallest, largest+1):
                if(not (x2, i) in mapping):
                    mapping[(x2,i)] = 1
                else:
                    mapping[(x2,i)] += 1
        else:
            if x1 > x2:
                largest = x1
                smallest = x2
            else:
                largest = x2
                smallest = x1
            for i in range(smallest, largest + 1):
                if (not (i, y2) in mapping):
                    mapping[(i, y2)] = 1
                else:
                    mapping[(i, y2)] += 1
    summen = 0
    for i in mapping:
        if mapping[i] > 1:
            summen += 1
    return summen

def part2(A):
    mapping = {}
    for i in A:
        temp1 = i.split("->")[0].split(",")
        temp2 = i.split("->")[1].split(",") 
        x1 = int(temp1[0])
        y1 = int(temp1[1])

        x2 = int(temp2[0])
        y2 = int(temp2[1])

        if x1 != x2 and y1 != y2:
            #vertical
            largestx = x2
            smallestx = x1
            largesty = y2
            smallesty = y1
            yneg = False
            xneg = False
            if y1 > y2:
                largesty = y1
                smallesty = y2
                yneg = True
            if x1 > x2:
                largestx = x1
                smallestx = x2
                xneg = True
            for k in range((largestx-smallestx) + 1):
                if xneg and yneg:
                    tupple = (largestx - k, largesty - k)
                    if(not tupple in mapping):
                        mapping[tupple] = 1
                    else:
                        mapping[tupple] += 1
                elif xneg:
                    tupple = (largestx - k,smallesty + k)
                    if(not tupple in mapping):
                        mapping[tupple] = 1
                    else:
                        mapping[tupple] += 1
                elif yneg:
                    tupple = (smallestx + k, largesty - k)
                    if(not tupple in mapping):
                        mapping[tupple] = 1
                    else:
                        mapping[tupple] += 1

                else:
                    if(not (smallestx + k, smallesty + k) in mapping):
                        mapping[(smallestx + k, smallesty + k)] = 1
                    else:
                        mapping[(smallestx + k, smallesty + k)] += 1
            continue
        if x2 == x1:
            if y1 > y2:
                largest = y1
                smallest = y2
            else:
                largest = y2
                smallest = y1
            for n in range(smallest, largest+1):
                if(not (x2, n) in mapping):
                    mapping[(x2,n)] = 1
                else:
                    mapping[(x2,n)] += 1
        else:
            if x1 > x2:
                largest = x1
                smallest = x2
            else:
                largest = x2
                smallest = x1
            for n in range(smallest, largest + 1):
                if (not (n, y2) in mapping):
                    mapping[(n, y2)] = 1
                else:
                    mapping[(n, y2)] += 1
    summen = 0
    for n in mapping:
        if mapping[n] > 1:
            summen += 1
    return summen


# file_name = "./test.txt"
file_name = "./input.txt"
def parseFile(file_name):
    return [i.rstrip() for i in open(file_name, "r")]

inp = parseFile(file_name)
print("part1: ", part1(inp))
print("part2: ", part2(inp))