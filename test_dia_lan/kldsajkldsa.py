f = open("test5.txt")
a = f.readlines()
ff = open("Ele_AND_1.txt")
b = ff.readlines()
for i in a:
    if i not in b:
        print(i)
        print("Found!")