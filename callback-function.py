def test(arg):
    arg()  # 呼叫回呼函式

# 定義一個回呼函式


def handle():
    print(100)


test(handle)


def test(arg):
    arg("Hello")  # 呼叫回呼函式，代入參數

# 定義一個回呼函式


def handle(data):
    print(data)


test(handle)

# 實例


def add(n1, n2, cb):
    cb(n1+n2)


def handle1(result):
    print("結果是", result)


def handle2(result):
    print("result of add is", result)


add(3, 4, handle1)
add(4, 2, handle2)
