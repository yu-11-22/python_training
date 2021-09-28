# 數字運算
x=7//6 # 整數除法
print(x)
x=2**3 #2的3次方
print(x)
x=8%3 #取餘數
print(x)
x=2+3
print(x)
x+=1 # x=x+1 # 等號後方會先看,變數中的數字+1
print(x)

# 字串運算
s="Hello" #單引號也可以
print(s)
s="Hel\"lo" #加上\可以讓引號變字串
print(s)
s="Hello"+"world" #"空白"或是"+"代表字串串接
print(s)
s="Hello\nworld" #"\n"會隔一行
print(s)
s="""Hello
my
wonderful
world""" # 3個引號也可以換行
print(s)
s="Hello"*2+"world"*3
print(s)
# 字串會對內部的字元編號(索引),從0開始算起
s="Hello"
print(s[0])
print(s[1:4])
print(s[1:])
print(s[:4])