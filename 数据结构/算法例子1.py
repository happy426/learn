"""
算法（Algorithm）是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令，
算法代表着用系统的方法描述解决问题的策略机制。
也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。
如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。
不同的算法可能用不同的时间，空间或效率来完成同样的任务。
一个算法的优劣可以用空间复杂度与时间复杂度来衡量

算法的五大特征：
输入性：
输出性：
确定性：
有穷性：
可行性：
"""
# question:a+b+c = 1000, a**2+b**2=c**2,求a,b,c所有组合

# # 算法1：
# import time
# start = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print(a, b, c)
# end = time.time()
# print(end-start)  # 78.4884524345398


# # 算法2：
# import time
# start = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001-a):
#         c = 1000 - a - b
#         if c < a:
#             continue
#         if a**2+b**2 == c**2:
#             print(a, b, c)
# end = time.time()
# print(end-start)  # 0.3160667419433594

# 算法3：
import time
start = time.time()
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2+b**2 == c**2:
            print(a, b, c)
end = time.time()
print(end-start)  # 0.5367386341094971




