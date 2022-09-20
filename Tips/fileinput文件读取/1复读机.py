"""
先来看一下fileinput的基本功能：
fileinput.filename()：返回当前被读取的文件名。 —>在第一行被读取之前，返回 None。
fileinput.fileno()：返回以整数表示的当前文件“文件描述符”。 —>当未打开文件时（处在第一行和文件之间），返回 -1。
fileinput.lineno()：返回已被读取的累计行号。 —>在第一行被读取之前，返回0。在最后一个文件的最后一行被读取之后，返回该行的行号。
fileinput.filelineno()：返回当前文件中的行号。 —>在第一行被读取之前，返回 0。
—>在最后一个文件的最后一行被读取之后，返回此文件中该行的行号。
"""
import fileinput

'当 Python 脚本没有传入任何参数时，fileinput 默认会以 stdin 作为输入源'
for line in fileinput.input():
    print(f'{line}')



