#!/usr/bin/python
# -*- coding: utf-8 -*-
#import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import webbrowser, os , re , sys, time
from os import path
global pfad

stand = "GitHelper   Version: 1.0 Software Stand: 18.10.2019"
NX = 8
NY = 8
class Application(ttk.Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.configure(background='black')
        #self.rowconfigure(15, minsize='30')
        #self.columnconfigure(15, minsize='30')
        self.parent = master
        self.master = master
        self.tool_bar()
        self.Werbung()
        self.hintergrund()
        #self.create_test_canvas()
        #self.place() 
        
        self.grid()
        
        self.pfad=str(os.getcwd())
        ##Buttons
        self.b1 = Button(self, text="git clone",                command=self.git_clone,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b1.grid(row=1,column=4)
        
        self.b2 = Button(self, text="git status",               command=self.git_status,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b2.grid(row=2,column=4)
        
        self.b3 = Button(self, text="git pull",                 command=self.git_pull,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b3.grid(row=3,column=4)
        
        self.b4 = Button(self, text="git add -A",               command=self.git_add,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b4.grid(row=4,column=4)
        
        self.b5 = Button(self, text='git commit -m "Message" ', command=self.git_commit,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b5.grid(row=5,column=4)
        
        self.b6 = Button(self, text="git push",                 command=self.git_push,bg='black',fg='SteelBlue1',font='impact 20',relief='flat')
        self.b6.grid(row=6,column=4)
        
        ##Entrys
        
        self.varTN1 = StringVar()
        self.varTN1.set("current path")
        self.labelTN1 = Label(self,textvariable=self.varTN1,height = 1,bg='black',fg='SteelBlue1',font='impact 15',relief='flat')
        self.labelTN1.grid(row=9,column=5,columnspan=NX)
        #self.pfad="path"
        self.boxTN1=Entry(self,textvariable=self.pfad,width=80,bg='grey',fg='SteelBlue1',font='impact 10',relief='flat')
        self.boxTN1.grid(row=10,column=0,columnspan=NX)
        
        self.varTN2 = StringVar()
        self.varTN2.set("Message ")
        self.labelTN2 = Label(self,textvariable=self.varTN2,height = 1,bg='black',fg='SteelBlue1',font='impact 15',relief='flat')
        self.labelTN2.grid(row=4,column=5)
        self.message = "Please enter commit Message!"       
        self.boxTN2=Entry(self,textvariable=self.message,width=80,bg='grey',fg='SteelBlue1',font='impact 10',relief='flat')
        self.boxTN2.grid(row=5,column=5)        
        
        self.varTN3 = StringVar()
        self.varTN3.set("clone Adress")
        self.labelTN3 = Label(self,textvariable=self.varTN3,height = 1,bg='black',fg='SteelBlue1',font='impact 15',relief='flat')
        self.labelTN3.grid(row=0,column=5)
        self.clone_repo = "Please enter http:// Repo Adress from GitHub"       
        self.boxTN3=Entry(self,textvariable=self.clone_repo,width=80,bg='grey',fg='SteelBlue1',font='impact 10',relief='flat')
        self.boxTN3.grid(row=1,column=5)
        self.display()
        
    def git_clone(self):
        self.clone_repo = self.boxTN3.get()
        
        if self.clone_repo == "Please enter http:// Repo Adress from GitHub":
            print ("git clone ",self.clone_repo )
            pass
        else:
            self.display()
            print ("git clone ",self.clone_repo )
            #os.system('git clone ' + (self.clone_repo))
            
    def git_status(self):
        print ("git status")
        #os.system('git status')
        self.display()
    def git_pull(self):
        print ("git pull") 
        #os.system('git pull')
        self.display()
    def git_add(self):
        print ("git add -A")
        #os.system('git add -A')
        self.display()
    def git_commit(self):
        self.message = self.boxTN2.get()
        if self.message == "Please enter commit Message!":
            print ("git commit -m " + '"' + self.message + '"')
            pass
        else:
            self.display()
            print ("git commit -m " + '"' + self.message + '"')
        #os.system('git clone + '"' + self.meassage + '"')
        self.display()
    def git_push(self):
        print ("git push") 
        #os.system('git push')
        self.display()
        
    def tool_bar(self):

        menu = Menu(self.master)
        self.master.config(menu=menu,bg='black')
        
        file = Menu(menu)
        file.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="Datei", menu=file)
        
        #edit = Menu(menu)
        #edit.add_command(label="öffne neue *.Ino Datei", command=self.open_new_ino)
        #menu.add_cascade(label="*.Ino Datei", menu=edit)
        
        about = Menu(menu)
        about.add_command(label="Navarra Software Solutions", command=self.about)
        menu.add_cascade(label="About", menu=about)
    
    def quit(self):
        sys.exit(0)
            
    def about(self):

        self.about = Toplevel(self)
        self.about.configure(background='black')
        self.about.geometry("550x250")
        #self.about.iconbitmap(self.pfad +'NAVARRAICON.ico')
        Label(self.about, text=str("[") + ("   ") + str("]"),bg=(self.BG),fg='grey',font='Helvetica 50 bold ').place(x=10,y=10);
        Label(self.about, text=str("*"),bg=(self.BG),fg=(self.FGBLUE),font=((self.FONT) + ("124"))).place(x=40,y=00);
        
        Label(self.about, text=(self.NAVARRA), bg=(self.BG), fg=(self.FGBLUE),font=((self.FONT) + ("22"))).place(x=130,y=20);
        Label(self.about, text=(self.SLOGAN) , bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=130,y=60);
        Label(self.about, text=(self.WEBSITE), bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=130,y=100);
        Label(self.about, text=(self.MAIL)   , bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=130,y=140);
        Label(self.about, text=(stand)  , bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) +  ("8"))).place(x=250,y=230);
    
    def hintergrund(self):
        Label(self, text=str("[") + ("   ") + str("]"),bg=(self.BG),fg='grey',font='Helvetica 50 bold ').place(x=350,y=110);
        Label(self, text=str("*"),bg=(self.BG),fg=(self.FGBLUE),font=((self.FONT) + ("124"))).place(x=380,y=100);
        
        #Label(self, text=(self.NAVARRA), bg=(self.BG), fg=(self.FGBLUE),font=((self.FONT) + ("22"))).grid(row=3,column=10,rowspan=3,columnspan=3);
        #Label(self, text=(self.SLOGAN) , bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=255,y=160);
        #Label(self, text=(self.WEBSITE), bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=255,y=200);
        #Label(self, text=(self.MAIL)   , bg=(self.BG), fg=(self.FG)    ,font=((self.FONT) + ("14"))).place(x=255,y=240);
    
    def display(self):
        
        self.boxTN1.delete(0 ,END)
        self.boxTN1.insert(0,(self.pfad))
        self.boxTN2.delete(0 ,END)
        self.boxTN2.insert(0,(self.message))
        self.boxTN3.delete(0 ,END)
        self.boxTN3.insert(0,(self.clone_repo))
        
    def Werbung(self):
        
        self.LOGO    = "[*]"
        self.NAVARRA = "NAVARRA SOFTWARE SOLUTIONS"
        self.BG      = 'black'
        self.FG      = 'white'
        self.FGBLUE  = 'SteelBlue1'
        self.FONT    = 'impact '
        self.SLOGAN  = "let my Software do it for YOU..."
        self.WEBSITE = "https://NAVARRA.home.blog"
        self.MAIL    = "contactNAVARRA@gmail.com"
        self.CEO     = "Sebastian de la Vega"
        self.PHONE   = "Phone: +49 (0) 151 566 57246 "
        
        def show_werbung(self):
            print (stand)
            print ("")
            print ("Grafisches Tool um das arbeiten mit GIT zu erleichtern")
            print ("")
            print ("von:")
            print (self.NAVARRA)
            print (self.SLOGAN)
            print (self.WEBSITE)
            print (self.MAIL)
            print (self.CEO)
            print (self.PHONE)
            print ("\n")
        #self.show_werbung()
        
    
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
def main():
    root = Tk()
    root.title("GitHelper")
    root.resizable(True, True)
    #root.resizable(False, False)
    root.configure(background='black')
    root.wm_overrideredirect(False)
    root.geometry("800x500")
    app = Application(root)
    app.pack(fill="both",expand=False)
    root.mainloop()   
if __name__ == "__main__":
    main()