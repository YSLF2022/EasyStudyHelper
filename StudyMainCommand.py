#!/usr/bin/python3
# coding=UTF-8
"""
Author:郑一鸣
Version : 0.1 beta 1
Last Update 2022/2/11
"""
import os;
import random     #此处的ReadJsonMod为同目录下的ReadJsonMod.py
import Resourse,CefBlowser
def main():
    Math_Questions = ["小明把他的500元压岁钱,买了五年期的国家建设债券,年利率按3.81％计算.到期时,小明的利息共有多少元?（只写数字）","淘气家投保了”家庭财产保险“,保险金额为15万元,保险期限三年.按年保险费率0.5％计算,共需缴纳保险费多少元?(只写数字)","甲、乙两队学生从相距18km的两地同时出发，相向而行。一个同学骑车以14km/时的速度，在两队之间联络。甲队5km/时，乙队4km/时。两队相遇时，骑车的同学共行多少千米？（答案只写数字）","把630本图书按3?4分给五年级和六年级,六年级分得图书( )本。（只写数字）","一个水库有一定的蓄水量，河水每天又均匀的流入水库，5台抽水机连续抽20天可以抽干：6台同样的抽水机连续15天可以抽干，如果想6天抽干，需要多少台同样的抽水机？"];#数学题库
    Math_Questions_Answers = {"小明把他的500元压岁钱,买了五年期的国家建设债券,年利率按3.81％计算.到期时,小明的利息共有多少元?（只写数字）":"57.15","淘气家投保了”家庭财产保险“,保险金额为15万元,保险期限三年.按年保险费率0.5％计算,共需缴纳保险费多少元?(只写数字)":"2250","把630本图书按3?4分给五年级和六年级,六年级分得图书( )本。（只写数字）":"840","甲、乙两队学生从相距18km的两地同时出发，相向而行。一个同学骑车以14km/时的速度，在两队之间联络。甲队5km/时，乙队4km/时。两队相遇时，骑车的同学共行多少千米？（答案只写数字）":"28","一个水库有一定的蓄水量，河水每天又均匀的流入水库，5台抽水机连续抽20天可以抽干：6台同样的抽水机连续15天可以抽干，如果想6天抽干，需要多少台同样的抽水机？":"12"};#数学题对应的答案
    Chinese_Questions = ["填入恰当的词语：道德高，名望重。 （      ）","补全单词（填整个词）：（ ）冲（ ）撞","露出 (lù  lòu ) lù = 1,lòu = 2","《离骚》的作者是谁？"];#语文题库
    Chinese_Questions_Answers = {"填入恰当的词语：道德高，名望重。 （      ）":"德高望重","补全单词（填整个词）：（ ）冲（ ）撞":"横冲直撞","露出 (lù  lòu ) lù = 1,lòu = 2":"1","《离骚》的作者是谁？":"屈原"};#语文题对应的答案    
    English_Questions = ["( )How heavy are you? I am____________.A. 155cm B. 12 years old C. 38kg ","( )Did your sister ___________ grandparents last Sunday?A. visit B. visits C. visited ","Look, my bag is ___________ ( 更大)than yours. ","country_________（复数）","( ) I want _______ a map of China .A. buy B. is buying C. to buy D. am buying "];#英语题库
    English_Questions_Answers = {"( )How heavy are you? I am____________.A. 155cm B. 12 years old C. 38kg ":"C","( )Did your sister ___________ grandparents last Sunday?A. visit B. visits C. visited ":"A","Look, my bag is ___________ ( 更大)than yours. ":"bigger","country_________（复数）":"countries","( ) I want _______ a map of China .A. buy B. is buying C. to buy D. am buying ":"C"};#英语题对应的答案
    ChengYu = ["窃窃私语是指小声说话","【守株待兔】原比喻希图不经过努力而得到成功的侥幸心理。现也比喻死守狭隘经验，不知变通。","【兔死狗烹】比喻有事时被重用,事成后即被毁弃. ","杯弓蛇影：将映在酒杯里的弓影误认为蛇。比喻因疑神疑鬼而引起恐惧。 ","一鸣惊人:比喻平时没有突出的表现；一下子做出惊人的成绩。"];#成语
    Chengyu_Questions = ["你知道窃窃私语的意思吗？","比喻希图不经过努力而得到成功的侥幸心理。现也比喻死守狭隘经验，不知变通的成语是什么？","兔死狗烹的释义是什么？","比喻因疑神疑鬼而恐惧的是那个成语？","来自俞伯牙、钟子期的故事的成语是哪个？"]#问题（成语）
    Chengyu_Questions_Answers = {"你知道窃窃私语的意思吗？":"小声说话","比喻希图不经过努力而得到成功的侥幸心理。现也比喻死守狭隘经验，不知变通的成语是什么？":"守株待兔","比喻因疑神疑鬼而恐惧的是那个成语？":"杯弓蛇影","比喻故意颠倒黑白，混淆是非的是哪个成语？":"指鹿为马","来自俞伯牙、钟子期的故事的成语是哪个？":"高山流水"}#成语测试的答案
    English_Words = ["ruler n.尺子，统治者","waste v.浪费","compile v.编写，编译"];
    print("|_________________________________________________________________________________________________________________|");
    print("|                                                    学习小助手                                                   |");
    print("|                                                 VERSION 0.1 0b1                                                 |");
    print("|_________________________________________________________________________________________________________________|");
    control = True; #掌控下方的学习loop
    score = 0; #分数
    Answered_questions = 0; #记录总共做过的题数
    correct_questions = 0; #记录总共做对的题数
    unlocked_tools = 0; #记录总共解锁了多少个工具
    usrlock = True;#添加用户
    localgrouplock = True;
    deleteusrlock = True;
    cmdlock = True;#解锁CMD，现用于控制shutdown。
    addadminlock = True;#添加管理员账户
    activeadminlock = True;#激活管理员账户
    translatelock = True;#翻译
    calclock = True;#计算器
    cmdcalclock = True;
    while control:   #学习或游戏的主进程
        print("Chinese=语文学习 Math=数学学习 English=英语学习 Toolkit=系统工具箱 Save = 导出分数 Quit=退出");
        switch_command = input("COMMAND? -->") #判断变量，用于判断进入那种模式
        if switch_command == "Chinese":#语文学习
            while 1:
                Chinese_switch_command = input("成语=成语学习，刷题=做语文例题，返回 = 返回上级菜单，退出 = 退出学习助手>");
                if Chinese_switch_command == "成语":
                    print("===========================成语学习v1.0==============================");
                    while True:
                        CYCtrl = input("学习 = 背成语，测试 = 成语检测，返回 = 返回上级菜单>")
                        if CYCtrl == "学习":
                            while True:
                                CYstudy = random.choice(ChengYu)
                                print(CYstudy)
                                killswitch = input("继续吗？[是/否]");
                                if killswitch == "否":
                                    break;
                        elif CYCtrl == "测试":
                            while True:
                                Answered_questions = Answered_questions + 1;
                                CYQuestion = random.choice(Chengyu_Questions);#问题
                                print(CYQuestion);
                                UserAns = input();
                                if UserAns == Chengyu_Questions_Answers[CYQuestion]:
                                    scoreplus = random.randint(0,10)
                                    print("恭喜你，答对啦！积分+",scoreplus);
                                    score = score + scoreplus;
                                    correct_questions = correct_questions + 1;
                                else: 
                                    print("对不起，答错了。"+ CYQuestion + "的答案是 %s" % Chengyu_Questions_Answers[CYQuestion])
                                killswitch = input("继续测试吗？[是/否]")
                                if killswitch == "否":
                                    break;
                        elif CYCtrl == "返回":
                            break
                    continue;
                if Chinese_switch_command == "刷题":
                    while True:
                        Answered_questions = Answered_questions + 1;
                        CNQuestion = random.choice(Chinese_Questions);#问题
                        print(CNQuestion);
                        UserAns = input();
                        CNshowans = Chinese_Questions_Answers[CNQuestion]
                        if UserAns == Chinese_Questions_Answers[CNQuestion]:
                            scoreplus = random.randint(0,10)
                            print("恭喜你，答对啦！积分+",scoreplus);
                            score = score + scoreplus;
                            correct_questions = correct_questions + 1;
                        else: 
                            print("对不起，答错了。答案是：",CNshowans)
                        killswitch = input("继续测试吗？[是/否]")
                        if killswitch == "否":
                            break;
                    continue;
                if Chinese_switch_command == "返回":
                    break;
                if Chinese_switch_command == "退出":
                    Resourse.Exit(score, Answered_questions, correct_questions, unlocked_tools);
                print("指令错误！")
        elif switch_command == "Math":#数学学习
            while 1:#以此保证不会执行一次就退出
                Maths_switch_command = input("1 = 计算练习，2 = 做数学例题，3 = 返回上级菜单，4 = 退出学习助手>");#判断进入那种模式
                if Maths_switch_command == "1":
                    lianxiSC = input("1 = 加法练习，2 = 减法练习，3.返回>")#
                    if lianxiSC == "1":
                        JFSC = input("1.100以内 2.1000以内 3.自定义>")
                        while 1:
                            if JFSC == "1":
                                a = random.randint(0,100)
                                b = random.randint(0,100)
                            if JFSC == "2":
                                a = random.randint(0, 1000)
                                b = random.randint(0, 1000)
                            if JFSC == "3":
                                try:
                                    max_num = float(input("请输入加数的最大值："))
                                    min_num = float(input("请输入加数的最小值："))
                                except ValueError as error:
                                    print("最大值或最小值请输入纯数字！")
                                    continue
                                else:
                                    if max_num <= min_num:
                                        print("ERROR:最大值小于等于最小值！")
                                        continue
                                    a = random.randint(min_num, max_num)
                                    b = random.randint(min_num, max_num)
                            ans = a + b;
                            print("算式为",a,"+",b)
                            try:
                                c = int(input("ANSWER?>"))
                            except ValueError as error:
                                print("答案请输入纯数字！")
                                continue
                            finally:
                                pass
                            if c == ans:
                                 sp = random.randint(0,5)
                                 print("恭喜您，答对了！积分+",sp);
                                 score = score + sp
                            else:print("对不起，答错了，答案是：",ans);
                            killswitch = input("Continue?(y/n)>")
                            if killswitch == "y":
                                 break;
                    elif lianxiSC == "2":
                        JFSC = input("1.100以内 2.1000以内 3.自定义>")
                        while 1:
                            if JFSC == "1":
                                a = random.randint(0,100)
                                b = random.randint(0,100)
                            elif JFSC == "2":
                                a = random.randint(0, 1000)
                                b = random.randint(0, 1000)
                            elif JFSC == "3":
                                while True:
                                    try:
                                        max_bjs = float(input("请输入被减数的最大值："))
                                        min_bjs = float(input("请输入被减数的最小值："))
                                        max_js = float(input("请输入减数的最大值:"))
                                        min_js = float(input("请输入减数的最小值:"))
                                    except Exception as err:
                                        print("[ERROR]最大值与最小值仅可为纯数字")
                                        print("%s" % err)
                                    else:
                                        if max_bjs <= min_bjs:
                                            print("ERROR:最大值小于等于最小值！")
                                            continue
                                        a = random.randint(min_bjs, max_bjs)
                                        if max_bjs <= min_bjs:
                                            print("ERROR:最大值小于等于最小值！")
                                            continue
                                        b = random.randint(min_js, max_js)
                                    break
                            ans = a - b;
                            print("算式为",a,"-",b)
                            try:
                                c = float(input("ANSWER?>"))
                            except ValueError as error:
                                print("[ERROR]请输入一个数字作为答案！")
                            if c == ans:
                                sp = random.randint(0,5)
                                print("恭喜您，答对了！积分+",sp);
                                score = score + sp
                            else:print("对不起，答错了，答案是：",ans);
                            killswitch = input("继续练习吗?(是/否)>")
                            if killswitch == "否":
                                break;
                    continue;
                if Maths_switch_command == "2":
                    while True:
                        Answered_questions = Answered_questions + 1;
                        MathQuestion = random.choice(Math_Questions);#问题
                        print(MathQuestion);
                        UserAns = input();
                        if UserAns == Math_Questions_Answers[MathQuestion]:
                            scoreplus = random.randint(0,10)
                            print("恭喜你，答对啦！积分+",scoreplus);
                            score = score + scoreplus;
                            correct_questions = correct_questions + 1;
                        else: 
                            print("对不起，答错了。"+ MathQuestion + "的答案是 %s" % Math_Questions_Answers[MathQuestion])
                        killswitch = input("继续测试吗？[是/否]")
                        if killswitch == "否":
                            break;
                    continue;
                if Maths_switch_command == "3":
                    break;
                if Maths_switch_command == "4":
                    Resourse.Exit(score, Answered_questions, correct_questions, unlocked_tools);
                print("指令错误！")
        elif switch_command == "English":
            while True:
                EngSwitch = input("Words = 英语单词练习，Exam = 做英语练习题，Menu=返回主菜单，Quit = 退出学习小助手");
                if EngSwitch == "Words":
                    while True:
                        Wordstudy = random.choice(English_Words)
                        print(Wordstudy)
                        killswitch = input("继续吗？[是/否]");
                        if killswitch == "否":
                                break;
                        continue;
                if EngSwitch == "Exam":
                    while True:
                        Answered_questions = Answered_questions + 1;
                        EngQuestion = random.choice(English_Questions);#问题
                        showans = English_Questions_Answers[EngQuestion]
                        print(EngQuestion);
                        UserAns = input();
                        if UserAns == English_Questions_Answers[EngQuestion]:
                            scoreplus = random.randint(0,10)
                            print("恭喜你，答对啦！积分+",scoreplus);
                            score = score + scoreplus;
                            correct_questions = correct_questions + 1;
                        else: 
                            print("对不起，答错了。答案是：",showans)
                        killswitch = input("继续测试吗？[是/否]")
                        if killswitch == "否":
                            break;
                elif EngSwitch == "Menu":
                    break;
                elif EngSwitch == "Quit":
                    exit();
        elif switch_command == "Toolkit":
            xt = input("您使用的系统是什么？1=Windows 2=Linux")
            if xt == "1":
                while True:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~学习小助手系统工具箱Windows版~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("警告！本工具箱中几乎所有的功能均需管理员权限！")
                    print("您的账户中有", score, "分积分")
                    while True:
                        if score >= 500:
                            switch = input("1=启动计算器（不要管理员权限）[免费] 2=在线翻译（不要管理员权限）[15积分]3=添加用户[30积分] 4=定时关机/重启（不要管理员权限）[35积分]  5=删除用户[50积分] 6=添加管理员账户[70积分] 7=激活管理员账户[100积分] 8=退出工具箱 9=退出学习小助手 CEF3 = 启动CefPython3浏览器")
                        else:
                            switch = input("1=启动计算器（不要管理员权限）[免费] 2=在线翻译（不要管理员权限）[15积分]3=添加用户[30积分] 4=定时关机/重启（不要管理员权限）[35积分]  5=删除用户[50积分] 6=添加管理员账户[70积分] 7=激活管理员账户[100积分] 8=退出工具箱 9=退出学习小助手")
                        if switch == "2":
                            if not translatelock:
                                URL = input("Baidu = 百度翻译，Youdao = 有道翻译，Qihoo = 360翻译")
                                CefBlowser.translate(URL)
                            else:
                                _1switch = input("该功能暂未被解锁，是否花费15积分解锁？[是/否]")
                                if _1switch == "是":
                                    if score >= 15:
                                        score = score - 15
                                        translatelock = False
                                        unlocked_tools = unlocked_tools + 1
                                        print("购买成功！")
                        if switch == "1":
                            if not calclock:
                                os.system("calc")
                            else:
                                _2switch = input("该功能暂未被解锁，是否免费解锁？[是/否]")
                                if _2switch == "是":
                                    if score >= 0:
                                        score = score - 0
                                        calclock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                else:
                                        print("积分不足！")
                            continue
                        elif switch == "3":
                            if not usrlock:
                                username = input("请输入你想添加的用户的用户名：")
                                password = input("请输入你想添加的用户的密码：")
                                command = "NET USER "+username+" "+password+" /add"
                                os.system(command)
                            else:
                                _3switch = input("该功能暂未被解锁，是否花费30积分解锁？[是/否]")
                                if _3switch == "是":
                                    if score >= 30:
                                        score = score - 30
                                        usrlock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                                continue
                            if switch == "4":
                                if not cmdlock:
                                    sdlock = input("s = 关机，r = 重启，a = q = 退出>")
                                    if sdlock == "s":
                                        time = input("多少秒后关机？（只写数字）")
                                        command = "SHUTDOWN -S -T " + time;
                                        os.system(command);
                                    elif sdlock == "r":
                                        time = input("多少秒后重启？（只写数字）")
                                        command = "SHUTDOWN -R -T " + time;
                                        os.system(command);
                                    elif sdlock == "a":
                                        os.system("SHUTDOWN -A");
                                    elif sdlock == "q":
                                        break;
                                    else:
                                        print("指令错误！")
                            else:
                                _4switch = input("该功能暂未被解锁，是否花费35积分解锁？[是/否]")
                                if _4switch == "是":
                                    if score >= 35:
                                        score = score - 35
                                        translatelock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                            if switch == "5":
                                if not deleteusrlock:
                                    deleteuser = input("请输入你想删除的用户的用户名：")
                                    command = "NET USER " + deleteuser + "/DELETE"
                                    os.system(command)
                                else:
                                    _4switch = input("该功能暂未被解锁，是否花费50积分解锁？[是/否]")
                                    if _4switch == "是":
                                        if score >= 50:
                                            score = score - 50
                                        deleteusrlock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                                continue
                            if switch == "6":
                                if not addadminlock:
                                    username = input("请输入你想添加的用户的用户名：")
                                    password = input("请输入你想添加的用户的密码：")
                                    command = "NET USER "+username+" "+password+" /add"
                                    addadmin = "NET LOCALGROUP Administrators "+username+" /add"
                                    os.system(command)
                                    os.system(addadmin)
                            else:
                                _4switch = input("该功能暂未被解锁，是否花费70积分解锁？[是/否]")
                                if _4switch == "是":
                                    if score >= 70:
                                        score = score - 70
                                        addadminlock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                else:
                                    print("积分不足！")
                                continue
                            if switch == "7":
                                if not activeadminlock:
                                    os.system("NET USER Administrator /active:yes")
                            else:
                                _4switch = input("该功能暂未被解锁，是否花费100积分解锁？[是/否]")
                                if _4switch == "是":
                                    if score >= 100:
                                        score = score - 100
                                        activeadminlock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                                continue
                            if switch == "8":
                                break
                            if switch == "9":
                                exit()
                            if switch == "CEF3":
                                URL == "BlowerMode";
                                CefBlowser.translate(URL)
            elif xt == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~学习小助手系统工具箱LINUX版~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("您的账户中有", score, "分积分")
                while True:
                    if score >= 500:
                        switch = input("1=在线翻译[15积分] 2=命令行计算器[20积分] 3=添加用户[30积分] 4=添加用户组[35积分] 5=退出工具箱 6=退出学习小助手 CEF3=启动CEF浏览器")
                    else:
                        switch = input(
                            "1=在线翻译[15积分] 2=命令行计算器[20积分] 3=添加用户[30积分] 4=添加用户组[35积分] 5=退出工具箱 6=退出学习小助手")
                        if switch == "1":
                            if not translatelock:
                                    URL = input("Baidu = 百度翻译 Youdao = 有道翻译 Qihoo = 360翻译")
                                    CefBlowser.translate(URL)
                            else:
                                _1switch = input("该功能暂未被解锁，是否花费15积分解锁？[是/否]")
                                if _1switch == "是":
                                   if score >= 15:
                                        score = score - 15
                                        translatelock = False
                                        unlocked_tools = unlocked_tools + 1
                                        print("购买成功！")
                        if switch == "2":
                            if not cmdcalclock:
                                Resourse.calc()
                            else:
                                _2switch = input("该功能暂未被解锁，是否花费30积分解锁？[是/否]")
                                if _2switch == "是":
                                    if score >= 20:
                                        score = score - 20
                                        cmdcalclock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                        if switch == "3":
                            if not usrlock:
                                username = input("请输入你想添加的用户的用户名：")
                                password = input("请输入你想添加的用户的密码：")
                                adduser = "sudo adduser "+username
                                addpasswd = "sudo passwd "+username+password
                                os.system(adduser)
                                os.system(addpasswd)
                            else:
                                _3switch = input("该功能暂未被解锁，是否花费30积分解锁？[是/否]")
                                if _3switch == "是":
                                    if score >= 30:
                                        score = score - 30
                                        usrlock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                            continue
                        if switch == "4":
                            if not localgrouplock:
                                username = input("请输入你想添加的工作组的名字：")
                                command = "groupadd"+username
                                os.system(command)
                            else:
                                _4switch = input("该功能暂未被解锁，是否花费35积分解锁？[是/否]")
                                if _4switch == "是":
                                    if score >= 35:
                                        score = score - 35
                                        translatelock = False
                                        print("购买成功！")
                                        unlocked_tools = unlocked_tools + 1
                                    else:
                                        print("积分不足！")
                        if switch == "5":
                            break
                        if switch == "6":
                                Resourse.Exit(score, Answered_questions, correct_questions, unlocked_tools);
                        if switch == "CEF3":
                            URL == "BlowerMode";
                            CefBlowser.translate(URL)
        elif switch_command == "Save":
            Resourse.SaveRecord(score, Answered_questions, correct_questions, unlocked_tools);
        elif switch_command == "Quit":
            Resourse.Exit(score, Answered_questions, correct_questions, unlocked_tools);
        else:
            print("指令错误！")
if __name__ == "__main__":
    main()
