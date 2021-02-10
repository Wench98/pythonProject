name = '张三'
age = 20
print(type(name), type(age))  # 说明 name 与 age 的数据类型不相同
print('my name is ' + name + '. ' + str(age) + " years old")

print('------ use str() to transform other parameter type to string type ------')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(a), type(b), type(c))

print('------ use int() transform other to int ------')
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))  # 将 str 转成 int 类型，字符串为数字串
print(int(f1), type(int(f1)))  # 将 float 转成 int 类型，截取整数部分，舍掉小数部分
print(int(ff), type(int(ff)))

print('--- float()---')
