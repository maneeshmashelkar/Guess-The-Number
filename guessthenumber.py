from tkinter import *
root=Tk()
root.title("GUESS THE NUMBER!")
result=0

def card1():
    mainframe.destroy()
    global row1,row2,row3,row4,row5,msg,card1frame

    row1=Label(root,text="  1     3     5  ",relief=GROOVE,font=("Verdana","20","bold"))
    row1.pack()
    row2=Label(root,text=" 7     9     11 ",relief=GROOVE,font=("Verdana","20","bold"))
    row2.pack()
    row3=Label(root,text="13    15    17",relief=GROOVE,font=("Verdana","20","bold"))
    row3.pack()
    row4=Label(root,text="19    21    23",relief=GROOVE,font=("Verdana","20","bold"))
    row4.pack()
    row5=Label(root,text="25    27    29",relief=GROOVE,font=("Verdana","20","bold"))
    row5.pack()

    msg=Label(root,text="->your picked Number is Present in given numbers \n then click 'Yes' else 'No'?",font=("Verdana","12","normal"))
    msg.pack()

    card1frame=Frame(root)
    card1frame.pack(side=BOTTOM)
    card1no=Button(card1frame,text=" No ",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=card2)
    card1no.pack(side=LEFT)
    card1yes=Button(card1frame,text="Yes",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:[card2(),guess(1)])
    card1yes.pack(side=RIGHT)


def card2():
    global row1,row2,row3,row4,row5,card1frame,card2frame
    card1frame.destroy()
    row1["text"]=" 2     3     6   "
    row2["text"]=" 7    10    11 "
    row3["text"]="14    15    18"
    row4["text"]="19    22    23"
    row5["text"]="26    27    30"
    card2frame=Frame(root)
    card2frame.pack(side=BOTTOM)
    card2no=Button(card2frame,text=" No ",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=card3)
    card2no.pack(side=LEFT)
    card2yes=Button(card2frame,text="Yes",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:[card3(),guess(2)])
    card2yes.pack(side=RIGHT)


def card3():
    global row1,row2,row3,row4,row5,card2frame,card3frame
    card2frame.destroy()
    row1["text"]="  4     5     6  "
    row2["text"]=" 7    12    13 "
    row3["text"]="14    15    20"
    row4["text"]="21    22    23"
    row5["text"]="28    29    30"
    card3frame=Frame(root)
    card3frame.pack(side=BOTTOM)
    card3no=Button(card3frame,text=" No ",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=card4)
    card3no.pack(side=LEFT)
    card3yes=Button(card3frame,text="Yes",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:[card4(),guess(4)])
    card3yes.pack(side=RIGHT)
    

def card4():
    global row1,row2,row3,row4,row5,card3frame,card4frame
    card3frame.destroy()
    row1["text"]=" 8     9     10 "
    row2["text"]="11    12    13"
    row3["text"]="14    15    24"
    row4["text"]="25    26    27"
    row5["text"]="28    29    30"
    card4frame=Frame(root)
    card4frame.pack(side=BOTTOM)
    card4no=Button(card4frame,text=" No ",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=card5)
    card4no.pack(side=LEFT)
    card4yes=Button(card4frame,text="Yes",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:[card5(),guess(8)])
    card4yes.pack(side=RIGHT)


def card5():
    global row1,row2,row3,row4,row5,card4frame,card5frame
    card4frame.destroy()
    row1["text"]="16    17    18"
    row2["text"]="19    20    21"
    row3["text"]="22    23    24"
    row4["text"]="25    26    27"
    row5["text"]="28    29    30"
    card5frame=Frame(root)
    card5frame.pack(side=BOTTOM)
    card5no=Button(card5frame,text=" No ",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=resultcard)
    card5no.pack(side=LEFT)
    card5yes=Button(card5frame,text="Yes",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:[guess(16),resultcard()])
    card5yes.pack(side=RIGHT)
    

def guess(guessvalue):
    global result
    result=result+guessvalue
    

def resultcard():
    global row1,row2,row3,row4,row5,msg,card5frame,result,resultframe,note
    msg.destroy()
    row1.destroy()
    row2.destroy()
    row3.destroy()
    row4.destroy()
    row5.destroy()
    card5frame.destroy()
    
    resultframe=Frame(root)
    resultframe.pack()
    var = StringVar()
    var1 = StringVar()
    resultmsg = Label(resultframe, textvariable=var ,font=("Verdana","15","normal"))
    var.set("         Your Picked value is :         ")
    resultmsg.pack(side=TOP)
    resultvalue = Label(resultframe, textvariable=var1,font=("Verdana","15","normal"))
    if result>=31:
        var1.set("unknow value")
        note=Label(root,text="NOTE:- unknown value ->value is out of range \n try again",font=("Verdana","10","normal"))
        note.pack(side=BOTTOM)
    else: 
        var1.set(str(result))
        note=Label(root,text="Let`s Try with different number!",font=("Verdana","10","normal"))
        note.pack(side=BOTTOM)
    resultvalue.pack()

    tryagain=Button(resultframe,text="Try Again",relief=GROOVE,bd=4,font=("Verdana","15","normal"),command=lambda:restart())
    tryagain.pack(pady=8)


def restart():
    global resultframe,note,result
    note.destroy()
    resultframe.destroy()
    result=0
    main()


def main():
    global mainframe
    mainframe=Frame(root)
    mainframe.pack()

    var = StringVar()
    maincard = Label(mainframe, textvariable=var,font=("Verdana","15","bold"))
    var.set("Pick Any Number From 1 - 30 ! \n \n 1     2     3     4     5 \n 6     7     8     9    10\n 11   12   13   14   15 \n 16   17   18   19   20 \n 21   22   23   24   25 \n 26   27   28   29   30 \n")
    maincard.pack()

    mainbutton=Button(mainframe,text="Ready",relief=GROOVE,bd=4,command=card1,font=("Verdana","15","normal"))
    mainbutton.pack()

main()

root.mainloop()