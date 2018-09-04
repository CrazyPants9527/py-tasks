import random
from sys import exit
# 不改变原来list元素顺序情况下去除重复元素
def unlike(before_list):
    if isinstance(before_list,list):
        list2 = list((set(before_list)))
        list2.sort(key = before_list.index)
        return list2
    else:
        return "数类型不是list"

# 输入一串字符，如果该字符是4个不一样的正整数，如0123，则返回list = [0, 1, 2, 3]
#  否则一直返回该函数 
def myinput():
    print("输入4个不同的数字")
    while True:
        temp = input(">")
        try:
            num = int(temp)
            if num < 10000 and num > 99:
                a = num//1000
                b = num//100-a*10
                c = num//10-a*100-b*10                    
                d = num % 10
                list2 = unlike([a, b, c, d])
                if len(list2) == 4:
                    return list2
                else:                        
                    print("不一样的数字得有4个才能玩")
        except:
                print("输入的不是整数！")

# 和猜的数字对比
def comparison(list1):
    while True:
        a = 0 # 多少个数字位置，大小相同
        b = 0 # 多少个数字大小相同，位置不同
        list2 = myinput()
        if list1 == list2:
            print("猜对了！")
            exit(0)
        else:
            for i in list1:
                if i in list2 and list1.index(i) == list2.index(i):
                    a = a + 1
                if i in list2 and list1.index(i) != list2.index(i):
                    b = b + 1
            print(a, "A", b, "B")
            comparison(list1)
        


# 主方法
list1 = random.sample(range(0,9),4) # 返回一个元素0-9，随机且不重复，长度为4的list
comparison(list1)
