# 載入內建的 sys(取得系統相關資訊) 模組並取得資訊
import geometry
import sys as system
system.path.append("modules")  # 在模組的搜尋路徑列表中[新增路徑]
print(system.platform)  # platform:作業系統
print(system.maxsize)   # maxsize:整數型態最大值
# 建立 geometry 模組，載入使用
result = geometry.distance(1, 1, 4, 5)
print(result)
result = geometry.slope(1, 2, 5, 6)
print(result)
# 調整搜尋模組的路徑
print(system.path)      # path:搜尋模組的路徑
