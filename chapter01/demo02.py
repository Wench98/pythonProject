print('hello\nworld')

print('hello\twench')

print('hello\rwench')

print('hello\bwench')

print('http://www.baidu.com\\')

print('teacher said:\'hello everybody\'')

# 原字符，不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r，或R
print(r'hello \n wench')
# 注意事项：最后一个字符不能是反斜杠 不可以是单个的 "\"
# print(r'hello \n wench\')
print(r'hello \n wench\\')
