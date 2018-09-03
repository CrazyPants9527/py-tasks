import random

# 返回一个元素0-9，随机且不重复，长度为4的list
def random_number():
    numbers = []
    temp_list = []
    while True:
        temp_list.append(random.randint(0,9))
        numbers = list(set(temp_list))
        if len(numbers) == 4:
            return numbers


# 不改变原来list元素顺序情况下去除重复元素
def unlike(before_list):
    if isinstance(before_list,list):
        list2 = list((set(before_list)))
        list2.sort(key = before_list.index)
        return list2
    else:
        return "数据类型不是list"

# 输入一串字符，如果该字符是4个不一样的正整数，如0123，则返回list = [0, 1, 2, 3]
#  否则一直返回该函数 
def myinput():
    print("输入4个不同的数字")
    nums = input(">")

    # 保证输入为整数
    try:
        int_nums = int(nums)
    except ValueError as e:
        print("输入的不是整数！")
        return myinput()

    # 将输入的数迭代成元素为int型，可能有重复元素的temp_list
    temp_num = int(nums)
    if temp_num < 10000 and temp_num > 99:
        a = temp_num//1000
        b = temp_num//100-a*10
        c = temp_num//10-a*100-b*10
        d = temp_num % 10
        temp_list = [a,b,c,d]  
    else:
        print("你输入的数字不是4个数！")
        return myinput()

    
    list2 = unlike(temp_list) # 排除相同元素后的list2

    # 排除相同元素后的list2是否为4位数
    if len(list2) == 4:
        return list2
    else:
        print("不一样的数字得有4个才能玩")
        return myinput()

# 和猜的数字对比
def comparison(list1,list2):
    a = 0 # 多少个数字位置，大小相同
    b = 0 # 多少个数字大小相同，位置不同
    if list1 == list2:
        return "猜对了！"
    else:
        for i in range(4):
            for j in range(4):
                if list1[i] == list2[j] and i == j:
                    a = a + 1
                elif list1[i] == list2[j] and i != j:
                    b = b + 1
        return a, "A", b, "B"

# 主方法
list1 = random_number()
while True:
    list2 = myinput()
    print("你的正确率是-->：",comparison(list1,list2))
    if comparison(list1,list2) == "猜对了！":
        break


