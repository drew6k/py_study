# 练习1:字符串的常用操作



#1 center(self,width,fillchar=None)，让字符串在中间
# a="hello"
# print(a.center(20,"-"))  #输出：-------hello--------

#2 count(self,sub,start=None,end=None)，计数：这样的值有几个
# b="curry"
# # print(b.count("r",0,4))  #输出：2
# # print(b.count("u"))  #输出：1
# print(b.count("r",0,3))  #输出：1

#3 endswith(self,suffix,start=None,end=None)，判断是否以**结尾
# c="我爱你中国,亲爱的母亲"
# print(c.endswith("亲"))  #输出：true
# print(c.endswith("中国",0,5))  #输出：true
# print(c.endswith("中国",0,6))  #输出：false

#4 startswith(self,prefix,start=None,end=None)，判断是否以**开头
# d="我为你流泪,也为你自豪"
# print(d.startswith("我"))  #输出：true
# print(d.startswith("我为你",0,5))  #输出：true
# print(d.startswith("自豪",0,6))  #输出：false

#5 find（self，sub，start=None，end=None），查找：是否有字样的字符（有则输出该字符索引，没有则输出-1）
# e="五星红旗迎风飘扬"
# print(e.find("风"))  #输出5
# print(e.find("红",0,2))  #输出：-1

#6 isdigit(self)，判断该字符串是不是整数
# f1="我爱学习,我要考100分"
# print(f1.isdigit())  #输出：false
# f2="22"
# print(f2.isdigit())  #输出：true

#7 join（self，iterable),拼接字符串
# g1=["我","爱","你","中","国"]
# print("-".join(g1))  #输出：我-爱-你-中-国

#8 replace（self，old，new，count=None），替换字符，从左往右替换的次数
# h1="123456789"
# print(h1.replace("1","0"))  #输出：023456789
# h2="111222333"
# print(h2.replace("2","4",2))  #输出：111442333

#9 strip（self，char=None）把字符串前后的空格和换行符去掉
# i="  123 \n"
# print(i)  #输出：  123 并且换行
# print(i.strip())  #输出：123

#10 split（self，sep=None，maxsplit=-1），分割：按照分隔符（没有分隔符就是空格）把字符串变成列表，分几次（默认全分）
# j="我爱你 中国 亲爱的 母亲"
# print(j.split())  #输出：['我爱你', '中国', '亲爱的', '母亲']
# print(j.split("爱"))  #输出：['我', '你 中国 亲', '的 母亲']
# print(j.split("爱",1))  #输出：['我', '你 中国 亲爱的 母亲']



# 练习2：列表常用操作



#1 .append("**")追加：把**追加在列表末尾

#2 .insert(一个数,"***")插入：把***插入到索引为那个数的位置

#3 ***.extend(**)合并：把**合并到***内
# a=[1,2,3,4]
# b=[4,3,2,1]
# a.extend(b)
# print(a)  #输出：[1, 2, 3, 4, 4, 3, 2, 1]

#4 [].insert(一个数，[])嵌套：把一个列表[]嵌入到原来列表那个数索引的位置
# c=[1,2,3]
# c.insert(1,["我","爱","你","中","国"])
# print(c)  #输出：[1, ['我', '爱', '你', '中', '国'], 2, 3]
# print(c[1])  #输出：['我', '爱', '你', '中', '国']
# print(c[1][4])  #输出：国

#5 删除操作：del直接删/remove从左到右删除第一个指定的值/pop删除并返回那个值/clear清空

# 6 切片：从列表里面截得一部分,顾首不顾尾
# d=['alex', 'jack', ['makc', '陈xxx'], '⿊黑姑娘']
# print(d[1:3])  #输出：['jack', ['makc', '陈xxx']]
# print(d[:3])  #输出：['alex', 'jack', ['makc', '陈xxx']]，左边从0开始可以省略
# print(d[2:])  #输出：[['makc', '陈xxx'], '⿊黑姑娘']，取最后几个，可以省略右边
# print(d[2:10])  #输出：[['makc', '陈xxx'], '⿊黑姑娘']，取最后几个,也可以超标写
# print(d[-4:])  #输出：['alex', 'jack', ['makc', '陈xxx'], '⿊黑姑娘'],倒着切同样顾首不顾尾，可省略
# print(d[0:4:2])  #输出:['alex', ['makc', '陈xxx']],步长（跳着切），第二个冒号之后是步长多少（默认是1）
# print(d[::3])  #输出：['alex', '⿊黑姑娘'],也可以省略，但明确步长

#7 排序和反转
# e1=[99,108,66,52,2,13,8]
# e1.sort()  #排序
# print(e1)  #输出：[2, 8, 13, 52, 66, 99, 108]，数字从小到大排序
# e2=['alex', 'jack', 'makc','Allen','小黑']
# e2.sort()
# print(e2)  #输出：['Allen', 'alex', 'jack', 'makc', '小黑', '陈xxx']，默认先大写再小写（a-z）在中文
# e1.reverse()  #反转
# print(e1)  #输出：[108, 99, 66, 52, 13, 8, 2]，反转排序

#8 循环列表
# f=['alex', 'jack', 'makc','Allen','小黑',8,108]
# print(f)
# for i in f:
#     print(i)     #输出：# alex
#                         # jack
#                         # makc
#                         # Allen
#                         # 小黑
#                         # 8
#                         # 108
# for j in enumerate(f):  #enumerate（）打印索引
#     print(j)     #输出：# (0, 'alex')这是元组，后续学
#                         # (1, 'jack')
#                         # (2, 'makc')
#                         # (3, 'Allen')
#                         # (4, '小黑')
#                         # (5, 8)
#                         # (6, 108)
#     print(j[0],j[1])     #输出：# 0 alex
#                                 # 1 jack
#                                 # 2 makc
#                                 # 3 Allen
#                                 # 4 小黑
#                                 # 5 8
#                                 # 6 108



# 练习3练习题：列表，班级成绩分组小程序
# stu_list = [['李渊', 82], ['李世民', 7], ['侯君集', 5], ['李靖', 58], ['魏征',41], ['房玄龄', 64], ['杜如晦', 65], ['柴绍', 94], ['程知节', 45], ['尉迟恭', 94],['秦琼', 54], ['⻓长孙⽆无忌', 85], ['李李存恭', 98], ['封德彝', 16], ['段志⽞玄', 44], ['李弘基', 18], ['徐世绩', 86], ['李治', 19], ['武则天', 39], ['太平公主', 57], ['⻙后',76], ['李隆基', 95], ['杨⽟环', 33], ['王勃', 49], ['陈子昂', 91], ['卢照邻', 70],['杨炯', 81], ['王之涣', 82], ['安禄山', 18], ['史思明', 9], ['张巡', 15], ['雷万春', 72], ['李白', 61], ['高力⼠', 58], ['杜甫', 27], ['⽩居易', 5], ['王维', 14],['孟浩然', 32], ['杜牧', 95], ['李商隐', 34], ['郭子仪', 53], ['张易之', 39], ['张昌宗', 61], ['来俊臣', 8], ['杨国忠', 84], ['李林甫', 95], ['高适', 100], ['王昌龄',40], ['孙思邈', 46], ['玄奘', 84], ['鉴真', 90], ['高骈', 85], ['狄仁杰', 62], ['黄巢', 79], ['王仙芝', 16], ['⽂成公主', 13], ['松赞⼲布', 47], ['薛涛', 79], ['鱼玄机', 16], ['贺知章', 20], ['李泌', 17], ['韩愈', 100], ['柳宗元', 88], ['朱温', 55], ['刘仁恭', 6], ['丁会', 26],['李克用', 39], ['李存勖', 11],['葛从周', 25], ['王建', 13], ['刘知远', 95], ['⽯敬瑭', 63], ['郭威', 28], ['柴荣', 50], ['孟昶', 17], ['荆浩', 84], ['刘彟', 18], ['张及之', 45], ['杜宇', 73],['高季兴', 39], ['喻皓', 50], ['历真', 70], ['李茂贞', 6], ['朱友珪', 7], ['朱友贞',11], ['刘守光', 2]]

# grade1=[]
# grade2=[]
# grade3=[]
# grade4=[]
# grade5=[]
# for i in range(-1,54):  #利用循环按照成绩把列表分类提取到不同的列表
#     i+=1
#     j=stu_list[i][1]
#     if j>89:
#         grade1.insert(0,stu_list[i])
#     elif j>79:
#         grade2.insert(0,stu_list[i])
#     elif j>69:
#         grade3.insert(0,stu_list[i])
#     elif j>59:
#         grade4.insert(0,stu_list[i])
#     else:
#         grade5.insert(0,stu_list[i])
# grade1.sort(key=lambda x:x[1],reverse=True)  #排序
# grade2.sort(key=lambda x:x[1],reverse=True)
# grade3.sort(key=lambda x:x[1],reverse=True)
# grade4.sort(key=lambda x:x[1],reverse=True)
# grade5.sort(key=lambda x:x[1],reverse=True)
# new_stu_list=[]
# new_stu_list.insert(0,grade1)  #把各成绩段的列表嵌入到新的总列表
# new_stu_list.insert(1,grade2)
# new_stu_list.insert(2,grade3)
# new_stu_list.insert(3,grade4)
# new_stu_list.insert(4,grade5)
# print(new_stu_list)



# 练习4：字典dict  key：value结构（key必须不可变的数据类型且必须唯一，若一个字典有重复的key，后面的key会把前面的覆盖掉，value可多个可修改可不唯一）

#1 增加操作  :[key]=value
# a={
#     "name":"刘堃",
#     "age":22
# }
# a["school"]="NCHU"  
# print(a)  #输出：{'name': '刘堃', 'age': 22, 'school': 'NCHU'}

#2 删除操作  ：
# b={
#     22:["age1"],
#     27:["age2"],
#     50:["age3"],
#     "name":"刘堃"
# }
# b.pop(22)  #指定删除key并返回
# print(b)  #输出：{27: ['age2'], 50: ['age3'], 'name': '刘堃'}
# del b["name"]  #指定删除key
# print(b)  #输出：{27: ['age2'], 50: ['age3']}
# b.clear()  #清空dict
# print(b)  #输出：{} 

#3 查找操作即取值
# c1 = {
#     "alex": [23, "CEO", 66000],
#     "⿊黑姑娘": [24, "行政", 4000],
#     "佩奇":[26, "讲师", 40000]
# }
# print(c1["alex"])  #取key对应的value，但不能通过value查key
# print("佩奇" in c1)  #判断key在不在字典里
# c2=c1.keys()  #查找字典所有的key并以列表返回
# print(c2)  #输出：dict_keys(['alex', '⿊黑姑娘', '佩奇'])
# c3=c1.values()  #查找所有的value并以列表返回
# print(c3)  #输出：dict_values([[23, 'CEO', 66000], [24, '行政', 4000], [26, '讲师', 40000]])
# c4=c1.items()  #返回一个其中包含所有（key，value）组成的元组的大列表
# print(c4)  #输出：dict_items([('alex', [23, 'CEO', 66000]), ('⿊黑姑娘', [24, '行政', 4000]), ('佩奇', [26, '讲师', 40000])])
# for i,j in c4:  #循环查找，用两个变量一个代表key一个value
#     print(i,j)  #输出： # alex [23, 'CEO', 66000]
#                         # ⿊黑姑娘 [24, '行政', 4000]
#                         # 佩奇 [26, '讲师', 40000]

#4 循环操作
# d={
#     "name":"刘堃",
#     "age":22,
#     "major":"engineering",
# }
# for i1 in d:
#     print(i1)  #输出三个key
# for i2,i3 in d.items():
#     print(i2,i3)  #输出三个对应的key和value
# for i4 in d:
#     print(i4,d[i4])  #输出三个对应的key和value，和上面输出的一样但省去了变为大列表那一步，效率高很多

#5 长度len(),全局的函数可用于列表字符串字典
# e1={
#     1:"a",
#     2:"b",
#     3:"c"
# }
# print(len(e1))  #输出：3也就是有几组key：value
# print(len("James"))  #输出：5也就是字符串的长度
# e2=[2,"KI","LBJ",23]
# print(len(e2))  #输出：4也就是列表的长度

# #6 嵌套
# f={
#     1:"haha",
#     2:"hehe",
#     3:"huhu"
# }
# f[4]={5:"hoho"}
# print(f)  #输出：{1: 'haha', 2: 'hehe', 3: 'huhu', 4: {5: 'hoho'}}
# print(f[4][5])  #输出：hoho，查找嵌套中的字典也一样，多查一层key即可
 


# 练习5练习题：字典练习



#1 生成一个包含100个key的字典，每个value的值不能一样
# a={}
# for i in range(100):
#     i+=1
#     a[i]=i+1
# print(a)

#2 {‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9} 请把这个dict中key大于5的值value打印出来。
# b={"k0":0,"k1":1,"k2":2,"k3":3,"k4":4,"k5":5,"k6":6,"k7":7,"k8":8,"k9":9}
# for i in b:  #i指的是b里面的key
#     if b[i]>5:  #b[i]指的是i这个key所对应的value，用那个数和5比较
#         print(b[i])  #再输出大于5的数

#3 把题2中value是偶数的统一改成-1
# b={"k0":0,"k1":1,"k2":2,"k3":3,"k4":4,"k5":5,"k6":6,"k7":7,"k8":8,"k9":9}
# for i in b:
#     if b[i]%2==0:  #用除以2取余来判断奇偶
#         b[i]=-1  #改成-1
# print(b)  #输出：{'k0': -1, 'k1': 1, 'k2': -1, 'k3': 3, 'k4': -1, 'k5': 5, 'k6': -1, 'k7': 7, 'k8': -1, 'k9': 9}

#4 请设计一个dict, 存储你们公司每个人的信息， 信息包含至少姓名、年龄、电话、职位、工资，并提供一个简单的查找接口，用户按你的要求输入要查找的人，你的程序把查到的信息打印出来
# c_512={
#     "lgy":[35,12345678911,"doctor",100],
#     "dqb":[37,12345678912,"doctor",100],
#     "dw":[28,12345678913,"brother",50],
#     "jjw":[23,12345678914,"brother",50],
#     "mjc":[23,12345678915,"student",20],
#     "lk":[22,12345678916,"student",20],
#     "tjy":[22,12345678917,"student",20],
#     "htq":[22,12345678918,"student",20]
# }
# Inquire=input("please input who do you want to inquire")
# for i in c_512:
#     if i==Inquire:
#         print(i,c_512[i])
