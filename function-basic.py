# 定義函式
# 函式內部的程式碼,如果沒有被呼叫,就不會執行
def multiply(n1, n2):
    print(n1*n2)


# 呼叫函式
multiply(7, 8)
# return把程式碼強制結束並以 return 為主


def add(n1, n2):
    print(n1+n2)
    return n1*n2


value = add(6, 8)  # 呼叫函式的值
print(value)       # 放入變數中,則以回傳值為主


def minus(n1, n2):
    return n1-n2


value = minus(10, 5)*minus(8, 6)
print(value)

# 程式的包裝: 同樣的邏輯可以重複利用


def calculate(max):
    sum = 0
    for n in range(max):
        n += 1
        sum += n
    print(sum)


calculate(10)
calculate(20)
