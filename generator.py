# 定義建立生成器函式
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10


# 呼叫並回傳生成器
gen = test()
print(gen)
# 搭配 for 迴圈中使用
for d in gen:
    print(d)  # 5

# 實例(無限多偶數)


def generateEven():
    number = 0
    while True:
        yield number
        number += 2

evengenerator=generateEven()
for data in evengenerator():
    print(data)
# 實例


def generate(maxNumber):
    number = 0
    while number < maxNumber:
        yield number
        number += 2


Generator = generate(10)
for data in Generator:
    print(data)
