from tkinter import *
from tkinter import ttk
import main
import os

class filemanager:
    def __init__(self,master):
            self.master=master
            self.total=''
            master.title('File Manager')
            master.geometry('400x350')
            drives=main.data()
            button=ttk.Button(root, text="Back",command=self.back)
            button.pack()
            self.Lb1=Listbox(master,width=400,height=350,font=('times',13))
            for i,v in enumerate(drives):
                self.Lb1.insert(i,v)
            self.Lb1.bind('<Double-1>',self.get_val)
            self.Lb1.pack()
            
    def back(self):
        if len(self.total)==3:
            self.Lb1.delete(0,'end')
            drives=main.data()
            for i,v in enumerate(drives):
                self.Lb1.insert(i,v)
            self.total=''
        else:
            os.chdir(self.total)
            os.chdir('..')
            self.total=os.getcwd()
            self.Lb1.delete(0,'end')
            for i,v in enumerate(os.listdir(self.total)):
                    self.Lb1.insert(i,v)
            
    def get_val(self,master):
        val=str((self.Lb1.get(ACTIVE)))
        self.total+=(val+'\\')
        self.Lb1.delete(0,'end')
        for i,v in enumerate(os.listdir(self.total)):
                self.Lb1.insert(i,v)
        self.Lb1.bind('<Double-1>',self.get_val)
        
root=Tk()
app=filemanager(root)
root.mainloop()

'''
from tkinter import *
from tkinter import ttk
import main
import os

class filemanager:
    def __init__(self,master):
            self.c_path=''
            self.master=master
            master.title('File Manager')
            master.geometry('400x350')
            drives=main.get_drives_list()
            button=ttk.Button(root, text="Back")
            button.pack()
            button2=ttk.Button(root, text="Back")
            button2.pack()
            self.Lb1=Listbox(master,width=400,height=350,font=('times',13))
            for i,v in enumerate(drives):
                self.Lb1.insert(i,v)
            self.Lb1.bind('<Double-1>',self.get_val)
            self.Lb1.pack()
            
            
    def get_val(self,master):
        val=str((self.Lb1.get(ACTIVE)))
        self.c_path+=(val+'\\')
        self.Lb1.delete(0,'end')
        for i,v in enumerate(os.listdir(self.c_path)):
                self.Lb1.insert(i,v)
        self.Lb1.bind('<Double-1>',self.get_val)
        
root=Tk()
app=filemanager(root)
root.mainloop()
'''
