# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 9:48
# @Author  : GuYi
# @Function    :


'''

描述
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。
满意度是指所购买的每件物品的价格与重要度的乘积的总和，假设设第ii件物品的价格为v[i]v[i]，重要度为w[i]w[i]，共选中了kk件物品，编号依次为j_1,j_2,...,j_kj


输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q

（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）

输出描述：
输出一个正整数，为张强可以获得的最大的满意度。

1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0

60 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0

50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0

50 5
20 3 5
20 3 5
20 1 0
20 2 0
20 3 0


'''


# cal the satisfaction of the main goods
def cal_satisfaction(price, weight):
    satisfaction = [price, price * weight]
    return satisfaction


# cal the main and accessory
def cal(key, value, accessory):
    prices, weight = [], []
    prices.append(value[0])
    weight.append(value[1])
    if key in accessory:
        # main1 + accessory1
        prices.append(prices[0] + accessory[key][0][0])
        weight.append(weight[0] + accessory[key][0][1])
        # one main + two accessories
        if len(accessory[key]) == 2:
            # main1 + accessory25
            prices.append(prices[0] + accessory[key][1][0])
            weight.append(weight[0] + accessory[key][1][1])
            # main1 + accessory 1 + accessory2
            prices.append(prices[0] + accessory[key][1][0] + accessory[key][0][0])
            weight.append(weight[0] + accessory[key][1][1] + accessory[key][0][1])
    return prices, weight


money, n = map(int, input().split(" "))
main_item, accessory_item, list_ = {}, {}, [0] * (money + 1)
for i in range(n):
    x, y, z = map(int, input().split(" "))
    # satisfaction
    satisfaction = cal_satisfaction(x, y)
    if z == 0:
        main_item[i + 1] = satisfaction
    else:
        if z in accessory_item:
            accessory_item[z].append(satisfaction)
        else:
            accessory_item[z] = [satisfaction]
# get the max
for key, value in main_item.items():
    prices, weight = cal(key, value, accessory_item)
    for j in range(money, -1, -10):  # the price of the item is an integral multiple of 10
        # main prices
        for k in range(len(prices)):
            # if money - pricej
            if j - prices[k] >= 0:
                # record the max
                print(j)
                print(j-prices[k])
                # print(list_[j - prices[k]] + weight[k])
                list_[j] = max(list_[j], list_[j - prices[k]] + weight[k])
                print(list_)
                print('-'*100)
                # list[50] = max(0,20) list[50-10]+20
                # 30,
# print(list_)
print(list_[money])
print(list_)
print(len(list_))
'''
嗯；大概理解了；博主的代码；list[j]记录着Money=j的最优解，通过max比较——当前j的最优解与j减去prices的金额所占用的
1. 最外层循环 main中的item
2. 第二层循环通过Money数 -10 的步长，得到当前money的最优数
3. 第三层循环在“当前的money内”，如果不超钱，去比较当前money的最优数及 （当前的钱-能继续购买的物品的钱）所在的最优数+
'''
