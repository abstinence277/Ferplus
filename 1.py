#coding=gbk
import os
import sys
def rename():
    path="E:\desktop\Process\Facial-Expression-Recognition.Pytorch-master\FER2013 plus\data2\data\data\Training\Fear"
    name=" "
    startNumber="1"
    fileType=".png"
    print("正在生成以"+name+startNumber+fileType+"迭代的文件名")
    count=0
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        Newdir=os.path.join(path,name+str(count+int(startNumber))+fileType)
        os.rename(Olddir,Newdir)
        count+=1
    print("一共修改了"+str(count)+"个文件")

rename()