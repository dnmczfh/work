# -*- coding: GBK -*-
import os
from time import sleep
from tkinter import *


class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()
        #���ô��ڱ���
        self.top.title("Ŀ¼ѡ��")

        self.label = Label(self.top,
                           text='��ǰĿ¼')
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
                           text='���ֹ�¼��һ��Ŀ¼��')
        self.labe2.pack()

        self.dirn = Entry(self.top, width=50,
                          textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='�������',
                          command=self.clrDir,
                          activeforeground='white',
                          activebackground='blue')
        self.ls = Button(self.bfm, text='��ʾĿ¼����',
                         command=self.doLS,
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='ȷ��',
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
            error = tdir + ': �ļ�������'
        elif not os.path.isdir(tdir):
            error = tdir + ': ����һ��Ŀ¼'
            self.cwd.set(self.last)
            self.dirs.config(
                selectbackground='LightSkyBlue')
            self.top.update()
            return
        self.cwd.set('�Ҳ��������Ŀ¼')
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
            #Ŀ¼���ļ�ʹ�ò�ͬ����ʾ
            if os.path.isdir(eachFile):
                self.dirs.insert(END, '['+eachFile+']')
            else:
                self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

    def submit(self):
        print("ѡ���Ŀ¼��{}".format(os.getcwd()))


def main():
    d = DirList(True)
    mainloop()


if __name__ == '__main__':
    main()