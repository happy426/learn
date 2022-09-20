import fileinput
import glob

# glob 匹配te开头的txt文件
for line in fileinput.input(glob.glob("te*.txt")):
    if fileinput.isfirstline():
        # 输出读取文件
        print('=' * 10, f'读取文件{fileinput.filename()}', '=' * 10)
        # fileinput.filelineno()方法读取
    print(str(fileinput.filelineno()) + ':' + line.upper(), end='')
