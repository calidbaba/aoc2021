import sys
def gamma(A, common):
    gamma = ""
    for x in range(len(A[0])):
        gamma_count = 0
        for i in A:
            gamma_count += int(i[x])
        if gamma_count > len(A)/2:
            if common:
                gamma += "1"
            else:
                gamma += "0"
        else:
            if not common:
                gamma += "1"
            else:
                gamma += "0"
    return int(gamma, 2)

file = "input.txt"
if len(sys.argv) == 2:
    if sys.argv[1] == "test":
        file = "test.txt"

inp = [i.rstrip() for i in open(file, "r")]
gamma_rate = gamma(inp, True)
epsilion_rate = gamma(inp, False)
if (file == "test.txt"):
    if not gamma_rate == 22:
        print(f"gamma rate is {gamma_rate} expected 22")
    if not epsilion_rate == 9:
        print(f"epsilion rate is {epsilion_rate} expected 9")

print(f"gamma_rate = {gamma_rate}")
print(f"epsilion_rate = {epsilion_rate}")
print(f"product = {epsilion_rate* gamma_rate}")
