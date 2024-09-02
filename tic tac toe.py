from random import choice
import time
flag=0

print("tic tac toe _______by ak")
a = input(str("Enter your choice for 'x' or 'o' :-"))
print("ok")
# according to user's sign decide computer's sign
if a!='x' and a!='o':
    print('by default x')
    a='x'
if a=="x":
    print('you choose x')
    m="o"
else:
    print('you choose o')
    m="x"
m1=1
m2=2
m3=3
m4=4
m5=5
m6=6
m7=7
m8=8
m9=9
print(f" {m1} | {m2} | {m3} ")
print("---|---|---")
print(f" {m4} | {m5} | {m6} ")
print("---|---|---")
print(f" {m7} | {m8} | {m9} ")
ama = [1,2,3,4,5,6,7,8,9]
for i in range (1,10,1):
    if i % 2 != 0:
        am = int(input("Click the number for your turn :-"))
        ama.remove(am)
    elif i % 2 == 0:
        if i==2:
            print("computer's turn")
            ak = "---"
            time.sleep(2)
            print(ak)
            time.sleep(1)
            print(ak)
            time.sleep(2)
            print(ak)
            am = choice(ama)
            ama.remove(am)
        else:#for forcefully terminate you
            log1 = []
            log2 = []
            print("computer's turn")
            ak = "---"
            time.sleep(2)
            print(ak)
            time.sleep(1)
            print(ak)
            time.sleep(2)
            print(ak)

            #below eight condtions make sure that computer can win if yes then give that place value
            if (m == m1 or m == m2 or m == m3):
                logic2 = [m1, m2, m3]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m3 or m == m6 or m == m9):
                logic2 = [m3, m6, m9]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m2 or m == m5 or m == m8):
                logic2 = [m2, m5, m8]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m4 or m == m5 or m == m6):
                logic2 = [m4, m5, m6]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m7 or m == m8 or m == m9):
                logic2 = [m7, m8, m9]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m1 or m == m4 or m == m7):
                logic2 = [m1, m4, m7]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m3 or m == m5 or m == m7):
                logic2 = [m3, m5, m7]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2
            if (m == m1 or m == m5 or m == m9):
                logic2 = [m1, m5, m9]
                if logic2.count(m) == 2 and a not in logic2:
                    log2 = log2 + logic2

            #below eight conditions is terminate user forcefully
            if (a == m1 or a == m2 or a == m3):
                logic1 = [m1, m2, m3]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m3 or a == m6 or a == m9):
                logic1 = [m3, m6, m9]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m2 or a == m5 or a == m8):
                logic1 = [m2, m5, m8]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m4 or a == m5 or a == m6):
                logic1 = [m4, m5, m6]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m7 or a == m8 or a == m9):
                logic1 = [m7, m8, m9]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m1 or a == m4 or a == m7):
                logic1 = [m1, m4, m7]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m3 or a == m5 or a == m7):
                logic1 = [m3, m5, m7]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1
            if (a == m1 or a == m5 or a == m9):
                logic1 = [m1, m5, m9]
                if logic1.count(a) == 2 and m not in logic1:
                    log1 = log1 + logic1


            #above 16 conditions made and now check(choose between terminate user or directly win) below conditions to make win computer
            if log1==[] and log2 ==[]: #if this true   #if this false  #if all 16 conditions failed then randomly choose value
                print("random")
                dj = choice(ama)
                log1.append(dj)
                log1.append(a)
                log1.append(a)
            # for removing redundancy
            if log2==[]:# also true    #either terminate user(if high priority) or choose random value
                print("force to terminate you")
                log1.remove(a)
                log1.remove(a)
                for i in range(1, 10, 1):
                    if i == log1[0]:
                        am = i
                i = 2 #neccesary for switching
                log1=[]
                ama.remove(am)
            if log2!=[]: #then this true    #when any condtion can make win computer then high priority
                print("you are out")
                log2.remove(m)
                log2.remove(m)
                for i in range(1, 10, 1):
                    if i == log2[0]:
                        am = i
                i = 2  # neccesary for switching
                log2=[]
                ama.remove(am)

    #below condtions replace above condtions value to x or o
    if i % 2 != 0:  #odd turn for me
        if am == 1:
            m1=a

        if am == 2:
            m2=a

        if am == 3:
            m3=a

        if am == 4:
            m4=a

        if am == 5:
            m5=a

        if am == 6:
            m6=a

        if am == 7:
            m7=a

        if am == 8:
            m8=a

        if am == 9:
            m9=a

    elif i%2==0:  #even for comp.
        if am == 1:
            m1=m

        if am == 2:
            m2=m

        if am == 3:
            m3=m

        if am == 4:
            m4=m

        if am == 5:
            m5=m

        if am == 6:
            m6=m

        if am == 7:
            m7=m

        if am == 8:
            m8=m

        if am == 9:
            m9=m

    #for display structure of tic tac toe with signs
    print(f" {m1} | {m2} | {m3} ")
    print("---|---|---")
    print(f" {m4} | {m5} | {m6} ")
    print("---|---|---")
    print(f" {m7} | {m8} | {m9} ")


    #below condition variable use for check three sign alignment
    dj = ('x' == m1 and 'x' == m2 and 'x' == m3)
    ty = ('x' == m3 and 'x' == m6 and 'x' == m9)
    di = ('x' == m2 and 'x' == m5 and 'x' == m8)
    zs= ('x' == m4 and 'x' == m5 and 'x' == m6)
    kk = ('x' == m7 and 'x' == m8 and 'x' == m9)
    ak = ('x' == m1 and 'x' == m4 and 'x' == m7)
    jk = ('x' == m3 and 'x' == m5 and 'x' == m7)
    op = ('x' == m1 and 'x' == m5 and 'x' == m9)
    dj1 = ('o' == m1 and 'o' == m2 and 'o' == m3)
    ak1 = ('o' == m1 and 'o' == m4 and 'o' == m7)
    jk1 = ('o' == m1 and 'o' == m5 and 'o' == m9)
    op1 = ('o' == m3 and 'o' == m5 and 'o' == m7)
    an1 = ('o' == m4 and 'o' == m5 and 'o' == m6)
    kk1 = ('o' == m7 and 'o' == m8 and 'o' == m9)
    di1 = ('o' == m2 and 'o' == m5 and 'o' == m8)
    ty1 = ('o' == m3 and 'o' == m6 and 'o' == m9)
    #below condtions display if win-loose
    if dj or ak or op or jk or zs or ty or di or kk:
        if a == 'x':
            print("You Win !!!!!!!")
            flag = 1
            break
        else:
            print("You Loose !!!!!")
            flag = 1
            break

    elif dj1 or ak1 or jk1 or op1 or an1 or di1 or kk1 or ty1:
        if a == 'o':
            print("You Win !!!!!!!")
            flag = 1
            break
        else:
            print("You Loose !!!!!")
            flag = 1
            break

#if no win or loose then tie
if flag!=1:
    print("Tie!!!!!!")