# -*- coding: GBK -*-
import os
from time import sleep
from tkinter import *


class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()
        #设置窗口标题
        self.top.title("目录选择")

        self.label = Label(self.top,
                           text='当前目录')
        self.label.pack()

        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue',
                          font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15,
                            width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.labe2 = Label(self.top,
                           text='请手工录入一个目录：')
        self.labe2.pack()

        self.dirn = Entry(self.top, width=50,
                          textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='清空输入',
                          command=self.clrDir,
                          activeforeground='white',
                          activebackground='blue')
        self.ls = Button(self.bfm, text='显示目录内容',
                         command=self.doLS,
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='确定',
                           command=self.submit,
                           activeforeground='white',
                           activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ': 文件不存在'
        elif not os.path.isdir(tdir):
            error = tdir + ': 不是一个目录'
            self.cwd.set(self.last)
            self.dirs.config(
                selectbackground='LightSkyBlue')
            self.top.update()
            return
        self.cwd.set('找不到输入的目录')
        self.top.update()
        if '[' in tdir:
            tdir=tdir[1: len(tdir)-1]
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            #目录和文件使用不同的显示
            if os.path.isdir(eachFile):
                self.dirs.insert(END, '['+eachFile+']')
            else:
                self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

    def submit(self):
        print("选择的目录是{}".format(os.getcwd()))


def main():
    d = DirList(True)
    mainloop()


if __name__ == '__main__':
    main()