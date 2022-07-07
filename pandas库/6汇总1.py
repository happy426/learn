import numpy as np
import pandas as pd

"""
文件读取
"""
data = pd.read_csv('data/train.csv')
data_table = pd.read_table('data/train.csv')  # read_table以\t来读取文件，可以读取txt
df = pd.DataFrame(data)
df_table = pd.DataFrame(data_table)
print(df)
"""
表信息查看
"""
# print(df.shape)  # 查看表维度
print(df.info())  # 查看表信息
# print(df.head())  # 查看表前五行
# print(df.tail())  # 查看后前五行
# print(df_table.info())
# print(df.isnull)
# print(df.values)  # 查看表值
# print(df.columns)  # 查看表列名称
# print(df.index)  # 查看表索引

"""
数据表清洗
"""
# df = df.fillna(0)  # 表空值填充0
# print(df)
# 要清洗数据格式
# print(df.fillna(df.mean()))  # 均值填充
# print(df['time'].fillna(df['time'].mean()))
# df['city'] = df['city'].str.lower()  # 大小写转换 upper()
# print(df['city'])
# df['time'] = df['time'].astype(int)  # 更改数据格式
# print(df['time'].dtype)
# print(df.rename(columns={'city': 'ziMu'}))  # 更改列名
print(df['city'].replace('aa', 'bb'))  # 替换



