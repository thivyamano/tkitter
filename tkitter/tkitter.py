from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time
import mysql.connector

count=0
text=''

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'  Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)
    
root=Tk()
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.configure(height=h,width=w,bg='#ffc8dd')
root.title('Student Management System')
datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

studentLabel=Label(root,text='Student Management System',font=('arial',30,'italic bold'),bg='#ffc8dd',width=30)
studentLabel.place(x=300,y=5)


leftFrame=Frame(root,bg='#fcd5ce',bd=10,relief=GROOVE)
leftFrame.place(x=50,y=80,width=300,height=500)



lbl=Label(leftFrame,text='STUDENT PROFILE',font=('verdana',10,'bold'),bd=10,relief=GROOVE,bg='#adc178',fg='#5B2333')
lbl.place(x=0,y=80)
lb2=Label(leftFrame,text='Roll No:',font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb2.place(x=1,y=130)

lb3=Label(leftFrame,text='Name:',font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb3.place(x=2,y=190)
lb4=Label(leftFrame,text='D.O.B:',font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb4.place(x=2,y=260)
lb5=Label(leftFrame,text='Gender:',font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb5.place(x=2,y=330)
lb6=Label(leftFrame,text='Nationlity:',font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb6.place(x=2,y=400)
ent1=Entry(leftFrame,font=('verdana',8),bd=10,relief=GROOVE,fg='black')
ent1.place(x=90,y=130)
ent2=Entry(leftFrame,font=('verdana',8),bd=10,relief=GROOVE,fg='black')
ent2.place(x=90,y=190)
ent3=Entry(leftFrame,font=('verdana',8),bd=10,relief=GROOVE,fg='black')
ent3.place(x=90,y=260)
ent4=Entry(leftFrame,font=('verdana',8),bd=10,relief=GROOVE,fg='black')
ent4.place(x=90,y=330)
ent5=Entry(leftFrame,font=('verdana',8),bd=10,relief=GROOVE,fg='black')
ent5.place(x=100,y=400)
'''
data=('Female','Male','others')
Var1=StringVar()
Var1.set('Select the Gender')
opt=OptionMenu(leftFrame,Var1,*data)
opt.place(x=90,y=330,width=160)

data=('Indian','USA','Others')
Var2=StringVar()
Var2.set('Select Nationality')
opt=OptionMenu(leftFrame,Var2,*data)
opt.place(x=100,y=400,width=160)
'''


def show():
    print(ent1.get())
    print(ent2.get())
    print(ent3.get())
    print(ent4.get())
    print(ent5.get())
    print(ent6.get())
    print(ent7.get())


middleFrame=Frame(root,bg='#ffc2d1',bd=12,relief=GROOVE)
middleFrame.place(x=350,y=80,width=320,height=500)
lb7=Label(middleFrame,text='REPORTS',font=('verdana',15,'bold'),bd=10,relief=GROOVE,bg='#9f86c0',fg='#5B2333')
lb7.place(x=70,y=20)

lb8=Label(middleFrame,text='SUBJECTS AND MARKS',font=('verdana',10,'bold'),bd=10,relief=GROOVE,bg='#adc178',fg='#5B2333')
lb8.place(x=0,y=80)
lb9=Label(middleFrame,text='English:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb9.place(x=1,y=130)
lb10=Label(middleFrame,text='Tamil:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb10.place(x=1,y=180)
lbl1=Label(middleFrame,text='Maths:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lbl1.place(x=1,y=230)
lbl2=Label(middleFrame,text='Total:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lbl2.place(x=1,y=280)
lb13=Label(middleFrame,text='Average:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lb13.place(x=1,y=330)
lbl4=Label(middleFrame,text='Grade:',width=10,font=('verdana',8,'bold'),bd=10,relief=GROOVE,bg='#55D6BE',fg='#2B2D42')
lbl4.place(x=1,y=380)

Englishvalue=StringVar()
Tamilvalue=StringVar()          
Mathsvalue=StringVar()

ent9=Entry(middleFrame,textvariable=Englishvalue,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent9.place(x=130,y=130)
ent10=Entry(middleFrame,textvariable=Tamilvalue,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent10.place(x=130,y=180)
ent11=Entry(middleFrame,textvariable=Mathsvalue,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent11.place(x=130,y=230)
ent12=Entry(middleFrame,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent12.place(x=130,y=280)

ent13=Entry(middleFrame,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent13.place(x=130,y=330)

ent14=Entry(middleFrame,font=('verdana',8),bd=10,relief=GROOVE,width=15,fg='black')
ent14.place(x=130,y=380)


def calculation():
    English=int(ent9.get())
    Tamil=int(ent10.get())
    Maths=int(ent11.get())
    totalvalue=StringVar()
    totalvalue=(English+Tamil+Maths)
    ent12.insert(0,totalvalue)
    averagevalue=StringVar()
    averagevalue=int(totalvalue/3)
    ent13.insert(0,averagevalue)
    if (averagevalue>50):
        grade="PASS"
    else:
        grade="FAIL"
    ent14.insert(0,grade)
    
        
          
Button(middleFrame,text="calculate",font=('verdana',8),bd=10,relief=GROOVE,width=15,bg='green',command=calculation).place(x=90,y=430)


#treeview
RightFrame=Frame(root)

RightFrame.place(x=670,y=80,width=850,height=500)



scrollBarX=Scrollbar(RightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(RightFrame,orient=VERTICAL)




Table=ttk.Treeview(RightFrame,columns=('RollNo','Name','D.O.B','Gender','Nationlity','English','Tamil','Maths','Total','Average','Grade'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
Table.column('RollNo',width=80)
Table.column('Name',width=100)
Table.column('D.O.B',width=100)

Table.column('Gender',width=100)
Table.column('Nationlity',width=100)
Table.column('English',width=80)
Table.column('Tamil',width=80)
Table.column('Maths',width=80)
Table.column('Total',width=80)
Table.column('Average',width=80)
Table.column('Grade',width=80)

scrollBarX.config(command=Table.xview)
scrollBarY.config(command=Table.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

Table.pack(fill=BOTH,expand=1)

Table.heading('RollNo',text='RollNo')
Table.heading('Name',text='Name')
Table.heading('D.O.B',text='D.O.B')
Table.heading('Gender',text='Gender')
Table.heading('Nationlity',text='Nationlity')
Table.heading('English',text='English')
Table.heading('Tamil',text='Tamil')
Table.heading('Maths',text='Maths')
Table.heading('Total',text='Total')
Table.heading('Average',text='Average')
Table.heading('Grade',text='Grade')

Table.config(show='headings')


data=(('101','Thivya','11.04.1996','femle','Indian','96','87','76','256','86','PASS'),('102','Kavitha','11.08.1995','femle','Indian','56','45','35','136','45','FAIL'),('103','Anitha','15.05.1996','femle','Indian','65','56','86','207','69','PASS'))

count=0
for i in data:
    Table.insert(parent='',index='end',iid=count,value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
    count+=1
   
def add_data():
    global count
    if ent1.get()!="":
        if ent1.get()>="0" and ent1.get()<="9":
            if ent2.get()!="":
                if ((ent2.get()>="A" and ent2.get()<="Z") or (ent2.get()>="a" and ent2.get()<="z")):
                    if ent3.get!="":
                        if ent3.get()>="0" and ent3.get()<="9":
                            if len(ent3.get())==10:
                                if ent4.get()!="":
                                    if ent5.get()!="":
                                        if (ent9.get()!="" and ent10.get()!="" and ent11.get()!=""):
                                            if (len(ent9.get())==2 and len(ent10.get())==2 and len(ent11.get())==2):
                                                if (ent12.get()!="" and ent13.get()!="" and ent14.get()!=""):
                                                    Table.insert(parent='',index='end',iid=count,value=(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get(),ent13.get(),ent14.get()))
                                                    count+=1
                                                    con=mysql.connector.connect(host='127.0.0.1',user='root',password='12345',db='students')
                                                    cur=con.cursor()
                                                    cur.execute("insert into profiles value('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get(),ent13.get(),ent14.get()))
                                                    con.commit()
                                                    ent1.delete(0,'end')
                                                    ent2.delete(0,'end')
                                                    ent3.delete(0,'end')
                                                    ent4.delete(0,'end')
                                                    ent5.delete(0,'end')
                                                    ent9.delete(0,'end')
                                                    ent10.delete(0,'end')
                                                    ent11.delete(0,'end')
                                                    ent12.delete(0,'end')
                                                    ent13.delete(0,'end')
                                                    ent14.delete(0,'end')
                                                    ent1.focus()
                                                     
                                                    
     
                                                    
                                                else:
                                                    messagebox.showinfo("Fields required","Press the calculate button")
                                            else:
                                                messagebox.showinfo("Fields required","Enter only 2 digit number")
                                        else:
                                            messagebox.showinfo("Fields required","Enter the subject marks")
                                    else:
                                        messagebox.showinfo("Fields required","Enter the Nationality")
                                else:
                                    messagebox.showinfo("Fields required","Enter the Gender")
                            else:
                                messagebox.showinfo("Fields required","Enter the correct 10 characters")
                        else:
                            messagebox.showinfo("Fields required","Enter only the numbers")
                    else:
                        messagebox.showinfo("Fields required","Enter the date of birth")
                else:
                    messagebox.showinfo("Fields required","Enter only the alphabets")
            else:
                messagebox.showinfo("Fields required","Enter the name")
        else:
            messagebox.showinfo("Fields required","Enter only numbers")
    else:
        messagebox.showinfo("Fields required","Enter the Rollno")
        
                                                    
                                            
     
        
buttonFrame=Frame(root,bd=10,relief=GROOVE,bg='#ffc2d1')

buttonFrame.place(x=45,y=600 ,width=930,height=100)

        
                                                        
    
but1=Button(buttonFrame,text='ADD DATA',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=add_data)
but1.place(x=4,y=14)
      
        
def sel_data():
     ent1.delete(0,'end')
     ent2.delete(0,'end')
     ent3.delete(0,'end')
     ent4.delete(0,'end')
     ent5.delete(0,'end')
     ent9.delete(0,'end')
     ent10.delete(0,'end')
     ent11.delete(0,'end')
     ent12.delete(0,'end')
     ent13.delete(0,'end')
     ent14.delete(0,'end')
     x=Table.selection()
     values=Table.item(x,'values')
     ent1.insert(0,values[0])
     ent2.insert(0,values[1])
     ent3.insert(0,values[2])
     ent4.insert(0,values[3])
     ent5.insert(0,values[4])
     ent9.insert(0,values[5])
     ent10.insert(0,values[6])
     ent11.insert(0,values[7])
     ent12.insert(0,values[8])
     ent13.insert(0,values[9])
     ent14.insert(0,values[10])



but3=Button(buttonFrame,text='SELECTED DATA',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=sel_data)
but3.place(x=150,y=14)

#UPdata button
def upd_data():
    sel=Table.focus()
    Table.item(sel,text='',value=(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get(),ent13.get(),ent14.get()))
    ent1.delete(0,'end')
    ent2.delete(0,'end')
    ent3.delete(0,'end')
    ent4.delete(0,'end')
    ent5.delete(0,'end')
    ent9.delete(0,'end')
    ent10.delete(0,'end')
    ent11.delete(0,'end')
    ent12.delete(0,'end')
    ent13.delete(0,'end')
    ent14.delete(0,'end')
    ent1.focus()

     
but4=Button(buttonFrame,text='UPDATE DATA',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=upd_data)
but4.place(x=300,y=14)

def clear_data():
     for i in Table.get_children():
          Table.delete(i)
but5=Button(buttonFrame,text='CLEAR DATA',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=clear_data)
but5.place(x=450,y=14)

def exit():
    root.destroy()
Button(buttonFrame,text='EXIT',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=exit).place(x=750,y=14)

def delete():
    for i in Table.selection()[0]:
        Table.delete(i)

Button(buttonFrame,text='DELETE',bd=10,relief=GROOVE,bg='#b0c7bd',width=15,cursor='hand2',command=delete).place(x=600,y=14)



        
    
root.mainloop()
