# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "=", i*j, end=" , ")
    print(end="\n")
# 正方形乘機
for i in range(1, 10):
    print(("%3d") % (i), end="")
    for j in range(1, 10):
        print(("%3d") % (j*i), end="")
    print(end="\n")
