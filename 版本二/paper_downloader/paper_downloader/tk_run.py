from tkinter import *
from tkinter.ttk import *
import PATHS
import Management
import RunSpider
import tkinter.messagebox
import frozen_dir
path1 = PATHS.CONFIG_ALL_DIR + r'\Search.txt'
path2 = PATHS.CONFIG_ALL_DIR + r'\Search_Three.txt'
path3 = PATHS.CONFIG_ALL_DIR + r'\settings.ico'






#----------------------开始-------------------------------------
class Run_tk():
    def __init__(self,root,spider):
        self.spider = spider
        self.root = root
        self.root.title('运行爬虫')
        self.root.iconbitmap(path3)
        self.creat_menu()

    def creat_menu(self):
        Dir = PATHS.CONFIG_ALL_DIR + r'\Search_Three.txt'
        def showinfo():
            content = name.get()
            content = "%s" % str(content)
            print(content)
            Management.File_Reset_Search(content, Dir)
        self.frame = Frame(self.root,height=50, width=100)
        self.frame.pack(expand=1)
        label = Label(self.frame, text='输入关键词:')
        self.tiebavar = StringVar()
        name = Entry(self.frame, textvariable=self.tiebavar, width=22)
        button = Button(self.frame,text='确定',command=showinfo)
        label.grid(row=0, column=0, sticky='we')
        name.grid(row=0, column=1)
        button.grid(row=0, column=2)
        # grid：存放路径
        self.grid_path(self.frame)
        # grid：开始按钮等
        self.grid_buttons(self.frame)
    


    def grid_path(self,the_frame):
        path_label= Label(the_frame, text='存放路径:',anchor='e')
        self.pathvar=StringVar()
        path_entry = Entry(the_frame, width=25, textvariable=self.pathvar)
        path_entry.insert(0,self.Path_Detail())
        path_label.grid(row=1, column=0,sticky='w')
        path_entry.grid(row=2, column=0, columnspan=3,sticky='we' )
    


    def grid_buttons(self,the_frame):
        def File_View(paths=path2):
            path = paths
            with open(path,"r") as f:
                ustr = str(f.read())
                f.close()
                return ustr
        def Key_Look():
            tkinter.messagebox.showinfo('提示','搜素关键词为: %s'%File_View())
        self.button_frame=Frame(the_frame)
        self.button_frame.grid(row=3, columnspan=3)
        self.start_button=Button(self.button_frame,text="开始爬取",width=25,command=self.run)
        self.start_button1 = Button(self.button_frame, text="关键词查看", command=Key_Look)
        #回调函数是 运行scrapy
        self.start_button.pack(side="right", expand="yes", fill="both", padx=5, pady=5)
        self.start_button1.pack(side="left", expand="yes", fill="both", padx=5, pady=5)
    


    def run(self):
        if self.spider == 'ICCV':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_ICCV_Spider()
            else:
                pass
        elif self.spider == 'CVPR':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_CVPR_Spider()
            else:
                pass
        elif self.spider == 'ECCV':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_ECCV_Spider()
            else:
                pass
        elif self.spider == 'LCLR':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_Iclr_Spider()
            else:
                pass
        elif self.spider == 'ICML':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_Icml_Spider()
            else:
                pass
        elif self.spider == 'IJCAI':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_Ijcai_Spider()
            else:
                pass
        else:
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_Nips_Spider()
            else:
                pass



    def Path_Detail(self):
        path = frozen_dir.app_path() + r'\download'
        return path








class Run_tk_search():

    def __init__(self,root,spider):
        self.spider = spider
        self.root = root
        self.root.title('运行爬虫')
        self.root.iconbitmap(path3)
        self.creat_menu()



    def creat_menu(self):
        Dir = PATHS.CONFIG_ALL_DIR + r'\Search.txt'
        def showinfo():
            content = name.get()
            content = "%s" % str(content)
            print(content)
            Management.File_Reset_Search(content, Dir)
        self.frame = Frame(self.root,height=50, width=100)
        self.frame.pack(expand=1)
        label = Label(self.frame, text='输入关键词:')
        self.tiebavar = StringVar()
        name = Entry(self.frame, textvariable=self.tiebavar, width=22)
        button = Button(self.frame,text='确定',command=showinfo)
        label.grid(row=0, column=0, sticky='we')
        name.grid(row=0, column=1)
        button.grid(row=0, column=2)
        # grid：存放路径
        self.grid_path(self.frame)
        # grid：开始按钮等
        self.grid_buttons(self.frame)



    def grid_path(self,the_frame):
        path_label= Label(the_frame, text='存放路径:',anchor='e')
        self.pathvar=StringVar()
        path_entry = Entry(the_frame, width=25, textvariable=self.pathvar)
        path_entry.insert(0,self.Path_Detail())
        path_label.grid(row=1, column=0,sticky='w')
        path_entry.grid(row=2, column=0, columnspan=3,sticky='we' )



    def grid_buttons(self,the_frame):
        def File_View(paths=path1):
            path = paths
            with open(path,"r") as f:
                ustr = str(f.read())
                f.close()
                return ustr
        def Key_Look():
            tkinter.messagebox.showinfo('提示','搜素关键词为: %s'%File_View())
        self.button_frame=Frame(the_frame)
        self.button_frame.grid(row=3, columnspan=3)
        self.start_button=Button(self.button_frame,text="开始爬取",width=25,command=self.run) #回调函数是 运行scrapy
        self.start_button1 = Button(self.button_frame, text="关键词查看", command=Key_Look)
        self.start_button.pack(side="right", expand="yes", fill="both", padx=5, pady=5)
        self.start_button1.pack(side="left", expand="yes", fill="both", padx=5, pady=5)



    def run(self):

        if self.spider == 'ACM':
            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_ACM_Spider()
            else:
                pass

        elif self.spider == 'SPRINGER':

            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_SPRINGER_Spider()
            else:
                pass

        elif self.spider == 'CNKI':

            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_CNKI_Spider()
            else:
                pass

        elif self.spider == 'HANS':

            warn = tkinter.messagebox.askokcancel("开始提示", "是否开始下载?")
            if warn == True:
                RunSpider.Run_Process_HANS_Spider()
            else:
                pass



    def Path_Detail(self):

        path = frozen_dir.app_path() + r'\download'
        return path
#-------------------------结束----------------------------------------------
if __name__ == '__main__':
    root = Tk()
    app = Run_tk_search(root,'SPRINGER')
    root.mainloop()