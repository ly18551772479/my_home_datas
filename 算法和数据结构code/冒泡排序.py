def maopao(alist):
    n = len(alist)
    # 外部冒泡循环
    for j in range(n-1,0,-1):
        # 排序异常处理：计数器
        count = 0
        # 内部比较循环
        for i in range(j):
            # 相邻元素比较
            if alist[i] < alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            break

if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    maopao(li)
    print(li)
