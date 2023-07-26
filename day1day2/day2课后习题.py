# 年会抽奖小程序问题
# import random

# ready1=int(input("are you ready for the first lottery?yes=1,no=0"))
# if ready1==1:
#     print("let us go")
# else:
#     exit("请还没准备好的朋友抓紧时间，咱们马上开始")
# n1=list(range(1,301))
# count1=0
# while count1<30:
#     count1+=1
# n2=random.sample(n1,30)
# print(n2)
# print("恭喜以上号码的朋友,获得三等奖byt一盒")
# i=0
# while i<300:
#     i+=1
#     if i in n2:
#         n1.remove(i)
# print("其他朋友不要灰心，还有两次机会!")

# ready2=int(input("are you ready for the seconde lottery?yes=1,no=0"))
# if ready2==1:
#     print("let us go")
# else:
#     print("请还没准备好的朋友抓紧时间，咱们马上开始")
# count2=0
# while count2<6:
#     count2+=1
# n3=random.sample(n1,6)
# print(n3)
# print("恭喜以上号码的朋友,获得二等奖iPhone14 pro max一台")
# j=0
# while j<270:
#     j+=1
#     if j in n3:
#         n1.remove(j)
# print("其他朋友不要灰心，还有一次终极大奖！")

# ready3=int(input("are you ready for the seconde lottery?yes=1,no=0"))
# if ready3==1:
#     print("let us go")
# else:
#     print("请还没准备好的朋友抓紧时间，咱们马上开始")
# count3=0
# while count3<6:
#     count3+=1
# n3=random.sample(n1,3)
# print(n3)
# exit("恭喜以上号码的朋友,获得一等奖泰国五日游！")