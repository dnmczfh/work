##-*- coding: utf-8 -*-
import os

print("欢迎大家跟我一起学Python")


system = os.name  # 获取系统的类型
if (system == "nt"):
    print("您使用的操作系统是windows")
    print("使用windows表示的特定路径分割符是 " + os.sep)  # 获取系统的分隔符
    print("您的电脑系统的终止符效果" + os.linesep)  # 获取系统换行符
else:
    print("您使用的操作系统是Linux")
    print("使用windows表示的特定路径分割符是 " + os.sep)
    print("您的电脑系统的终止符是" + os.linesep)

path = os.getcwd()  # 获得当前目录
print("您运行本程序所在目录是 " + path)

print("你电脑的Path环境变量为 " + os.getenv("Path"))  # 获取环境变量的值os.putenv(key,value)可以设置环境变量的值

print("你当前文件夹中的文件有：")
print(os.listdir(path))  # 获取文件夹中的所有文件
if (os.path.exists("test.txt")):  # 判断文件是否存在
    os.remove("test.txt")  # 删除指定文件
    print("删除成功")
else:
    print("文件不存在")

print("咱们来删除一个文件，删除后的结果：")
print(os.listdir(path))

print("查看您的ip：",end = '')
print(os.system("ipconfig"))  # 执行系统命令

filepath1 = r"H:\python\project"
filepath2 = r"H:\python\project\learn_os.py"

if (os.path.isfile(filepath2)):  # 判断是不是文件
    print(filepath2 + "是一个文件")
if (os.path.isfile(filepath1)):
    print(filepath1 + "是一个文件")
else:
    print(filepath1 + "不是一个文件")

name = "learn_os.py";
print("本程序的大小为")
print(os.path.getsize(name))  # 获取文件大小
name = os.path.abspath(name)  # 获取文件的绝对路径
print("本程序的绝对路径是" + name)

print("本程序的路径的文件名分别为：")

print(os.path.split(name))  # 将文件名和路径分开

files = os.path.splitext(name)  # 将文件名和扩展分开
print("本程序的扩展为" + files[1])

print("本程序的文件名为" + os.path.basename(name)) # 获取文件的名字

print("本程序的路径为" + os.path.dirname(name))  # 获取文件的路径