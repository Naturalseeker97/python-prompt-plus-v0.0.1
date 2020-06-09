##copyright @ Naturalseeker97
## pyp+ v0.0.1 (python prompt + version 0.0.1)

## imports
import os
from tkinter import *
import time

##settings
checkforstart = True
os.system("cls")
port = 2604
start_folder = os.chdir("C://")
local_folder = os.getcwd()
gettime = time.ctime()
isprogramlive = False

##maincode

##%sub% is live check
def isprogramlivecheck():
    ##settings
    global isprogramlive
    ifcheck = True

    ##code
    if ifcheck == True and  isprogramlive == False:
        isprogramlive = True
        dowhile()

##

def traceip():
    ip = input("enter ip or hostname  ")
    os.system("tracert "+ str(ip))

def getip():
    os.system("ipconfig /all")

def ping():
    ip = input("enter ip or hostname  ")
    os.system("ping "+ str(ip))

def newTk():
    global win
    width = input("enter width(only numbers)  ")
    height = input("enter height(only numbers)  ")
    title = input("enter window title  ")
    win = Tk()
    win.title(title)
    win.geometry(str(width)+"x"+str(height))

def newtext():
    fg = input("enter foreground color  ")
    bg = input("enter background color(for non color enter non)  ")
    text = input("enter text  ")
    if bg == "non":
        Label(win,fg=fg,text=text).pack()
    else:
        Label(win,fg=fg,text=text,bg=bg).pack()

def newspace():
    Label(win,text="").pack()

##%sub% start program and end programm
def start():
    isprogramlivecheck()

def endprogramm():
    ##settings
    global isprogramlive,ifcheck
    isprogramlive = False
    ifcheck = False

##%functions% main functions
def timeoutput():
    print(gettime)

def changedir():
    path = input("enter path (with / )(exampel C://user/yourusername)  ")
    os.chdir(str(path))
    
##%sub% do while
def dowhile():
    while isprogramlive:
        ##globals
        global gettime
        
        ## input
        ter_in = input("pyp+ : "+str(os.getcwd()) + "  ==> ")
        ter_in = ter_in.strip()
        ter_list = list(ter_in)
        ter_split = ter_in.split()
        
        ##new settings / vars
        gettime = time.ctime()
        nowlocal_folder = os.getcwd()
        

        ##get input cmd
        if ter_in == "exit" or ter_in == "leave":
            endprogramm()
        elif ter_in == "time" or ter_in == "date":
            timeoutput()
        elif ter_in == "dirs" or ter_in == "dir" or ter_in == "cdir":
            os.system("dir")
        elif ter_in == "changedir" or ter_in == "chdir":
            changedir()
        elif ter_in == "clear" or ter_in == "cls" or ter_in == "clear prompt" or ter_in == "clear commandline":
            os.system("cls")
        elif ter_in == "color 1" or ter_in == "color a":
            os.system("color a")
        elif ter_in == "color 2" or ter_in == "color b":
            os.system("color b")
        elif ter_in == "color 3" or ter_in == "color c":
            os.system("color c")
        elif ter_in == "localdir" or ter_in == "ldir" or ter_in == "cwd":
            print(str(nowlocal_folder))
        elif ter_in == "ping":
            ping()
        elif ter_in == "getip":
            getip()
        elif ter_in == "traceip":
            traceip()
        elif ter_in == "newTk":
            newTk()
        elif ter_in == "newtext":
            newtext()
        elif ter_in == "newspace":
            newspace()
        elif ter_in == "cmd":
            os.system("start")
        elif ter_in == "pshell" or ter_in == "powershell":
            os.system("powershell")
        elif ter_in == "netsh":
            os.system("netsh")
        elif ter_in == "shutdown --me":
            os.system("shutdown -s -t 20")
        elif ter_in == "shutdown --stop":
            os.system("shutdown -a")
        elif ter_in == "shutdown --other":
            os.system("shutdown -i")
        elif ter_in == "hex2utf-8":
            bytearray.fromhex(input("enter hex  ")).decode()
        elif ter_in == "info":
            print("if u got idees for commands (or u made extra cmd in python) send it to sup.pypplusqgmail.com ")
        elif ter_in == "support":
            print("for support send a message with your problem to sup.pypplus@gmail.com")
        

        ##troll cmds
        elif ter_in == "crash":
            crash = True
            while crash:
                os.system("start")
        
            

        ##if not a command
        else:
            print("error command " + str(ter_in) + " was not found")
            






