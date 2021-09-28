# 隨機模組
import statistics as stat
import random
# 隨機選取
data = random.choice([1, 5, 6, 10, 20])  # 隨機選取一個
print(data)
data = random.sample([1, 5, 6, 10, 20], 3)  # 隨機選取三個
print(data)
# 隨機調換順序
data = [1, 5, 8, 20]
random.shuffle(data)
print(data)
# 隨機取得亂數
data = random.random()    # 0 ~ 1 之間的隨機亂數
print(data)
# 取得亂數較適用的方法
data = random.uniform(60, 100)
print(data)
# 取得常態分配亂數
data = random.normalvariate(100, 10)   # 平均數100 標準差10 資料約在90 ~ 110
print(data)
# 統計模組
data = stat.mean([1, 2, 3, 4, 5, 8, 100])          # 平均數
print(data)
data = stat.median([1, 2, 3, 4, 5, 8, 100])        # 中位數
print(data)
data = stat.stdev([1, 2, 3, 4, 5, 8, 10])          # 標準差
print(data)
