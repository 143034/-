from tkinter import *
from tkinter.ttk import *
from tk_run import Run_tk,Run_tk_search
from tkinter import ttk
import tkinter,time
import tkinter.messagebox
import pymysql
import Management
import PATHS
import RunSpider
import frozen_dir
from Error_Recovery import Error_Recovery
import paper_downloader.settings as setting
path_ico = PATHS.CONFIG_ALL_DIR + r'\diabo4.ico'
class My_tk():
    def __init__(self,tk=Tk()):
        self.root=tk
        self.root.title('管理界面')
        self.root.resizable(0, 0)
        self.root.geometry('1300x400+300+200')
        self.root.iconbitmap(path_ico)
        self.Creat_Main_Menu()
        self.root.mainloop()

#-------------------------------------起始位置-------------------------------
#开始问候语
    '''
    在程序的开始后在屏幕中心显示
    '''
    def Start_Hello(self):
        label = tkinter.Label(self.root,
                      text="欢迎使用！",
                      bg="black",
                      fg="white",
                      font=("宋体", 15),
                      width=89,
                      height=11,
                      wraplength=200,
                      justify="left",
                      anchor="center")


        label.pack()
        label.place(x=220, y=0)



#主程序
    '''
    设计功能选项卡,绑定事件.是程序的主程序
    '''
    def Creat_Main_Menu(self):
        self.Mysql_Show_Data('init')
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        menu1 = Menu(menubar, tearoff=False)

        for item in ['关于作者','刷新界面','关键词修复','退出']:
            if item == '关于作者':

                menu1.add_command(label=item, command=self.Author_About)

            elif item == '刷新界面':

                menu1.add_separator()
                menu1.add_command(label=item, command=My_tk)

            elif item == '关键词修复':

                menu1.add_separator()
                menu1.add_command(label=item, command=self.Fix)

            else:

                menu1.add_separator()
                menu1.add_command(label=item, command=self.root.quit)

                

        menubar.add_cascade(label='设置',menu=menu1)
        # menubar.add_command()

        menu2 = Menu(menubar, tearoff=False)  
        for i in ['论文爬虫','顶会爬虫','爬取结果展示'] :
            if i == '论文爬虫':

                menu2.add_command(label=i,command=self.Choose_First)

            elif i == '顶会爬虫':

                menu2.add_separator()
                menu2.add_command(label=i,command=self.Choose_Second)

            else:
                
                menu2.add_separator()
                menu2.add_command(label=i,command=self.Show_Date)
                
        menubar.add_cascade(label='爬虫',menu=menu2)
        menu3 = Menu(menubar, tearoff=False)

        for item in ['搜索']:
            if item == '搜索':
                menu3.add_command(label=item,command=self.Search_Mysql)
        menubar.add_cascade(label='搜索',menu=menu3)
        menu4 = Menu(menubar, tearoff=False)
        for item in ['特别注意','帮助']:
            if item == '特别注意':
                menu4.add_command(label=item, command=self.Text_Warning)
            else:
                menu4.add_separator()
                menu4.add_command(label=item,command=self.Help)
        menubar.add_cascade(label='帮助',menu=menu4)
        menu5 = Menu(menubar, tearoff=False)
        menu5.add_command(label='本地下载地址', command=self.Path_Detail)
        menubar.add_cascade(label='下载地址', menu=menu5)
        self.Search_Key_First()
        self.Search_Key_Second()
        self.Txt_Show(0,5)
        self.Start_Hello()
        self.Author_About()



#数据库读取操作
    '''
    输入特殊键,对数据库进行增删改查操作
    '''
    def Mysql_Show_Data(self,key):
        db = pymysql.connect(  
            host=setting.MYSQL_HOST,
            port=setting.MYSQL_PORT,
            user=setting.MYSQL_USER,
            passwd=setting.MYSQL_PASSWORD,
            db=setting.MYSQL_DATABASE,
            )
        cursor = db.cursor()
        key = key
        if key == "*":
            sql = "select * from papers"
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        elif key == "xxx":
            sql= "delete from papers"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                # 如果提交失败，回滚到上一次数据
                db.rollback()
        elif key == 'init':
            sql = "insert into papers values('网络论文下载器','xxx','xxx','xxx','xxx','欢迎使用!','xxx','xxx','xxx','xxx')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                # 如果提交失败，回滚到上一次数据
                db.rollback()
        else:
            sql = "delete from papers where search = '%s'" %(key)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                # 如果提交失败，回滚到上一次数据
                db.rollback()

        cursor.close()
        db.close()




#关于作者
    '''
    作者简介,在设置选项卡中
    '''
    def Author_About(self):
        text = Text(self.root, width=30, height=8)
        text.pack()
        text.place(x=0, y=0)
        str = '''If you want to communicate with me, please add my qq or leave a message on github.
QQ:1430349989
github:https://github.com/143034/scrapy_paper.git
        '''
        text.insert(tkinter.INSERT,str)


    def Fix(self):
        Error_Recovery(Tk())



#前三个爬虫开始运行的地方
    '''
    调用函数启动相关的爬虫
    '''
    def Choose_First(self):
        lbv = StringVar()
        lb = Listbox(self.root, selectmode=SINGLE, height=6, width=30 , listvariable=lbv)
        lb.pack()
        lb.place(x=0, y=0)
        for item in ["ACM", "CNKI", "SPRINGER", 'HANS']:
            lb.insert(END, item)
        # print(lbv.get())
        def myPrint(event):
            print(lb.get(lb.curselection()))
            sele = lb.get(lb.curselection())

            if sele == 'ACM':

                root = Tk()
                Run_tk_search(root, spider='ACM')
                root.mainloop()


            elif sele == 'CNKI':

                root = Tk()
                Run_tk_search(root, spider='CNKI')
                root.mainloop()

    
            elif sele == 'SPRINGER':

                root = Tk()
                Run_tk_search(root, spider='SPRINGER')
                root.mainloop()

            elif sele == 'HANS':

                root = Tk()
                Run_tk_search(root, spider='HANS')
                root.mainloop()

        lb.bind('<Double-Button-1>', myPrint)



#三大顶会爬虫开始运行的地方
    '''
    调用函数启动相关的爬虫
    '''
    def Choose_Second(self):
        lbv = StringVar()
        lb = Listbox(self.root, selectmode=SINGLE, height=6, width=30 , listvariable=lbv)
        lb.pack()
        lb.place(x=0, y=0)
        for item in ["CVPR", "ECCV", "ICCV", "LCLR", 'ICML', 'IJCAI', 'NIPS']:
            lb.insert(END, item)

        def myPrint(event):
            print(lb.get(lb.curselection()))
            sele = lb.get(lb.curselection())

            if sele == 'CVPR':

                root = Tk()
                Run_tk(root, spider='CVPR')
                root.mainloop()
                # RunSpider.Run_Process_CVPR_Spider()

            elif sele == 'ECCV':

                root = Tk()
                Run_tk(root, spider='ECCV')
                root.mainloop()
                    # RunSpider.Run_Process_ECCV_Spider()

            elif sele == 'ICCV':

                root = Tk()
                Run_tk(root, spider='ICCV')
                root.mainloop()

            elif sele == 'ICML':

                root = Tk()
                Run_tk(root, spider='ICML')
                root.mainloop()

            elif sele == 'LCLR':

                root = Tk()
                Run_tk(root, spider='LCLR')
                root.mainloop()

            elif sele == 'IJCAI':

                root = Tk()
                Run_tk(root, spider='IJCAI')
                root.mainloop()

            else:

                root = Tk()
                Run_tk(root, spider='NIPS')
                root.mainloop()

        lb.bind('<Double-Button-1>', myPrint)



#显示数据库内容的控件,并展示到屏幕上
    '''
    在scrapy选项卡中的爬取结果显示中,使用了ttk.Treeview
    '''
    def Show_Date(self):
        data = self.Mysql_Show_Data("*")
        tree = Treeview(self.root)
        tree.pack()
        tree.place(x=220, y=0)
        #定义列
        tree['columns'] = ('title','authors','publicationDate','publication','publisher','snippet','keyword','file_urls','search','crawl_time')
        #设置列
        tree.column('title',width=100)
        tree.column('authors',width=50)
        tree.column('publicationDate',width=50)
        tree.column('publication',width=50)
        tree.column('publisher',width=50)
        tree.column('snippet',width=200)
        tree.column('keyword',width=50)
        tree.column('file_urls',width=50)
        tree.column('search',width=50)
        tree.column('crawl_time',width=50)
        #设置表头
        tree.heading('title', text='title')
        tree.heading('authors', text='authors')
        tree.heading('publicationDate', text='publicationDate')
        tree.heading('publication', text='publication')
        tree.heading('publisher', text='publisher')
        tree.heading('snippet', text='snippet')
        tree.heading('keyword', text='keyword')
        tree.heading('file_urls', text='download_url')
        tree.heading('search', text='search')
        tree.heading('crawl_time', text='crawl_time')
        for x in range(len(data)):
            tree.insert('',x,text='line%d' %x,values=('%s' %data[x][0],'%s' %data[x][1],'%s' %data[x][2],'%s' %data[x][3],'%s' %data[x][4],'%s' %data[x][5],'%s' %data[x][6],'%s' %data[x][7],'%s' %data[x][8],'%s' %data[x][9]))
        



#查询数据库,对数据库进行删除等操作
    '''
    对数据库进行关键词的删除,保证数据库不会数据太多
    '''
    def Search_Mysql(self):
        def showInfo():
            num = int(entry.get())
            self.Txt_Show(num,5)
        def showInfo1():
            key = str(entry2.get())
            self.Mysql_Show_Data(key)
        def showInfo2():
            num = int(entry1.get())
            self.Txt_Show(num,7)
        def showInfo3():
            self.Mysql_Show_Data("xxx")
        label = Label(text = '根据行号查找url')
        label.pack()
        label.place(x=1130,y=0)
        labe2 = Label(text='根据行号查找snippet')
        labe2.pack()
        labe2.place(x=1130, y=100)
        labe3 = Label(text='关键词删除数据库内容')
        labe3.pack()
        labe3.place(x=1130, y=200)
        entry = Entry(self.root)
        entry.pack()
        entry1 = Entry(self.root)
        entry1.pack()
        entry2 = Entry(self.root)
        entry2.pack()
        entry.place(x=1130, y=120)
        entry1.place(x=1130, y=20)
        entry2.place(x=1130, y=220)
        button1 = Button(self.root, text='搜索', command=showInfo)
        button1.pack()
        button1.place(x=1160, y=160)
        button2 = Button(self.root, text='搜索', command=showInfo2)
        button2.pack()
        button2.place(x=1160, y=60)
        button3 = Button(self.root, text='删除', command=showInfo1)
        button3.pack()
        button3.place(x=1160, y=260)
        button4 = Button(self.root, text='一键删除数据库中的所有内容', command=showInfo3)
        button4.pack()
        button4.place(x=1125, y=320)



#文本内容显示
    '''
    屏幕下方的文本框显示
    '''
    def Txt_Show(self,num,k):
        data = self.Mysql_Show_Data("*")
        text = Text(self.root, width=128, height=10)
        # text.insert(tkinter.INSERT, '使用须知')
        text.pack()
        text.place(x=220, y=230)
        ustr = str(data[num][k])
        text.insert(INSERT, ustr)



#帮助信息
    '''
    帮助信息,帮助选项卡中
    '''
    def Help(self):
        text = Text(self.root, width=30, height=8)
        text.pack()
        text.place(x=0, y=0)
        ustr = '''   当程序的关键词错误时,请打开Error_Recovery.exe修改关键词!'''
        text.insert(INSERT, ustr)



#下载地址显示
    '''
    显示下载地址
    '''
    def Path_Detail(self):
        text = Text(self.root, width=30, height=8)
        text.pack()
        text.place(x=0, y=0)
        path = frozen_dir.app_path() + r'\download'
        ustr = "%s"%path
        text.insert(INSERT, ustr)



#前三个爬虫关键字控制
    '''
    通过对相关文件的读写操作,实现关键词的可控制化
    '''
    def Search_Key_First(self):
        Dir = PATHS.CONFIG_ALL_DIR + r'\Search.txt'
        def showInfo():
            content = entry.get()

            content = "%s" %str(content)
            print(content)
            Management.File_Reset_Search(content,Dir)
        def File_View(paths=Dir):
            path = paths
            with open(path,"r") as f:
                ustr = str(f.read())
                f.close()
                return ustr
        def Key_Look():
            tkinter.messagebox.showinfo('提示','搜素关键词为: %s'%File_View())
        label = Label(text='输入要检索的关键字')
        label.pack()
        label.place(x=40,y=150)
        entry = Entry(self.root)
        # entry.insert(0, '输入要检索的关键字(输入完成后要在scrapy中选择相应的爬虫)')
        entry.pack()
        entry.place(x=40, y=170)
        button1 = Button(self.root, width=8, text='确定', command=showInfo)
        button2 = Button(self.root, width=8, text='关键词', command=Key_Look)
        button2.pack()
        button1.pack()
        button1.place(x=120, y=200)
        button2.place(x=40, y=200)



#三大顶会年份控制
    '''
    通过对相关文件的读写操作,实现关键词的可控制化
    '''
    def Search_Key_Second(self):
        Dir = PATHS.CONFIG_ALL_DIR + r'\Search_Three.txt'
        def showInfo():
            content = entry.get()

            content = "%s" %str(content)
            print(content)
            Management.File_Reset_Search(content,Dir)
        def File_View(paths=Dir):
            path = paths
            with open(path,"r") as f:
                ustr = str(f.read())
                f.close()
                return ustr
        def Key_Look():
            tkinter.messagebox.showinfo('提示','搜素关键词为: %s'%File_View())

        label = Label(text='输入要检索的年份')
        label.pack()
        label.place(x=40, y=250)
        entry = Entry(self.root)
        # entry.insert(0, '输入要检索的年份(输入完成后要在scrapy中选择相应的爬虫)')
        entry.pack()
        entry.place(x=40, y=270)
        button1 = Button(self.root, width=8, text='确定', command=showInfo)
        button2 = Button(self.root, width=8, text='关键词', command=Key_Look)
        button1.pack()
        button2.pack()
        button1.place(x=120, y=300)
        button2.place(x=40, y=300)



#三大顶会爬虫使用须知
    '''
    由于三大顶会的爬虫有年份的控制,键入相关年份便可达到控制的目的,但不能乱键入值
    '''
    def Text_Warning(self):
        text = Text(self.root, width=30, height=8)
        text.pack()
        text.place(x=0, y=0)
        ustr = '''   特别注意:关于顶会的爬虫,根据提示填入年份和选取爬虫。
    CVPR:(2013-2019)
    ICCV:(2013,2015,2017,2019)
    ECCV:(2018)
    ICLR:(2013,2014,2016-2020)
    ICML:(2017,2019)
    IJCAL:(2017,2018)
    NIPS:(2010-2019)'''
        text.insert(INSERT, ustr)
#----------------------------------------------终止位置---------------------------------------------------

