# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('Hello World')
print("Hello Wench")

# 含有运算符的表达式
print(3 + 1)

# 将数据输出到文件中
fp = open('/Users/wench/PycharmProjects/pythonProject/text.txt', 'a+')
print('Hello World', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('Hello', 'Wench', 'Python')
