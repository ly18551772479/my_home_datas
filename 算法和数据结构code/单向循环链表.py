class BaseNode(object):
    # 对象基本属性：item和next
    def __init__(self,item):
        self.item = item
        self.next = None

class CycleLinkList():
    # 自动获取链表头结点
    def __init__(self,node=None):
        self.__head = node

    # 单向循环链表判空
    def is_empty(self):
        return self.__head is None

    # 单向循环链表长度
    def length(self):
        # 准备功能：标签+计数器
        cur = self.__head
        count = 1

        # 异常
        if self.is_empty():
            return 0
        else:
            while cur.next is not self.__head:
                count += 1
                cur = cur.next
            #  这个时候，退出循环，标签在尾结点
            return count

    # 单向循环链表内容
    def travel(self):
        # 准备功能：标签
        cur = self.__head
        # 异常
        if self.is_empty():
            print("")
        else:
            while cur.next is not self.__head:
                print(cur.item,end=" ")
                cur = cur.next
            #  这个时候，退出循环，标签在尾结点
            print(cur.item)


    # 单向循环链表查找内容
    def search(self,item):
        # 准备功能：标签
        cur = self.__head
        # 异常
        if self.is_empty():
            return False
        else:
            while cur.next is not self.__head:
                if cur.item == item:
                    return True
                cur = cur.next
            #  这个时候，退出循环，标签在尾结点
            if cur.item == item:
                return True
            else:
                return False

    # 单向循环链表头部增加内容
    def  add(self,item):
        # 顺序：实例化节点-位置(头+尾)-属性
        node = BaseNode(item)
        cur = self.__head
        # 异常情况：空链表
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 非空链表
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环，标签在尾结点上
            cur.next = node
            node.next = self.__head
            self.__head = node

    # 单向循环链表尾部增加内容
    def append(self,item):
        # 顺序：实例化节点-位置(头+尾)-属性-异常
        node = BaseNode(item)
        # 空链表情况
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 非空链表找尾结点
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 修改属性
            cur.next = node
            node.next = self.__head
    # 单向循环链表指定位置增加内容
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

    # 单向循环链表删除内容
    def remove(self,item):
        # 准备工作
        cur = self.__head
        pre = None
        # 步骤：判空-匹配-位置-修改属性-异常
        # 空链表处理：
        if self.is_empty():
            return

        # 非空链表的删除：
        while cur.next is not self.__head:
            if cur.item == item:
                # 删除头结点，要找尾结点
                if cur == self.__head:
                    tnode = self.__head
                    while tnode.next is not self.__head:
                        tnode = tnode.next
                    # 属性修改
                    self.__head = cur.next
                    tnode.next = self.__head
                # 中间位置
                else:
                    pre.next = cur.next
                return
            # 标签移动
            pre = cur
            cur = cur.next
        # 尾结点处理
        if cur.item == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head
        else:
            return


if __name__ == '__main__':
    ll = CycleLinkList()
    ll.add(7)
    ll.add(99)
    ll.append(23)
    ll.insert(2,100)
    ll.remove(7)
    ll.travel()

