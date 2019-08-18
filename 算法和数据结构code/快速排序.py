def quick_sort(alist,start,end):
    # 递归拆分到什么时候？
    if start < end:
        # 挑元素划分组准备工作：三标签
        mid = alist[start]
        left = start
        right = end
        # 左右交互移动
        while left < right:
            #右标签移动
            while left < right and alist[right] >= mid:
                right -= 1
            alist[left] = alist[right]

            #右标签移动
            while left < right and alist[left] < mid:
                left += 1
            alist[right] = alist[left]
        # 中间元素归位
        alist[left] = mid

        # 分组重复前两步
        quick_sort(alist, start, left-1)
        quick_sort(alist, left+1, end)

if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)

