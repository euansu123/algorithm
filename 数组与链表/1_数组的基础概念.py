"""
数组(array)是一种线性数据结构,其将相同类型的元素存储在连续的内存空间中。
我们将元素在数组中的位置称为该元素的索引(index)。
"""
# 初始化数组
import random
arr: list[int] = [0] * 5
nums: list[int] = [1, 3, 2, 5, 4]

def random_access(nums: list[int]) -> int:
    """随机访问数组元素"""
    # 1.在区间内随机抽取一个数字作为数组的索引
    random_index = random.randint(0, len(nums) - 1)
    # 2.获取索引处对应的值
    random_num = nums[random_index]
    return random_num

def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素"""
    # 把索引index处及之后的元素向后移动一位
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i-1]
    # 将元素num赋值给索引index处
    nums[index] = num

def remove(nums: list[int], index: int):
    """删除索引 index 处的元素"""
    # 把索引index之后的元素向前移动一位
    for i in range(index, len(nums)-1):
        nums[i] = nums[i+1]

def traverse(nums: list[int]):
    """遍历数组"""
    # 通过索引遍历数组
    for i in range(len(nums)):
        print(nums[i])

    # 直接遍历数组
    for num in nums:
        print(num)

    # 同时遍历数据索引和元素
    for i,num in enumerate(nums):
        print(i, num)

def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素，返回元素的索引"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

def extend(nums: list[int], enlarge_length: int):
    """扩展数组长度"""
    # 初始化一个扩展长度后的数组
    res: list[int] = [0] * (len(nums) + enlarge_length)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

if __name__=='__main__':
    random_num = random_access(nums)
    print(random_num)
    nums: list[int] = [1, 5, 2, 0, 4, 7]
    insert(nums, 3, 3)
    print(nums)
    nums: list[int] = [1, 5, 3, 0, 4, 7]
    remove(nums, 2)
    print(nums)
    traverse(nums)

    new_nums = extend(nums, 3)
    print(new_nums)