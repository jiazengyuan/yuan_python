# 字符串
# 字符串的替换
my_str = "贾增元，yuanyuan"
new_str = my_str.replace("元","圆")
print(my_str)
print(new_str)

# 字符串分隔
my_str = "贾增元 yuan yuan quan 圈圈"
my_str_list = my_str.split(" ")
print(my_str_list)

# 去除首尾空格
my_str = " 贾增元 yuan yuan quan 圈圈 "
new_str = my_str.strip()
print(new_str)
print(my_str)

# 去除首位特定值
my_str = "na贾增元 yuan yuan quan 圈圈 12 yu"
new_str = my_str.strip("yuan")
print(new_str)
print(my_str)