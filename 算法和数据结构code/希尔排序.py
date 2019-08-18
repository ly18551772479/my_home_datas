def xier(alist):
    n = len(alist)
    gap = n // 2
    # 希尔排序需要进行多少次？
    while gap >= 1:
        # 一次希尔需要有多少个组进行插入排序
        for i in range(gap,n):
            # 组内元素插入排序的前提：
            while (i-gap) >= 0:
                # 分组内元素插入排序
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    # 目的：过程跟踪
                    i = i - gap
                else:
                    break
        # 每次希尔后，偏移量都应该/2
        gap = gap // 2

if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    xier(li)
    print(li)