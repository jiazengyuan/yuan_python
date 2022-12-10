# #数据容器
# #列表list、元组、字符串、集合、字典
# user = ['yuanyuan',[1,2,3],'quanquan']
# print(user)
# print(type(user))
#
# #正序取数据
# print(user[0])
# print(user[1])
# print(user[2])
#
# #倒序取数据
# print(user[-1])
# print(user[-2])
# print(user[-3])
#
# #取嵌套列表数据
# print(user[1][2])
#
# #查询元素值的下标索引
# index = user.index("quanquan")
# print(index)
#
# #修改下标索引元素值
# user[2] = "quanq"
# user[1] = "quanq"
# print(user)
#
# #插入元素,在第X个索引除插入值
# user.insert(0,"sss")
# print(user)
#
# user1 = ['yuanyuan',[1,2,3],'quanquan']
# #尾部插入单个,是将插入的作为一个整体插入
# user1.append(["插入值1","插入值2","插入值3","插入值4"])
# print(user1)
#
# user2 = ['yuanyuan',[1,2,3],'quanquan']
# #尾部批量插入，是将插入的拆分成元素一个一个插入
# user2.extend(["插入值1","插入值2","插入值3","插入值4"])
# print(user2)
#
# #删除元素值,语法一
# user3 = ['yuanyuan',[1,2,3],'quanquan']
# del user3[1]
# print(user3)
#
# #删除元素值,语法一,通过取出
# user4 = ['yuanyuan',[1,2,3],'quanquan']
# quchu_value = user4.pop(1)
# #输出取出值
# print(quchu_value)
# #输出最终值
# print(user4)
#
# #指定元素值删除
# user5 = ['yuanyuan',[1,2,3],'quanquan']
# user5.remove("yuanyuan")
# print(user5)
#
# #清空列表内容
# user6 = ['yuanyuan',[1,2,3],'quanquan']
# user6.clear()
# print(user6)
#
# #统计元素值的数量
# user7 = ['yuanyuan',[1,2,3],'quanquan',"quanquan"]
# count = user7.count("quanquan")
# print(count)
#
# #统计列表中全部元素的数量
# user8 = ['yuanyuan',[1,2,3],'quanquan',"quanquan"]
# count = len(user8)
# print(count)
#
#

# 练习案例
student_age = [21,25,21,23,22,20]
#追加数字31到尾部
student_age.append(31)
print(f"追加后数组是：{student_age}")
# 追加一个新列表到尾部
student_age.extend([29,33,30])
print(f"追加后数组是：{student_age}")
# 取出一个元素
quchu_vavle = student_age.pop(0)
print(f"取出的值是：{quchu_vavle}")
#取出最后一个元素
quchu_vavle = student_age.pop(-1)
print(f"取出的值是：{quchu_vavle}")
#查找元素31的下标位置
print(student_age.index(31))
print(student_age)