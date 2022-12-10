"""float_num = float(11)
print(type(float_num),float_num)

float_num1 = str(float_num)
print(type(float_num1),float_num1)

num = 1
num += 1
print(num)

num -= 1
print(num)

num *= 4
print(num)

num /= 1.1
print(num)

num **= 3
print(num)

num %= 2
print(num)"""

#三种变量定义法（都可以）
"""name = '贾增元'
print(name)

name = "贾增元"
print(name)

name = '''贾增元'''
print(name)"""

"""name = "贾增元"
print("\"name\"")"""

#通过“+”可以拼接
"""print("1"+"哈哈")"""

#字符串格式化,通过%进行拼接
"""name = "贾增元"
age = 12
love = "原神"
shengao = 1.75
print("我的名字是：%s,年龄是%d，身高是%f，喜欢的游戏是%s"%(name,age,shengao,love))"""

"""字符串-数字精度控制"""
"""num1 = 11
num2 =11.345
print("数字11宽度显示5.结果是%5d"%num1)
print("数字11宽度限制1，结果是%1d"%num1)
print("数字11.34宽度限制7，小数位精度是2，结果是%7.2f"%num2)
print("数字11.345宽度不限制，小数精度是2，结果是%.2f"%num2)"""

"""快速格式化"""
"""name = "贾增元"
age = 12
love = "原神"
shengao = 1.75
print(f"我的名字是{name},年龄是{age}，爱好的游戏是{love}，身高是{shengao}米")"""

"""print("1*1的结果是%d"%(1*1))
print(f"1*1的结果是{1*1}")"""

"""company = "元元科技有限公司"
stock_price = 19.99
stock_code = "00302"
stock_price_daily_growth_factor = 1.2
growth_days = 7
final_price = stock_price*(stock_price_daily_growth_factor**growth_days)
print(f"公司：{company},股票代码{stock_code}，当前股价{stock_price}")
print("每日增长系数%.1f，经过%d天的增长后，股价达到了%.2f"%(stock_price_daily_growth_factor,growth_days,final_price))"""


"""name = input("请输入你的名字")
print(f"我知道了，你是{name}")
age = input("请输入你的年龄")
age = int(age)
print(type(age))"""

"""user_name = input("请输入你的名字")
user_type = "SVVVVVIP"
print(f"您好，{user_name}，您的身份是{user_type}")"""

#逻辑判断
#布尔类型：是或否


#if语句
"""age = input("年龄")
age = int(age)
if age >= 18:
    print("我已经成年了，即将步入大学生活")

print("生活过的真快啊")"""

#练习案例:成年人【按断

"""print("欢迎来的元元的游乐园，儿童（10岁以下）免费，成人收费")
age = input("请输入你的年龄")
age = int(age)
if age >= 10:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快！")"""

#练习案例：我要买票吗
"""print("欢迎来到元元的游乐园")
shengao = int(input("请输入你的身高"))
if shengao >120:
    print("你的身高超过120cm，游玩需要购票")
else:
    print("你的身高未超过120cm，游玩无需购票")"""


"""print("欢迎来到元元的游乐园")
shengao = int(input("请输入你的身高"))
VIp = int(input("请输入你的VIP等级"))
day = int(input("今天是几号"))
if shengao <120:
    print("你的身高未超过120cm，游玩无需购票")
elif VIp>=3:
    print("你的VIP等级达到了3级，您可以免费游玩")
elif day==1:
    print("今天是1号，可以免费游玩哈")
else:
    print("你需要付费哦")"""

"""if int(input("请输入你的身高")) <120:
    print("你的身高未超过120cm，游玩无需购票")
elif int(input("请输入你的VIP等级"))>=3:
    print("你的VIP等级达到了3级，您可以免费游玩")
elif int(input("今天是几号"))==1:
    print("今天是1号，可以免费游玩哈")
else:
    print("你需要付费哦")"""

"""my_num = 10
if int(input("请输入第一次猜想的数字")) == my_num:
    print("好厉害啊，猜对了")
elif int(input("猜错了，再来一次")) == my_num:
    print("好厉害啊，猜对了")
elif int(input("最后一次机会")) == my_num:
    print("好厉害啊，猜对了")
else:
    print(f"sorry，全部猜错了，我想的数字是{my_num}")"""

"""print("欢迎来到元元的游乐园")
if int(input("请输入你的身高")) > 120:
    if int(input("请输入你的会员等级（1-5）")) < 3:
        if int(input("今天是几号")) == 1:
            print("您可以免费游玩")
    else:
        print("您可以免费游玩哈")
else:
    print("您可以免费游玩")
"""

"""if 18 <= int(input("请输入年龄")) <= 30:
    if 2 <= int(input("请输入你的入职时间")):
        print("您符合领取要求")
    elif 3 <= int(input("请输入你的级别")):
        print("您符合领取要求")
    else:
        print("您不符合领取要求")
else:
    print("您不符合领取要求")"""

"""import random
num = random.randint(1,10)
#print(f"随机数字是{num}")
one_num = int(input("请输入第一次猜想的数字"))
if one_num == num:
    print("好厉害猜对了")
else:
    if one_num > num :
        print("猜错了，大了")
    else:
        print("猜错了，小了")
    two_num = int(input("请输入第2次猜想的数字"))
    if two_num == num:
        print("好厉害猜对了")
    else:
        if two_num > num:
            print("猜错了，大了")
        else:
            print("猜错了，小了")
        three_num = int(input("最后一次"))
        if three_num == num:
            print("好厉害猜对了")
        else:
            print("都不对哦，游戏结束")
"""

"""num = 0
while num <= 100:
    print("小元元",num)
    num += 1"""
#练习作业：求1-100的和
"""i = 1
sum = 0
while i <=100:
    sum = sum + i
    i = i+1
print(sum)"""

"""import random
num = random.randint(1,100)
flag = True
caice_num = 0
while flag:
    shuru_num = int(input("请输入猜想数字"))
    caice_num += 1
    print(f"你已经猜了{caice_num}次")
    if shuru_num == num:
        print("猜对了")
        break
    else:
        if shuru_num > num:
            print("大了")
        else:
            print("小了")"""

"""i = 1
while i<=100:
    print(f"今天是表白第{i}天")
    i += 1
    j = 1

    while j <= 10:
        print(f"送给小美的第{j}朵花")
        j+=1
print("hhh")"""

#九九乘法表
"""i=1
while i<10:
    j=1
    while j<=i:
        print(f"{j}*{i}={i*j}",end="   ")
        j+=1
    i += 1
    print("")"""
#for循环
"""name = "yuanyuan"
for X in name:
    print(X)"""
"""
name = "yuanyuanyuanyuan"

num=0
for x in name:
    if x == "a":
        num+=1
print(num)
"""

num = 0
for x in range(1,100):
    if x % 2 == 0:
        num+=1
print(num)
