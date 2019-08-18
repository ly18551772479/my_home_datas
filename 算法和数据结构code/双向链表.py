class BaseNode(object):
    # 对象基本属性：item和next\pre
    def __init__(self,item):
        self.pre = None
        self.item = item
        self.next = None

class DoubleLinkList(object):
    # 自动获取链表头结点
    def __init__(self,node=None):
        self.__head = node

    # 双向链表判空
    def is_empty(self):
        return self.__head is None

    # 双向链表长度
    def length(self):
        # 准备工作：标签+计数器
        cur = self.__head
        count = 0
        # 遍历循环
        while cur is not None:
            count += 1
            cur = cur.next
        # 返回总数量
        return count

    # 双向链表所有内容
    def travel(self):
        # 准备工作：标签
        cur = self.__head
        # 遍历循环
        while cur is not None:
            print(cur.item,end=" ")
            cur = cur.next
        # 修复格式
        print("")

    # 双向链表指定内容
    def search(self,item):
        # 准备工作：标签
        cur = self.__head
        # 遍历循环
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        # 异常情况
        return False

    # 双向链表头增加
    def add(self,item):
        # 步骤：实例化节点-找位置-改属性
        node = BaseNode(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.pre = node

    # 双向链表尾增加
    def append(self,item):
        # 步骤：实例化节点-找位置-改属性-异常
        node = BaseNode(item)
        cur = self.__head
        # 异常
        if self.is_empty():
            self.__head = node
        # 找尾结点
        while cur.next is not None:
            cur = cur.next
        # 修改尾结点属性
        cur.next = node
        node.pre = cur

    # 指定位置增加
    def insert(self,pos,item):
        # 步骤：实例化节点-找位置(判断位置)-改属性
        node = BaseNode(item)
        # 头和尾使用现有方法
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        # 中间位置
        else:
            count = 0
            cur = self.__head
            # 找位置
            while count < pos:
                count += 1
                cur = cur.next
            # 改属性
            cur.pre.next = node
            node.pre = cur.pre
            node.next = cur
            cur.pre = node

    # 删除内容
    def remove(self,item):
        cur = self.__head
        # 删除流程：判空-匹配-位置-异常
        while cur is not None:
            if cur.item == item:
                # 头位置
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        self.__head.pre = None
                # 其他位置
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                return
            # 异常情况
            cur = cur.next

if __name__ == '__main__':
    ll = DoubleLinkList()
    ll.add(5)
    ll.add(8)
    ll.append(78)
    ll.insert(2,99)
    ll.remove(5)
    ll.travel()

