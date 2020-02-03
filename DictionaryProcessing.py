# -*- coding:utf-8 -*-

import os
from collections import Counter
import sys
#读入当前目录下的字典（txt）---check
#合并目录下所有字典----check
#去重----check
#频率排行----check
#选择功能--获取要提取的前N条----check
#对提取前N条时产生的频率相同，由于提取的数目原因导致没提取到的内容进行一并提取
#Version:1.0
#by:reboot

#获取目标文件夹的路径
filedir = os.path.abspath('.') # 获取当前目录
filenames = os.listdir(filedir)
fname = open(filedir + '\\' + 'all_in_one.txt',"wb")

def MergeTxt():   #合并所有txt文件
    pyname = sys.argv[0].split("/")[-1]
    filenames.remove(pyname) #提前将脚本文件的名字从列表中移除，省去后面的比较过程。
    #############合并文件
    for filename in filenames:
        file = open(filedir+'\\{0}'.format(filename), "rb")  # 打开列表中的文件,读取文件内容
        fname.write(file.read())  # 写入新建的文件中
        file.close()  # 关闭列表文件
    fname.close()


def top_dict(all_in_one,all_in_one_length): #提取TOP字典  # 参数1：未去重的所有内容组成的列表  2：列表长度
    top = input("请输入要生成排行前几的字典：\n")
    if top.isdigit() and int(top) <= all_in_one_length:  # 判断top是否是纯数字
        counts = Counter(all_in_one)
        data = counts.most_common(int(top))

        result = open(filedir + '\\' + 'Top' + top +'字典.txt',"wb")
        for i in data:
            result.write(list(i)[0])
        result.close()


def data_deduplication():  #合并的基础上对数据进行去重
    file_deduplication = open(filedir + '\\' + 'all_in_one_deduplication.txt', "wb")
    fname_set = open(filedir + '\\' + 'all_in_one.txt',"rb").readlines()
    set_out = list(set(fname_set)) #文本内容每一行组成的无重复列表
    set_out_length = len(set_out)
    for i in set_out:
        file_deduplication.write(i)
    file_deduplication.close()
    print("已完成对字典的去重操作。\n")

    #进行排序，提取前几的字典
    fname_set_length = len(list(fname_set))
    top_dict(fname_set,fname_set_length)


if __name__ == '__main__':
    MergeTxt()
    print('已完成字典合并，文件名：all_in_one.txt\n')
    data_deduplication()  #进行去重
    input('按回车退出...')