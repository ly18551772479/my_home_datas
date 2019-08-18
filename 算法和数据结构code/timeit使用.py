import timeit

# 内置属性
def T1():
    li = []
    for i in range(1000):
        li.append(i)

# 列表拼接
def T2():
    li = []
    for i in range(1000):
        li = li + [i]

# 列表推导
def T3():
    li = [i for i in range(1000)]

# 属性转换
def T4():
    li = list(range(1000))

if __name__ == '__main__':
    time1 = timeit.Timer("T1()","from __main__ import T1")
    cost1 = time1.timeit(1000)
    print("内置属性：%f" % (cost1))

    time2 = timeit.Timer("T2()","from __main__ import T2")
    cost2 = time2.timeit(1000)
    print("列表拼接：%f" % (cost2))

    time3 = timeit.Timer("T3()","from __main__ import T3")
    cost3 = time3.timeit(1000)
    print("列表推导：%f" % (cost3))

    time4 = timeit.Timer("T4()","from __main__ import T4")
    cost4 = time4.timeit(1000)
    print("属性转换：%f" % (cost4))