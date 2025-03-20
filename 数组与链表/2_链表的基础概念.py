"""
内存空间是所有程序的公共资源，在一个复杂的系统运行环境下，空闲的内存空间可能散落在内存各处，而存储数组的内存空间必须是连续的，当数组非常大时，内存可能无法提供如此大的连续空间。
在这种场景下，链表灵活的优势特性就体现出来了，链表（linkedlist）是一种线性数据结构，其中的每个元素都是一个节点对象，各个节点通过“引用”相连接。引用记录了下一个节点的内存地址，通过它可以从当前节点访问到下一个节点。
链表的设计使得各个节点可以分散存储在内存各处，它们的内存地址无须连续。
"""

class ListNode:
    """链表节点类"""
    def __init__(self, val:int):
        self.val = val                      # 节点值
        self.next : ListNode | None = None  # 指向下一节点的引用

# 链表的初始化操作
# 初始化链表 1-> 3 ->2 ->5 -> 4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# 插入节点
def insert(n0: ListNode, p:ListNode):
    """在链表的n0和n1之间插入p"""
    n1 = n0.next
    p.next = n1
    n0.next = p

# 删除节点
def delete(n0: ListNode):
    p = n0.next
    n0.next = p.next

# 访问节点
def access(head:ListNode, index:int) -> ListNode | None:
    for _ in range(index):
        if head is None:
            return None
        head = head.next
    return head

r = access(n0, 3)
print(r.val)

# 查找节点
def find(head:ListNode, target:int) -> int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1

    return -1
r = find(n0, 6)
print(r)

# 双向链表
class ListNode:
    """双向链表节点类"""
    def __init__(self, val:int):
        self.val = val                      # 节点值
        self.next: ListNode | None = None   # 指向后继节点的引用
        self.prev: ListNode | None = None   # 指向前驱节点的引用