# 练习一：流程控制单双分支，猜测年龄问题
# age=int(input("please input your age"))
# if age<18:
#     print("you are a juvenile,congratulation!")
# else:
#     print("unfortunately,you are already a adult")



# 练习二：多分支，打印成绩问题
# grade=int(input("please input your grade"))
# if grade>=90:
#     print("A")
# elif grade>=80:
#     print("B")
# elif grade>=60:
#     print("C")
# elif grade>=40:
#     print("D")
# else:
#     print("E")



# 练习三：for嵌套，continue/break，打印楼层信息问题
# for i in range(1,5):
#     print(f"-----第{i}层-----")
#     if i==2:
#             print("stop")
#             continue  #暂停本次循环继续下一次
#     for j in range(1,10):
#         if i==3 and j==6:
#              print("306房间异常，结束三层")
#              break  #结束本次循环继续下一次
#         print(f"L{i}-{i}0{j}室")



# 练习四：for循环，打印三角形问题
# for i in range(10):
#     if i<=5:
#         print("*"*i)
#     else:
#         print("*"*(10-i))



# 练习五：while循环，猜年龄问题
# age2=22
# count=0  #计数器
# while count<3:
#     count+=1
#     guess=int(input("please input your answer"))

#     if guess<22:
#         print("sorry,you are wrong,I am older")
#     elif guess>22:
#         print("sorry,you are wrong,I am younger")
#     else:
#         print("yes,you are right")
#         break 
    
# print("ha ha ha")



# 练习六：while循环，打印乘法表问题
# i=0
# while i<9:
#     i+=1
#     for j in range(1,i+1):  #关键在于让j在1到i之间循环取值
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()



# 练习七：循环，流程控制，random库，string库，选择车牌问题
# answer=int(input("you only have three chance,dou you understand?please input your answer 0=no,1=yes"))
# if answer>0:
#     print("祝你好运!let us go")
# else:
#     exit("欢迎下次再来")
# import random
# import string
# count=0
# while count<3:
#     count+=1
#     car_nums=[]
#     for i in range(20):
#         n1=random.choice(string.ascii_uppercase)
#         n2="".join(random.sample(string.ascii_uppercase+string.digits,5))
#         c_num=f"京{n1}-{n2}"
#         car_nums.append(c_num)
#         print(i+1,c_num)
#     choice=input("please input which is your favorite:").strip()
#     if choice in car_nums:
#         exit(f"恭喜你成功选择{choice}")
#     else:
#         print("您所选择的内容不在所选范围，请重新选择")




