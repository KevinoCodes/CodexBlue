from tkinter import *
import random
from PIL import ImageTk, Image

win = Tk()
win.title("Goal Tracker Login Page")
win.resizable(width=False, height=False)
win.configure(background="light grey")





#The Top "I accomplished the goal" button

def GoalFinish1():
    TitleText1 = Text(Title1, width=41, height=18, bg="#a4b8c4")
    TitleText1.grid(row=1,column=0)
    TitleText1.destroy()
    TitleText1 = Text(Title1, width=41, height=18, bg="#a4b8c4")
    TitleText1.grid(row=1,column=0)

    SideNtxt = Text(SideN1,width=41, height=18,bg="#a4b8c4")
    SideNtxt.grid(row=1,column=0)
    SideNtxt.destroy()
    SideNtxt = Text(SideN1,width=41, height=18,bg="#a4b8c4")
    SideNtxt.grid(row=1,column=0)
    
    print("task added")
    progress[0] = progress[0] + 1
    ProgressB.create_rectangle(0, 0, 5.2*progress[0],50, fill="#a4b8c4")

    print("task added")
    progress[0] = progress[0] + 1
    ProgressB2.create_rectangle(0, 0, 31*progress[0],50, fill="#a4b8c4")

    if progress == [10]:
        Goal2.destroy()
        YAY = Label(ProgressBar,text="Monthly goal Completed! Stay Tuned for more!", bg="#929a9b")
        YAY.grid(row=2, column=0)

    if progress == [60]:
        Goal.destroy()
        WOW = Label(ProgressBar,text="Yearly Goal Completed! Stay Tuned for more!", bg="#929a9b")
        WOW.grid(row=0, column=0)
        



        
        






#The Bottom "I accomplished the goal" button

def GoalFinish2():
    TitleText2 = Text(Title2, width=41, height=18, bg="#66a9af")
    TitleText2.grid(row=1,column=0)
    TitleText2.destroy()
    TitleText2 = Text(Title2, width=41, height=18, bg="#66a9af")
    TitleText2.grid(row=1,column=0)

    SideNtxt2 = Text(SideN2,width=41, height=18,bg="#66a9af")
    SideNtxt2.grid(row=1,column=0)
    SideNtxt2.destroy()
    SideNtxt2 = Text(SideN2,width=41, height=18,bg="#66a9af")
    SideNtxt2.grid(row=1,column=0)

    print("task added")
    progress[0] = progress[0] + 1
    ProgressB.create_rectangle(0, 0, 5.2*progress[0],50, fill="#a4b8c4")

    print("task added")
    progress[0] = progress[0] + 1
    ProgressB2.create_rectangle(0, 0, 31*progress[0],50, fill="#a4b8c4")

    if progress == [10]:
        Goal2.destroy()
        YAY = Label(ProgressBar,text="Monthly goal Completed! Stay Tuned for more!", bg="#929a9b")
        YAY.grid(row=2, column=0)

    if progress == [60]:
        Goal.destroy()
        WOW = Label(ProgressBar,text="Yearly Goal Completed! Stay Tuned for more!", bg="#929a9b")
        WOW.grid(row=0, column=0)


    
        
def UserLogout():
    win.destroy()

#Doundations of program. These are the 5 frams that divide up my program. It is a 3x2 frame rectangular window but the right 2 frames are merged, meaning there is only 5 frames. 

Goal1 = Frame(win,borderwidth = 1.5, width=300, height=350, bg="#a4b8c4")
Goal1.grid(row=0,column=0)

Goal2= Frame(win,borderwidth = 1.5,width=300, height=350, bg="#66a9af")
Goal2.grid(row=1,column=0)

Note1 = Frame(win,borderwidth = 1.5, width=300, height=350, bg="#a4b8c4")
Note1.grid(row=0,column=1)

Note2= Frame(win,borderwidth = 1.5, width=300, height=350, bg="#66a9af")
Note2.grid(row=1,column=1)

Menu = Frame(win,borderwidth = 1.5, relief=RAISED, width=350, height=800, bg="#708090")
Menu.grid(row=0, rowspan=2, column=2)



#This is the code for the Top Right Frame to adress goal 1

Title1 = Frame(Goal1, width=275, height=230, bg="#a4b8c4")
Title1.grid(row=0,column=0)

Titledes1 = Label(Title1, text= "Brief Description of your goal", bg="#a4b8c4")
Titledes1.grid(row=0,column=0)

TitleText1 = Text(Title1, width=41, height=18,bg="#a4b8c4")
TitleText1.grid(row=1,column=0)

Finish1 = Button(Goal1,text= "I Reached my goal!",width=32, height = 4,command=GoalFinish1)
Finish1.grid(row=1,column=0)



#This is the code for the Bottom Left Frame to adress goal 2

Title2 = Frame(Goal2, width=275, height=235, bg="#66a9af")
Title2.grid(row=0,column=0)

Titledes2 = Label(Title2, text= "Brief Description of your goal",  bg="#66a9af")
Titledes2.grid(row=0,column=0)

TitleText2 = Text(Title2, width=41, height=18, bg="#66a9af")
TitleText2.grid(row=1,column=0)

Finish2 = Button(Goal2,text= "I Reached my goal!",width=32, height = 4, command = GoalFinish2)
Finish2.grid(row=1,column=0)

# Top midle frame for explaning goal 1

SideN1= Frame(Note1,width=275, height=230, bg="#a4b8c4")
SideN1.grid(row=0,column=0)

SideNDes = Label(SideN1,text="How will I accomplish this?",bg="#a4b8c4")
SideNDes.grid(row=0,column=0)

SideNtxt = Text(SideN1,width=41, height=18,bg="#a4b8c4")
SideNtxt.grid(row=1,column=0)

SideNsave = Button(Note1, text="Save to Hard Drive",width=32, height = 4)
SideNsave.grid(row=1,column=0)


#Bottom middle frame for explaining goal 2

SideN2= Frame(Note2,width=275, height=230,bg="#66a9af")
SideN2.grid(row=0,column=0)

SideNDes2 = Label(SideN2,text="How will I accomplish this?",bg="#66a9af")
SideNDes2.grid(row=0,column=0)

SideNtxt2 = Text(SideN2,width=41, height=18,bg="#66a9af")
SideNtxt2.grid(row=1,column=0)

SideNsave2 = Button(Note2, text="Save to Hard Drive",width=32, height = 4)
SideNsave2.grid(row=1,column=0)


#Program title+Client name Welcome

TitleName = Frame(Menu, width=330, height=125, bg="#708090")
TitleName.grid(row=0,column=0)

ProgramName = Label(TitleName,text="Goal Setter",bg="#708090" )
ProgramName.grid(row=0,column=0)
ProgramName.config(font=("Bebas Neue", 40))

Client = Label(TitleName,text="Wecome Back, David Bard!",bg="#708090")
Client.grid(row=1,column=0)
Client.config(font=("Montesserat",20))



#This is my Tip Selection. It uses a list of tips and picks a random one.

def tipplease():
    a = ["Remeber to foucs on one goal at a time! \n You will be overwhelmed and inefficient \n if you think about too many things at once!",
           "When trying to reach goals efficiently, Make \n sure to have a detailed plan to follow \n(Using this app of course:)", "Don't hurry too much when trying to \n accomplish a goal. A hurried goal is as good \n as no goal at all.",
             "Ask for help!, \n always remember you can count on friends \n and family to help!", "Setting goals can make your life more \n organized, so make sure to set and follow \n through with your goals on a daily basis!",
             "Invite friends to Set goals with you!, \n They will also find it very useful and fun. \n Plus, friends make everything better!", "Remember, goal setting is not a chore! \n set goals when you feel that you \n have something that you need to work on!"]
     

    TipText = Label(Tip,text=(random.choice(a)), bg="#708090")
    TipText.grid(row=1,column=0)
    
Tip = Frame(Menu, relief = SUNKEN, width=315, height=250,bg="#708090")
Tip.grid(row=2,column=0)

a = ["Remeber to foucs on only one goal at a time! \n You will get overwhelmed and will be inefficient \n if you think about too many things at once!",
           "When trying to reach a goal efficiently, Make \n sure to have a detailed plan to follow \n(Using this app of course:)", "Don't hurry too much when trying to \n accomplish a goal. A hurried goal is as good \n as no goal at all.",]
     

TipText = Label(Tip,text=(random.choice(a)), bg="#708090")
TipText.grid(row=1,column=0)

TipButton = Button(Tip,text="Another Tip",width=35, height=7,command=tipplease)
TipButton.grid(row=0,column=0)



                   



#Progress Bar Frame+Canvas2

ProgressBar = Frame(Menu,width=315, relief=SUNKEN, height=325,bg="#929a9b")
ProgressBar.grid(row=4,column=0)

progress = [0]

Goal = Label(ProgressBar, text = "Yearly Goal: \n Complete 30 Goals",bg="#929a9b")
Goal.grid(row=0,column=0)

ProgressB = Canvas(ProgressBar,  relief=SUNKEN, width = 300, height = 45, bg = "#66a9af")
ProgressB.grid(row = 1, column = 0)

Goal2 = Label(ProgressBar, text = "Monthly Goal: \n Complete 5 Goals",bg="#929a9b")
Goal2.grid(row=2,column=0)

ProgressB2 = Canvas(ProgressBar,  relief=SUNKEN, width = 300, height = 45, bg = "#66a9af")
ProgressB2.grid(row = 3, column = 0)

Instructions = Frame(Menu, height=275, width=315,bg="#708090")
Instructions.grid(row=6,column=0)

Instruction = Label(Instructions, text="This is a Goal Tracking App.  On the left, feel \n free  to  add your goals, and specify how they \n will be done. Above, Notice the Progress  \n tracking bar and the tip generator to \n aide you in  acheving your goals!\n \n for any furthur inquiries or issue, please email \n Kevin.Han@ucc.on.ca, or call 416-783-3857", bg="#929a9b")
Instruction.pack(side=BOTTOM)





#Invisible frames to space menubar out

Spacer1=Frame(Menu, width= 350, height=7,bg="#708090")
Spacer1.grid(row=1, column=0)

Spacer2 = Frame(Menu,width = 250, height=25,bg="#708090")
Spacer2.grid(row=3,column=0)

Spacer3 = Frame(Menu,width = 250, height=25,bg="#708090")
Spacer3.grid(row=5,column=0)

Spacer3 = Frame(Menu,width = 250, height=25,bg="#708090")
Spacer3.grid(row=7,column=0)

Logout = Button(Menu, text="Logout", width=35, height=5,command=UserLogout)
Logout.grid(row=8,column=0)


win.mainloop()



















