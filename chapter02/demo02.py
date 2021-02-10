# 数据类型


# 整数类型
# 可以表示 正数、负数、0
n1 = 90
n2 = -79
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
# 整数可以表示为 二进制、十进制、八进制、十六进制
print('十进制', 118)
print('二进制', 0b10101111)  # 二进制以 0b 开头
print('八进制', 0o176)  # 八进制以 0o 开头
print('十六进制', 0x1EAF)

# 浮点类型
a = 3.14159
print(a, type(a))
num1 = 1.1
num2 = 2.2
print(num1 + num2)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

# 布尔类型
# True -> 1
# False -> 0

f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))

# 布尔值可以转成整数计算
print(f1 + 1)  # 2
print(f2 + 1)  # 1

# 字符串类型
str1 = '人生苦短，我用Python'
print(str1, type(str1))
