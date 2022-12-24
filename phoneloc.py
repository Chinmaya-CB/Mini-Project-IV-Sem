import tkinter
from tkinter import *
from findloc import fcountry,fserprov,giveloc

def find():
    TextPanel.config(state=DISABLED)
    TextPanel.yview(END)
    phno=EntryPanel.get("1.0",'end-1c').strip()
    EntryPanel.delete("0.0",END)
    TextPanel.config(state=NORMAL)
    TextPanel.insert(END,"\nYour Inserted Phone number is "+ phno+'\n')
    
    country=fcountry(phno)
    service=fserprov(phno)
    TextPanel.config(state=NORMAL)
    TextPanel.insert(END,"\nDetails of the phone number:\n")
    TextPanel.insert(END,"\nCountry = " + country + '\n')
    TextPanel.insert(END,"\nService Provider = "+service+"\n")
    TextPanel.insert(END,"\nPlease open the HTML file\n")
    TextPanel.insert(END,"\"Mylocation.html\" to view the results\n")
    giveloc(phno)
    TextPanel.insert(END,"\n\nPlease Enter the phone number\n")
    TextPanel.config(state=DISABLED)
    TextPanel.yview(END)

EntryPage=Tk()
EntryPage.title("PhoneLOC")
EntryPage.geometry("550x700")
EntryPage.resizable(width=FALSE,height=FALSE)

TextPanel=Text(EntryPage,bd=0,bg="ivory",height="8",width="50",font="Centaur")
TextPanel.config(foreground="#442265",font=("Verdana",12))
TextPanel.insert(END,"Please Enter the phone number\n")

scroller=Scrollbar(EntryPage,command=TextPanel.yview,cursor="heart")
TextPanel['yscrollcommand']=scroller.set

sendicon=Button(EntryPage,font=("Garamond",16,'bold'),text="Enter",width="12",
                height=5,bd=0,bg="red",activebackground="white",fg='white',command= find )

EntryPanel=Text(EntryPage,bd=0,bg="#23e8ad",width="29",height="5",font="Arial")

scroller.place(x=520,y=6,height=556)
TextPanel.place(x=6,y=6,height=556,width=509)
EntryPanel.place(x=150,y=568,height=127,width=366)
sendicon.place(x=6,y=568,height=127)

EntryPanel.mainloop()
