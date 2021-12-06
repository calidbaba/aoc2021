spawn_age = 8

#set respawn age to 6 +1 as its 0 indexed, same goes for spawn age, but i just handle that directly in the function
respawn_age = 7
def part1(A, day):
    for _ in range(day):
        appendlist = []
        for index, fish in enumerate(A):
            if fish == 0:
                fish = 6
                appendlist.append(8)
            else:
                fish -= 1
            A[index] = fish
        for i in appendlist:
            A.append(i)
    return len(A)
memo = {}
def getDoubles(fish, days_left):
    start_days_left = days_left
    if (fish, start_days_left) in memo:
        return memo[(fish, start_days_left)]
    if days_left < fish +1:
        return 0
    days_left -= fish + 1
    amount_of_fish = 1 
    amount_of_fish += getDoubles(spawn_age, days_left)
    
    for _ in range(days_left, 0, -respawn_age):
        if days_left < respawn_age:
            break
        amount_of_fish += 1
        days_left -= respawn_age
        amount_of_fish += getDoubles(spawn_age, days_left)
    memo[(fish, start_days_left)] = amount_of_fish
    return amount_of_fish
    
def part2(A, day):
    answer = len(A)
    for fish in A:
        answer += getDoubles(fish, day)
    return answer 
    



def parseFile(file):
    # return [3]
    return [int(i.strip()) for i in open(file).read().split(",")]


file = "input.txt"
# file = "test.txt"

inp = parseFile(file)
print(inp)
print("part2: ", part2(inp, 256))
#part 1 goes last as it fuck up the input lolol 
print("part1: ",part1(inp, 80))