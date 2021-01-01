from random import randint
ele_AND_1 = open("Ele_AND_1.txt")
ele_AND_1 = [int(i) for i in ele_AND_1]
print(ele_AND_1)

def gen_test1(n,k):
    temp = str(n) + "\n" + str(k)
    for i in range(n):
        j = randint(0,len(ele_AND_1))
        temp +=("\n" + str(ele_AND_1[j]))
    with open("test5.txt",'w') as f:
        f.write(temp)

def gen_test2(n,k):
    temp = str(n) + "\n" + str(k)
    for i in range(1,n-1):
        temp = temp + "\n" + str(randint(1,4096))
    with open("test1.txt",'w') as f:
        temp += '\n 0' # Do output của test này là 0 nên phải thêm giá trị vào cuối (tất cả phép and với 0 thì bằng 0)
        f.write(temp)


def gen_test3(n,k):
    temp = str(n) + "\n" + str(k)
    for i in range(n):
        temp +=("\n" + str(1))
    with open("test2.txt",'w') as f:
        f.write(temp)



def check():
    f = open("test1.txt")
    a = f.readlines()
    print(len(a))
n = randint(1,20000)
k = randint(1,n)
#gen_test1(n,k)