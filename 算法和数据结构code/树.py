class BaseNode(object):
    def __init__(self,item):
        self.lsub = None
        self.item = item
        self.rsub = None

class Tree(object):
    # 树操作的基本属性：获取根节点
    def __init__(self,node=None):
        self.root = node

    # 增加结点
    def add(self,item):
        # 准备工作：结点
        node = BaseNode(item)
        # 空树处理
        if self.root == None:
            self.root = node
        # 非空树
        else:
            # 辅助工具；空队列
            queue = []
            queue.append(self.root)
            # 增加结点：父-左-右
            while len(queue) > 0:
                cur = queue.pop(0)
                # 左子节点处理
                if cur.lsub == None:
                    cur.lsub = node
                    return
                else:
                    queue.append(cur.lsub)
                # 右子节点处理
                if cur.rsub == None:
                    cur.rsub = node
                    return
                else:
                    queue.append(cur.rsub)

