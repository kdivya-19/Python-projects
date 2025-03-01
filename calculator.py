
from tkinter import *

class Calculator:
    def __init__(self,master):
        master.title("calculator")
        master.geometry("357x350+0+0")
        master.config(bg="gray")
        master.resizable(False,False)
        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17,bg='#fff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)
        

        Button(width=11,height=3,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0,y=50,)
        Button(width=11,height=3,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=11,height=3,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11,height=3,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=100)
        Button(width=11,height=3,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=100)
        Button(width=11,height=3,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=100)
        Button(width=11,height=3,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=150)
        Button(width=11,height=3,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=150)
        Button(width=11,height=3,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180,y=150)
        Button(width=11,height=3,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=200)
        Button(width=11,height=3,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=90,y=200)
        Button(width=11,height=3,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=180,y=200)
        Button(width=11,height=3,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=250)
        Button(width=11,height=3,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=50)
        Button(width=11,height=3,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=100)
        Button(width=11,height=3,text='*',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270,y=150)
        Button(width=11,height=3,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=200)
        Button(width=11,height=3,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=0,y=250)
        Button(width=11,height=3,text='c',relief='flat',bg='white',command=self.clear).place(x=180,y=250)
        Button(width=11,height=3,text='=',relief='flat',bg='white',command=self.solve).place(x=270,y=250)
    
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
        

    def clear(self):

        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)  # Evaluate the mathematical expression
        self.equation.set(result)
        
window=Tk()
calculator=Calculator(window)
window.mainloop()
                
