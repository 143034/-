import os
def Sele(obj):
    obj = obj
    files = os.listdir(obj)
    # print (max(files))
    return max(files)

