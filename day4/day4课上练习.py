# 创建文件
# a=open(file="D:\个人\python8天学习\8天练习\文件操作.txt",mode="w")
# a.write("lk 学习 py\n")
# a.write("lk 喜欢 学习")
# a.close()

#只读模式
# a=open(file="D:\个人\python8天学习\8天练习\文件操作.txt",mode="r")
# print(a.readline())
# print("00000000000000000")
# print(a.read())

# 追加模式
# a=open(file="D:\个人\python8天学习\8天练习\文件操作.txt",mode="a")
# a.write("lk like play\n")
# a.write("lk love freedom")
# a.close()

# 循环文件
# f=open("D:\个人\python8天学习\8天练习\day4\联系方式")
# for i in f:  #循环一次读一行
#     j=i.split()  #把字符串变成列表
#     hight=int(j[3])  #把字符串转成数字，以便后续与数字作比较
#     wight=int(j[4])
#     if hight>172 and wight>=50:
#         print(j)
