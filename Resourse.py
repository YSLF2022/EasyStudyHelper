#!/usr/bin/python3
# coding=UTF-8
import platform
import sys, os


def Exit(score, Answered_questions, correct_questions, unlocked_tools):
    print("您总共获得了", score, "分积分")
    print("总共解锁了", unlocked_tools, '个工具')
    print("您总共参与了", Answered_questions, "次答题")
    print("共有", correct_questions, "次答题是正确的")
    print("==========================GOODBYE============================")
    sys.exit()


def SaveRecord(score, Answered_questions, correct_questions, unlocked_tools):
    try:
        fw1 = "您总共获得了" + str(score) + "分积分\n"  # 第一行文字
        fw2 = "总共解锁了" + str(unlocked_tools) + '个工具\n'  # 第二行文字
        fw3 = "您总共参与了" + str(Answered_questions) + "次答题\n"  # 第三行
        fw4 = "共有" + str(correct_questions) + "次答题是正确的\n"  # 第四行
        file = open(file="Record.eshf", mode="a")
        file.write(fw1)
        file.write(fw2)
        file.write(fw3)
        file.write(fw4)
        file.write("==============================================")
    except Exception as error:
        print("出现错误：%s" % error)
        print("保存失败！")
    else:
        print("保存成功，文件为本目录下的Record.eshf")
    finally:
        pass


def calc():
    print("输入START开始计算，输入HELP进入帮助模式，输入CHECK_VERSION查看版本，输入QUIT退出")
    command = input("请输入指令：")
    if command == "START":
        del command
        while 1:
            """shuzi1 = int(input("PLEASE TYPE IN THE FIRST NUMBER IN YOUR FORMULA>"))
            _operator_ = input("PLEASE TYPE IN THE OPERATOR>")
            shuzi2 = int(input("PLEASE TYPE IN THE FIRST NUMBER IN YOUR FORMULA>"))
            if _operator_ == "+":
                print("ANSWER = ", shuzi1 + shuzi2)
            elif _operator_ == "-":
                print("ANSWER = ", shuzi1 - shuzi2)
            elif _operator_ == "*":
                print("ANSWER = ", shuzi1 * shuzi2)
            elif _operator_ == "**":
                print("ANSWER =", shuzi1 ** shuzi2)
            elif _operator_ == "/":
                if shuzi2 == 0:
                    print("ERROR! 0x00000002 ZeroDivision")
                else:
                    print("ANSWER = ", shuzi1 / shuzi2)
            elif _operator_ == "//":
                if not shuzi2 == "0":
                    print("ANSWER = ", shuzi1 // shuzi2)
                else:
                    print("ERROR! 0x00000002 ZeroDivision")
            else:
                print("ERROR! 0x00000001 ValueError")"""
            try:
                shuzi1 = float(input("请输入算式中的第一个数："))
                _operator_ = input("请输入运算符：")
                shuzi2 = float(input("请输入算式中的第二个数："))
            except ValueError as error:
                print("本计算器仅支持确切的一个数进行计算，不支持带有字母等字符的数进行计算哦！")
            else:
                if _operator_ == "+":
                    print("答案是", shuzi1 + shuzi2)
                elif _operator_ == "-":
                    print("答案是", shuzi1 - shuzi2)
                elif _operator_ == "*":
                    print("答案是", shuzi1 * shuzi2)
                elif _operator_ == "**":
                    print("答案是", shuzi1 ** shuzi2)
                elif _operator_ == "/":
                    if shuzi2 == 0:
                        print("ERROR! 0x00000002 ZeroDivision")
                    else:
                        print("答案是", shuzi1 / shuzi2)
                elif _operator_ == "//":
                    if not shuzi2 == "0":
                        print("答案是", shuzi1 // shuzi2)
                    else:
                        print("ERROR! 0x00000002 ZeroDivision")
                elif _operator_ == "exit" or _operator_ == "EXIT" or _operator_ == "Exit":
                    print("ヾ(￣▽￣)Bye~Bye~")
                    break
                else:
                    print("ERROR! 0x00000001 OperatorError")
            finally:
                pass

    elif command == "HELP":
        del command
        print("*************************简易计算器帮助文件*************************")
        print("1.运算符")
        print("加法 +")
        print("减法 -")
        print("乘法 *")
        print("除法 /")
        print("整除 //")
        print("幂运算（次方运算） **")
        print("2.退出计算模式")
        print("注意！这会直接退出简易计算器程序，不会回到菜单栏！！！")
        print("方法：在询问运算符时输入exit即可（全大写或首字母大写都能实现退出计算模式）")
    elif command == "CHECK_VERSION":
        del command
        print("版本:1.0.0.810.1405 beta version 3")
    elif command == "QUIT":
        del command
        print("再见")
    else:
        print("ERROR! 0x00000001 CommandError")
