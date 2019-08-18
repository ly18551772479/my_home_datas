def charu(alist):
    n = len(alist)
    # 外部插入循环
    for i in range(n):
        # 有序列表冒泡循环：
        for j in range(i,0,-1):
            # 有序列表元素比较: j和j-1比较
            if alist[j] > alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break
if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    charu(li)
    print(li)
