import numpy as np
import pandas as pd

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing', 'SH', 'guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})

print(df)
print(df1)
"""
数据表合并
merge(表1，表2，how=''), 相当于左右连接数据库里的join
append: 表1.append(表2)， 相当于数据库里的union
"""
df_inner = pd.merge(df, df1, how='inner')  # 匹配合并，交集
df_left = pd.merge(df, df1, how='left')  #
df_right = pd.merge(df, df1, how='right')
df_outer = pd.merge(df, df1, how='outer')  # 并集
print(df_left)

df1_append = df1.append(df)
print(df1_append)

# df = df.set_index('id')  # 设置索引列
# print(df.index.values)
# print(df.sort_values('age', ascending=False))  # 按照age排序，降序，ascending意思是上升的
# df['age'] = np.where(df['age']>32, 'up32', 'low32')
# print(df.where(df['age']>32))  # 查找过滤

"""
数据提取
loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取。
"""
# print(df.loc[0])  # 按照索引提取单行的值
# print(df.loc[0:3])  # 按照索引提取多行的值
# # df = df.set_index()  # 重设索引
# # print(df.loc[0]) # 重设索引后，就不能用了，需要设置索引
# df = df.set_index('id')
# print(df.loc[1001])

# print(df.iloc[0])  # 提取第一行
# print(df.iloc[0:5])  # 从第一行开始提取，提取出5行
# print(df.iloc[0:5:2])  # 从第一行开始提取，每隔两行取一行
# print(df.iloc[3, 3])  # 提取第四行第4列
# print(df.iloc[[0, 3], [2, 3]])  # 提取第一行和第四行的第3，4两列
# print(df['city'].str[0:2])  # 提取前两个字符

# print(df['id'].values)
"""
数据筛选
与 &
或 |
非 !=
表.query()
"""
# print(df.loc[(df['id']>1001) & (df['age']>32)])  # 与
# print(df.loc[(df['id']>1001) | (df['age']>32)])  # 或
# print(df.loc[df['age']!=32])  # 非
# df['city'] = df['city'].map(str.strip)  # 去除空格
# print(df.query('city == ["Beijing", "shanghai"]').price.sum())
# print(df.query('city == ["Beijing", "shanghai"]'))


"""
数据汇总
表.groupby()[].方法
count
sum
max
min
mean
"""
# print(df['age'].mean())  # 平均值
# print(df['age'].max())
# print(df.groupby('city').count())  # 对所有的列进行计数汇总
# print(df.groupby('city')['id'].count())  # 按城市对id字段进行计数
# print(df.groupby(['city', 'age'])['id'].count())  # 对两个字段进行汇总计数

"""
数据统计
"""
# print(df.sample(n=3))  # 简单的数据采样
# weights = [0, 0, 0, 0, 0.5, 0.5]
# print(df.sample(n=2, weights=weights))
# print(df.sample(n=6, replace=False))  # 采样后不放回
# print(df_inner.describe().round(2).T)  # round函数设置显示小数位，T表示转置


"""
数据输出
"""
# df.to_csv('data/df.csv')
