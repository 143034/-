from tkinter import *
from tkinter.ttk import *
import PATHS
from RunSpider import Run_all
from Sele_path import  Sele
import csv
import time

BASE = PATHS.Export_data + '/pneumonia/'
BASE_1 = PATHS.Export_data + '/pro_pneumonia/'

class Display_data():
    def __init__(self,root=Tk()):
        Run_all()
        time.sleep(2)
        self.root = root
        self.root.title('全国患病数据查看(第一行是全国数据)')
        self.root.resizable(0, 0)
        self.display()
        self.root.mainloop()

    def display(self):
        self.Frame = Frame()
        tree = Treeview(self.root,show = "headings")
        tree['columns'] = ('Confirmed', 'Suspected', 'Healing', 'Death', 'Deadline')
        tree.heading('Confirmed', text='确诊人数')
        tree.heading('Suspected', text='观察人数/省份')
        tree.heading('Healing', text='治疗人数')
        tree.heading('Death', text='死亡人数')
        tree.heading('Deadline', text='截止日期')
        path = BASE + Sele(BASE)
        path1 = BASE_1 + Sele(BASE_1)
        result = self.Read_csv(path)
        result_1 = self.Read_csv(path1)
        for i in range(len(result_1)-1):
            tree.insert('',index=i,values=(result_1[i+1][0],result_1[i+1][3],result_1[i+1][2],result_1[i+1][1],result[1][1]))
        for i in range(len(result)-1):
            tree.insert('',index=i,values=(result[i+1][0],result[i+1][4],result[i+1][3],result[i+1][2],result[i+1][1]))
        tree.grid()
        self.Frame.grid()
    def Read_csv(self,sele):
        path = sele
        with open(path,'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            result = list(reader)
            return result
    # def Run_spider(self):
    #     cmdline.execute("scrapy crawlall".split())

if __name__ == "__main__":
    root = Display_data()




