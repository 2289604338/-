#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：土木三班赏箫楠
日期：2020/11/21
"""
import random
def name_to_number(name):
    if name=='石头':
        return 0
    elif name=='史波克':
        return 1
    elif name=='纸':
        return 2
    elif name=='蜥蜴':
        return 3
    elif name=='剪刀':
        return 4
    else:
        print('Error: No Correct Name')

def number_to_name(number):
    if number==0:
        return '石头'
    elif number==1:
        return '史波克'
    elif number==2:
        return '纸'
    elif number==3:
        return '蜥蜴'
    elif number==4:
        return '剪刀'

def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print('计算机的选择是：',comp_choice)
    if player_choice_number==0:
        if comp_number==3 or comp_number==4:
            print('您赢了！')
        elif comp_number==player_choice_number:
            print('您和计算机出的一样呢')
        else:
            print('您输了！')
    elif player_choice_number==1:
        if comp_number==0 or comp_number==4:
            print('您赢了！')
        elif comp_number==player_choice_number:
            print('您和计算机出的一样呢')
        else:
            print('您输了！')
    elif player_choice_number==2:
        if comp_number==1 or comp_number==0:
            print('您赢了！')
        elif comp_number==player_choice_number:
            print('您和计算机出的一样呢')
        else:
            print('您输了！')
    elif player_choice_number==3:
        if comp_number==1 or comp_number==2:
            print('您赢了！')
        elif comp_number==player_choice_number:
            print('您和计算机出的一样呢')
        else:
            print('您输了！')
    elif player_choice_number==4:
        if comp_number==2 or comp_number==3:
            print('您赢了！')
        elif comp_number==player_choice_number:
            print('您和计算机出的一样呢')
        else:
            print('您输了！')

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
player_choice=choice_name
rpsls(choice_name)