f = open("Input/test3.txt")
inp = f.readlines()
n,k = int(inp[0]), int(inp[1])
a = inp[2:]
a = [int(i) for i in a]

def solution(n,k,a):
    count_one = [0] * 12
    x = k
    check = False
    for i in a[:k]:
        for bit in range(12):
            if (1 << bit) & i:
                count_one[bit] += 1
            if count_one[bit] == k:
                check = True
    if check == False:
        return "YES"
    while x < n:
        check = False
        l,r = x - k, x
        for bit in range(12):
            if (1 << bit) & a[l]:
                count_one[bit] -= 1
            if (1 << bit) & a[r]:
                count_one[bit] += 1
            if count_one[bit] == k:
                check = True
        if check == False:
            return "YES"
        x += 1
    
    return "NO"

result = solution(n,k,a)
print(result)