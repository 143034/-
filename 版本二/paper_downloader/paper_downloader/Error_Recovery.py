from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import PATHS
path1 = PATHS.CONFIG_ALL_DIR + r'\Search.txt'
path2 = PATHS.CONFIG_ALL_DIR + r'\Search_Three.txt'
path3 = PATHS.CONFIG_ALL_DIR + r'\settings.ico'
class Error_Recovery():
    def __init__(self,tk):
        self.root = tk
        self.root.title('关键词修复界面')
        self.root.resizable(0, 0)
        self.root.geometry('400x120+800+450')
        self.root.iconbitmap(path3)
        self.Creat_Main_Window()
    def Creat_Main_Window(self):
        def Fix_First():
            path = path1
            content = entry.get()
            print(content)
            ustr = "%s"% str(content)
            with open(path,'w') as f:
                f.write(ustr)
                f.close()

        def Fix_Second():
            path = path2
            content = entry1.get()
            print(content)
            ustr = "%s"% str(content)
            with open(path, 'w') as f:
                f.write(ustr)
                f.close()
        def File_View(paths):
            path = paths
            with open(path,"r") as f:
                ustr = str(f.read())
                f.close()
                return ustr
        def See_Content():
            tkinter.messagebox.showinfo("提示", '前三个爬虫关键词: %s      后三个爬虫关键词: %s'%(File_View(path1),File_View(path2)))
        def Help():
            ustr = '''   关于三大顶会的爬虫,请根据以下提示修改关键字。
                    CVPR:(2013-2019)
                    ICCV:(2013,2015,2017,2019)
                    ECCV:(2018)'''
            tkinter.messagebox.showinfo("提示", ustr)
        entry = Entry(self.root)
        button = Button(self.root, text="修复",command=Fix_First)
        entry1 = Entry(self.root)
        button1 = Button(self.root, text="修复", command=Fix_Second)
        button2 = Button(self.root, text="关键词查看", command=See_Content)
        button3 = Button(self.root, text="修复须知", command=Help)
        label = Label(self.root,text="对前三个爬虫的关键词修复")
        label1 = Label(self.root,text="对三大顶会爬虫关键词修复")
        entry.pack()
        button.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        label.pack()
        label1.pack()
        entry.place(x=0, y=21)
        button.place(x=150, y=19)
        entry1.place(x=0, y=81)
        button1.place(x=150, y=79)
        button2.place(x=280, y=19)
        label.place(x=0, y=0)
        label1.place(x=0, y=60)
        button3.place(x=280, y=79)
        # text.place(x=250, y=19)
        # text1.place(x=250, y=79)
if __name__ == "__main__":
    root = Tk()
    app = Error_Recovery(root)
    root.mainloop()