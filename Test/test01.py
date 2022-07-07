a = [4,5,6,7,3,2,4,2,1]


# # 冒泡
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j+1], a[j] = a[j], a[j+1]
# print(a)

# # 插入
# for i in range(1, len(a)):
#     for j in range(i,0,-1):
#         if a[j]<a[j-1]:
#             a[j], a[j-1] = a[j-1],a[j]
# print(a)

# 选择
for i in range(len(a)-1):
    index = i
    for j in range(i+1,len(a)):
        if a[j]<a[index]:
            index = j
    a[i],a[index] = a[index],a[i]
print(a)





