import os
import string
#帮助：
#readini()为读取文档配置
#addini为添加工具配置
#需要传入参数 工具名称 工具路径 (绝对路径如:C:\user\a.exe)
#

def readini() :
    f = open("config.ini",mode="r",encoding="gbk")      #打开文件
    list1 = f.readlines()                               #读文件
    for i in range(0, len(list1)):                      #去除\n
        list1[i] = list1[i].strip('\n')
    f.close
    
    list_number = len(list1)    #获取文本数量
    
    

    if list_number == 0 :
        print("你还未进行初始化") 
        print("请输入你要初始化工具名称")
        tool_name = input("")
        print("请输入你要运行的工具的绝对路径")
        tool_path = input("")
        addini(tool_name,tool_path)
        return 1 
    
    j = 0
    while j < list_number :
        print(list1[j])
        j = j+2
        
    print("输入add进行工具添加")
    choose = input("")
    choose_number = choose
    choose_number = int(choose_number)
    choose_str = string(choose)
    syslist = choose_number*2 - 1

    if choose_str == 'add' :
        print("请输入你要添加的工具名称")
        tool_name = input("")
        print("请输入你要运行的工具的绝对路径")
        tool_path = input("")
        addini(tool_name,tool_path)

    os.system(list1[syslist])

def addini(name,path) :
    name = name + "\n"
    path = path + "\n"
    fadd = open("config.ini",mode="a",encoding="gbk")
    fadd.write(name)
    fadd.write(path)
    fadd.close
    return 0

if __name__ == '__main__' :
    readini()
    

