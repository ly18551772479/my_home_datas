class BaseNode(object):
    # 对象基本属性：item和next
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkList():
    # 自动获取链表头结点
    def __init__(self,node=None):
        self.__head = node

    # 单向链表判空
    def is_empty(self):
        return self.__head is None

    # 单向链表长度
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

    # 单向链表所有内容
    def travel(self):
        # 准备工作：标签
        cur = self.__head
        # 遍历循环
        while cur is not None:
            print(cur.item,end=" ")
            cur = cur.next
        # 修复格式
        print("")

    # 单向链表指定内容
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

    # 头部增加内容
    def add(self,item):
        # 步骤：实例化节点-找位置-改属性
        node = BaseNode(item)
        node.next = self.__head
        self.__head = node

    # 尾部增加结点
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
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 改属性
            node.next = cur.next
            cur.next = node

    # 删除尾结点
    def remove(self,item):
        # 准备工作： 两个标签
        cur = self.__head
        pre = None
        # 删除流程：判空-内容匹配-位置-异常
        while cur is not None:
            if cur.item == item:
                # 头
                if cur == self.__head:
                    self.__head = cur.next
                # 其他位置
                else:
                    pre.next = cur.next
                return
            # 异常情况
            pre = cur
            cur = cur.next

if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(5)
    ll.add(8)
    ll.append(6)
    ll.insert(2,7)
    ll.remove(5)
    ll.travel()


