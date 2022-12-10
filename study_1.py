"""for x in range(1,10):
    for j in range(1,x+1):
        print(f"{x}*{j}={x*j}",end=" ")
    print("")"""

# 练习案例发工资,方式1
"""company_account = 10000
staff_num = range(1,21)
for x in staff_num:
    import random
    achievements = random.randint(1,10)
    if achievements >= 5:
        company_account -= 1000
        print(f"员工{x}的绩效达标啦，工资已发,发了1000，老板还剩{company_account}元")
        if company_account <= 0:
            print("老板没钱了，不发工资啦")
            break
    else:
        print(f"员工{x}的绩效未达标，不发工资，下一位！")"""

# 练习案例发工资,方式2
"""company_account = 9000
staff_num = range(1,21)
for x in staff_num:
    import random
    achievements = random.randint(1,10)
    if company_account <= 1000:
        print("老板没钱了，不发工资啦")
        break
    else:
        if achievements < 5:
            print(f"员工{x}的绩效未达标，不发工资，下一位！")
            continue
        company_account -= 1000
        print(f"员工{x}的绩效达标啦，工资已发,发了1000，老板还剩{company_account}元")
"""
"""company_account = 900
staff_num = range(1,21)
for x in staff_num:
    import random
    achievements = random.randint(1,10)
    if achievements < 5:
        print(f"员工{x}的绩效未达标，不发工资，下一位！")
        continue
    if company_account >= 1000:
        company_account -= 1000
        print(f"员工{x}的绩效达标啦，工资已发,发了1000，老板还剩{company_account}元")
    else:
        print("老板没钱了，不发工资啦")
        break
"""

"""#函数
num = 100
def ha():
    num = 200
    print(num)

ha()
print(num)

num = 100
def ha():
    #公国global声明是全局变量
    global num
    num = 200
    print(num)

ha()
print(num)"""

"""
def select_balance():
    #查询余额函数
   # :return:
    print(f"尊贵的{name},您的余额还剩余{money}")

def deposit():
    deposit_num = int(input("请输入您需要存储的金额"))
    global money
    money += deposit_num
    print(f"存款成功，余额还剩{money}")

def withdraw_money():
    withdraw_money_num = int(input("请输入你要取款的金额"))
    global money
    money -= withdraw_money_num
    print(f"取款成功，余额还剩{money}")

def menu():
    print("欢迎来到元元的银行")
    print("输入1，查询余额；输入2，存款；输入3，取款；输入4，退出系统")
    shuru_value = input("请输入")
    if shuru_value =="1":
        select_balance()
        menu()
    elif shuru_value == "2":
        deposit()
        menu()
    elif shuru_value == "3":
        withdraw_money()
        menu()
    else:
        print("未找到指令")
        menu()

money = 5000000
name = input("请输入您的名字")
menu()
"""

"""
money = 5000000
name = None
name = input("请输入你的名字")
def select_balance():

    # 查询余额函数
    # :return:

    print(f"尊贵的{name},您的余额还剩余{money}")

def deposit(deposit_num):

    # 存款函数
    global money
    money += deposit_num
    print(f"存款成功，余额还剩{money}")

def withdraw_money(withdraw_money_num):

   # 取款函数

    global money
    money -= withdraw_money_num
    print(f"取款成功，余额还剩{money}")

def main():
    print("-------元元银行-------")
    print("输入1，查询余额；输入2，存款；输入3，取款；输入4，退出系统")
    return int(input("请输入"))

while True:
    shuru_value = main()
    if shuru_value == 1:
        select_balance()
    elif shuru_value == 2:
        deposit(int(input("请输入存款金额")))
    elif shuru_value == 3:
        withdraw_money(int(input("请输入取款金额")))
    else:
        print("已退出系统")
        break"""
