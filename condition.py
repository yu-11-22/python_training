# 判斷式
x=input("請輸入數字:") #取得字串形式的使用者輸入
x=int(x) #int是將字串型態轉換成數字型態
if x>=200:
    print("大於等於 200")
elif x>=100:
    print("大於等於 100, 小於 200")
else:
    print("小於 100")
# 四則運算
n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
print(n1+n2)
# 計算機
x1=int(input("請輸入數字一:"))
x2=int(input("請輸入數字二:"))
op=input("請輸入運算符號:( +, -, *, /):")
if op=="+":
    print(x1+x2)
elif op=="-":
    print(x1-x2)
elif op==("*"):
    print(x1*x2)
elif op==("/"):
    print(x1/x2)
else:
    print("不支援的運算")