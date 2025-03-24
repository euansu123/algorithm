"""
列表（list）是一个抽象的数据结构概念，它表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作，无须使用者考虑容量限制的问题。列表可以基于链表或者数组实现。
"""
from itertools import count

# 1.列表的初始化操作
# 无初始化值
nums1: list[int] = []
# 有初始值
nums2: list[int] = [1, 2, 3, 4, 5]

# 2.访问元素
# 访问元素
num: int = nums2[1]  # 访问索引1处的元素
# 更新元素
nums2[1] = 0  # 将索引1处的元素更新为0

# 3.插入与删除元素
# 清空列表
nums2.clear()

# 在尾部添加元素
nums2.append(1)
nums2.append(2)
nums2.append(3)

# 在中间添加元素
nums2.insert(1, 1)  # 在索引 1 处插入数字1

# 删除元素
nums2.pop(1)  # 删除索引1处的元素

# 4.遍历列表
# 通过索引遍历列表
count = 0
for i in range(len(nums2)):
    count += nums2[i]

# 直接遍历列表元素
for num in nums2:
    count += num

# 5.拼接两个列表
nums3: list[int] = [1, 2, 3, 4, 5]
nums4: list[int] = [6, 7, 8, 9, 10]
nums3 += nums4  # 将列表nums4拼接到nums3之后

# 6.列表排序
nums5: list[int] = [1, 3, 5, 6, 4, 9]
nums5.sort()