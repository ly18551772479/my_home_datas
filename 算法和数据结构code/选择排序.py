def xuanze(alist):
    n = len(alist)
    # 外部选择循环
    for j in range(n-1):
        # 无序队列选择最小元素
        min_index = j
        # 比较循环
        for i in range(min_index+1,n):
            # 元素比较
            if alist[min_index] > alist[i]:
                min_index = i
        # 无序第一和最小替换
        if min_index != j:
            alist[min_index],alist[j] = alist[j],alist[min_index]


if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    xuanze(li)
    print(li)

