# 有序可變動的列表 List
grades=[12,60,15,70,90]
print(grades)
grades[0]=55 #把列表中的第一個位置更新
print(grades)
print(grades[0])
grades=[12,60,15,70,90]
grades[1:4]=[] # 連續刪除列表中編號1到編號4(不包含)的資料
print(grades)
grades=[12,60,15,70,90]
grades+=[12,33]
print(grades)
grades=[12,60,15,70,90]
length=len(grades) #取得列表的長度 len(列表資料)
print(length)
print(len(grades))
data=[[3,4,5],[6,7,8]] #巢狀列表
print(data[0][1])
data[0][0:2]=[5,5,5]
print(data[0])
# 有序不可變動的列表 Tuple
data=(3,4,5)
print(data[1])
data=(3,4,5)
data[0]=5 #錯誤: Tuple 的資料不可變動
print(data)