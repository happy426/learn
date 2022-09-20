# import fileinput
#
#
# with fileinput.input('../test02.txt') as file:
#     for line in file:
#         print(f'{fileinput.filename()} 第{fileinput.lineno()}行：{line}', end='')

import fileinput

# glob 匹配te开头的txt文件
'files 输入打开文件的名称即可'
with fileinput.input(files=('test.txt', '../test02.txt')) as file:
    for line in file:
        # fileinput.lineno() 把两个文件的整合陈一个文件对象file，需要排序输出
        print(f'{fileinput.filename()} 第{fileinput.lineno()}行: {line}', end='')

        # fileinput.filelineno()两个文件单独读取，需要单独排序
        print(f'{fileinput.filename()} 第{fileinput.filelineno()}行: {line}', end='')
