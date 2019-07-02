# 将UI目录下的所有.ui文件转化换为.py文件
import os

def findUI(ulist, dir="./ui", need_suffix='.ui'):
    '''
    查找 .ui 文件
    :param ulist: 存储文件
    :param dir: 查找目录
    :param need_suffix: 查找文件后缀
    :return:
    '''
    # 是否存在目录
    if not os.path.exists(dir):
        print("ui director inexistence ")
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
def translation(clist, tag_dir='./py_'):
    '''
    调用uic，转ui变为py
    :param clist: 需要转化的.ui文件
    :param tag_dir: .py文件的目标路径
    :return:
    '''
    for file in clist:
        try:
            # window
            # os.system("python -m PyQt5.uic.pyuic " + file + " -o " + tag_dir + file[0:-3] + ".py  ")
            # mac
            os.system(os.popen('which pyuic5').read()[:-1] +' '+ file + " -o " + tag_dir + file[0:-3] + ".py  ")
        except Exception as e:
            print(str(file) + "translation failed")
            print(e)

if __name__ == "__main__":
    ulist = []
    findUI(ulist)
    # 只转化指定文件
    sub_ulist = ['UI/settings.ui']
    if sub_ulist:
        translation(sub_ulist)
    else:
        translation(ulist)
