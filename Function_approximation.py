# Laboratory Work 2.3
# Function Approximation and Interpolation
# Performed by: Ulyana Yunusova BIB2206

# Node Numbers:  1 3 5 7 9 10 13
# Function Number: f1(x)
# Approximation Nodes: -5 -4 -3 -2 -1 -0.5 1
# Function Values at Nodes: 1.38 1.511 1 0.976 0.599 0.192 -0.405

import tkinter as tk
from tkinter import*
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
import sys

class Aproximator():
    def __init__(self):

        self.root=Tk()
        self.root.geometry("400x400")
        self.root.resizable(0,0)
        self.root.title("Апроксимация")
        
        self.frame_up,self.frame_down,self.frame_button_approks=self.create_frames()
        self.text_title,self.label_up,self.text_up,self.label_down,self.text_down = self.create_labeles()
        self.ButtonApproximate=self.create_button_approks()

        
        
    def create_frames(self):
        frame1=tk.Frame(self.root,width=500,height=500,bg='blue')
        frame1.pack(padx=20,pady=20)
        frame2=tk.Frame(self.root,width=500,height=500,bg='blue')
        frame2.pack(padx=20,pady=20)
        frame3=tk.Frame(self.root,width=500,height=500,bg='blue')
        frame3.pack(padx=20,pady=20)
        return frame1,frame2,frame3

    def create_labeles(self):
        label1=tk.Label(self.frame_up,text="Лобаротароная работа 2.3 \n Апроксимация и интерполяция функций \n Выполнил: Юнусова Ульяна БИБ2206",font=('Arial',10))
        label1.pack(expand=True,fill='both')
        
        label2=tk.Label(self.frame_up,text="Введите значения узлов",font=('Arial',10))
        label2.pack(expand=True,fill='both')
        
        label3=tk.Text(self.frame_up,height=1,width=50,font=('Arial',20,'bold'))
        label3.pack(expand=True,fill='both')
        
        label4=tk.Label(self.frame_down,text="Введите значения функции",font=('Arial',10))
        label4.pack(expand=True,fill='both')
        
        label5=tk.Text(self.frame_down,height=1,width=50,font=('Arial',20,'bold'))
        label5.pack(expand=True,fill='both')
        
        return label1,label2,label3,label4,label5

    def create_button_approks(self):
        btn=tk.Button(self.frame_button_approks,text='Апроксимировать\n функцию',font=('Arial',10),height=20,width=50, command=lambda:self.Approximation(1))
        btn.pack(expand=True,fill='both')
        
        return btn

    def Approximation(self,flag):
        if(flag==1):
            x,y=self.get_inputs()
            
            polynomial=np.poly1d(np.polyfit(x,y,1))
            y1=polynomial(x)
            
            polynomial=np.poly1d(np.polyfit(x,y,2))
            y2=polynomial(x)
            
            polynomial=np.poly1d(np.polyfit(x,y,3))
            y3=polynomial(x)
            
            buf,chart=plt.subplots()
            
            chart.plot(x,y,x,y1,x,y2,x,y3)
            
            chart.legend(['График Шаблонной функции',
                        'График Линейной апроксимации',
                        'График Квадратичной апроксимации',
                        'График Кубической апроксимации'])
            chart.set(xlabel='Значения узлов: Xi',ylabel='Значение функции: y=f1(Xi)',title='Апроксимация функции')
            chart.grid()
            
            plt.show()
        
        

    def get_inputs(self):
        
        x,y=self.text_up.get('1.0',END),self.text_down.get('1.0',END)
        x=[float(el)for el in x.split()]  
        y=[float(el)for el in y.split()]

        if((len(x)==0)or(len(y)==0)):
            self.error()
        return x,y
        
            

    def error(self):
        self.frame_error=tk.Tk()
        self.frame_error.title("Ошибка")
        self.frame_error.geometry("250x200")
        self.frame_error.resizable(0,0)
        lbl=tk.Label(self.frame_error,text='Ошибка: \n Вы не ввели значения \nx или y\n Bведите новые значения',font=('Ariel',14))
        lbl.pack(expand=True,fill='both')
        btn=tk.Button(self.frame_error,text='OK',font=('Ariel',14), command=lambda:self.frame_error.destroy())
        btn.pack(expand=True,fill='both')
        self.frame_error.mainloop()

    def run(self):
        self.root.mainloop()

if __name__=='__main__':
    Application=Aproximator()
    Application.run()
