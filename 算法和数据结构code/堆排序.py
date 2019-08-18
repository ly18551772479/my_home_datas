def tiaozheng(alist,low,high):
    # 准备工作
    i = low
    j = 2 * i + 1
    tmp = alist[i]

    while j <= high:
        # 选择最大子节点
        if j+1 <= high and  alist[j] < alist[j+1]:
            j = j + 1
        # 最大子节点和堆顶元素比较
        if alist[j] > tmp:
            alist[i] = alist[j]
            i = j
            j = 2 * i + 1
        else:
            break
    # 临时堆顶元素归位
    alist[i] = tmp

# 堆排序代码
def heap_sort(alist):
    # 准备工作：长度
    n = len(alist)
    # 无序队列从n/2-1位置开始构造
    for i in range(int(n/2)-1,-1,-1):
        tiaozheng(alist, i, n-1)
    # 堆排序，堆尾元素标签假设为j
    for j in range(n-1,-1,-1):
        # 堆首尾替换
        alist[j],alist[0] = alist[0],alist[j]
        tiaozheng(alist, 0, j - 1)
    # 返回调整后的队列
    return alist

if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    heap_sort(li)
    print(li)