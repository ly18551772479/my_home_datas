def guibing(alist):
    # 准备工作
    n = len(alist)
    # 异常：空列表
    if n <= 1:
        return alist

    # 正常递归
    mid = n // 2
    # 左分组
    zuo = guibing(alist[:mid])
    # 右分组
    you = guibing(alist[mid:])
    # 合并分组
    return merge(zuo,you)

def merge(zuo,you):
    #  准备工作：两标签+新队列
    l,r = 0,0
    result = []

    # 标签移动的前提：
    zuo_len = len(zuo)
    you_len = len(you)
    while l < zuo_len and r < you_len:
        # 左标签移动
        if zuo[l] < you[r]:
            result.append(zuo[l])
            l += 1
        #  右标签移动
        else:
            result.append(you[r])
            r += 1
    # 异常：有一个为空
    result += you[r:]
    result += zuo[l:]
    return result

if __name__ == '__main__':
    li = [2,6,3,8,12,7,75,34]
    print(li)
    print(guibing(li))
    print(li)

