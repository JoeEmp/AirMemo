# 将UI目录下的所有.ui文件转化换为.py文件
import os


def findUI(ulist, dir="./UI",need_suffix='.ui'):
    # 是否存在目录
    if not os.path.exists(dir):
        print("UI director inexistence ")
        exit(-1)
    # 存在目录
    for filename in os.listdir(dir):
        filename = os.path.join(dir, filename)
        if os.path.isfile(filename):
            suffix = os.path.splitext(filename)
            if suffix[1] == need_suffix:
                ulist.append(filename)
        else:
            findUI(ulist, filename)


# windows系统调用此方法 转换成linux目录格式
def dirAlter(clist):
    length = len(clist)
    for i in range(0, length):
        clist[i] = clist[i].replace('\\', '/')


# 执行命令行将 .ui 转换成 .py
def translation(clist):
    for file in clist:
        try:
            os.system("python -m PyQt5.uic.pyuic " + file + " -o " + file[0:-3] + ".py  ")
        except:
            print(str(file) + "translation failed")


if __name__ == "__main__":
    ulist = []
    findUI(ulist)
    # 只转化指定文件
    sub_ulist = ['UI/recycle.ui']
    if not sub_ulist:
        translation(ulist)
    else:
        translation(ulist)
