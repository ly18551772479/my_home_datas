import time
# 起始时间
start_time = time.time()

# 猜两个
for a  in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a,b,c: %d,%d,%d" % (a,b,c))

#  结束时间
end_time = time.time()
cost = end_time - start_time
if __name__ == '__main__':
    print("花费时间: %f" % (cost))