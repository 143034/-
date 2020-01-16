from tkinter import *
from tkinter.ttk import *
import PATHS
import tkinter.messagebox

import csv


path = PATHS.CONFIG_ALL_DIR + r'\data.csv'

class Display_data():
    def __init__(self,root):
        self.root = root
        self.root.title('数据查看')
        self.root.resizable(0, 0)
        self.display()

    def display(self):
        self.Frame = Frame()
        tree = Treeview(self.root,show = "headings")
        tree['columns'] = ('title', 'author', 'file_urls')
        tree.heading('title', text='title')
        tree.heading('author', text='author')
        tree.heading('file_urls', text='file_urls')
        with open(path,'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            result = list(reader)
            for i in range(len(result)-1):
                tree.insert('',index=i,values=(result[i+1][0],result[i+1][1],result[i+1][2]))
        tree.grid()
        self.Frame.grid()

if __name__ == "__main__":
    root = Tk()
    app = Display_data(root)
    root.mainloop()




