from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมหา VAT ของ 500')
GUI.geometry('500x400')
Grand = 500

L1 = Label(GUI,text='VAT ของ 500',font=('Angsana New',30),fg='green')
L1.place(x=100,y=20)
def Button1(): #ฟังก์ชัน
    text = f'{(Grand*5)/105:,.2f}'
    messagebox.showinfo('Vat 5%',text)
    
FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B1 = ttk.Button(FB1,text='5%', command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2(): #ฟังก์ชัน
    text = f'{(Grand*7)/107:,.2f}'
    messagebox.showinfo('Vat 7%',text)
    
FB2 = Frame(GUI)
FB2.place(x=100,y=200)
B2 = ttk.Button(FB2,text='7%', command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3(): #ฟังก์ชัน
    text = f'{(Grand*10)/110:,.2f}'
    messagebox.showinfo('Vat 10%',text)
    
FB3 = Frame(GUI)
FB3.place(x=100,y=300)
B3 = ttk.Button(FB3,text='10%', command=Button3)
B3.pack(ipadx=20,ipady=20)
GUI.mainloop()
