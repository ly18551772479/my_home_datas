def binary_search(alist, item):
    # 准备工作
    n = len(alist)
    # 列表空判断
    if n == 0:
        return False
    mid = n // 2
    # 中间值匹配
    if alist[mid] == item:
        return True
    # 左侧二分查找
    elif item < alist[mid]:
        return binary_search(alist[:mid], item)
    # 右侧二分查找
    else:
        return binary_search(alist[mid + 1:], item)

if __name__ == '__main__':
    li = [2,3,6,8,12,17,25,34]
    print(binary_search(li,17))
