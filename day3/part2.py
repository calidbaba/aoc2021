import sys
#ravioli
def gamma(A, common, x):
    gamma = ""
    gamma_count = 0
    for i in A:
        gamma_count += int(i[x])
    common_umcommon = None
    if common:
        if gamma_count >= len(A)/2:
            common_umcommon = "1"
        else:
            common_umcommon = "0"
    else:
        if gamma_count < len(A)/2:
            common_umcommon = "1"
        else:
            common_umcommon = "0"
    return common_umcommon 

def remove_non_matching(A, x, right):
    return filter(lambda l: (l[x] == right), A)

def start(A, common):
    for x in range(len(A[0])):
        A = list(filter(lambda l: (l[x] == gamma(A, common, x)), A))
        if len(A) == 1:
            return int("".join(str(i) for i in A),2)


file = "input.txt"
if len(sys.argv) == 2:
    if sys.argv[1] == "test":
        file = "test.txt"
gen_expected = 23
scrub_expecped = 10

inp = [i.rstrip() for i in open(file, "r")]
print(gamma(inp, True, 0))
gen_value = start(inp, True)
scrup_value = start(inp, False)
if (file == "test.txt"):
    if not gen_value == gen_expected:
        print(f"generator value is {gen_value} expected {gen_expected}")
    if not scrup_value == scrub_expecped:
        print(f"scrup value is {scrup_value} expected {scrub_expecped}")

print(f"prosuct = {gen_value* scrup_value}")
