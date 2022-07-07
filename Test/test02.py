import os
import shutil

# 删除文件
# os.remove('./result/text.txt')
# 拷贝文件
# os.system(r'copy D:\pylearn\learn\learn\Test\result\test01.txt D:\pylearn\learn\learn\Test\result\test02.txt')
shutil.copy('./result/test01.txt', 'result/test03.txt')

