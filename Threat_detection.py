import tkinter as tk
import random as rnd

class Finding_threats:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x750')
        self.window.resizable(0,0)
        self.window.title('Finding threats')
        
        self.threat = {'а':(0,1), 'и':(0,2),'п':(0,3),'о':(0,4),
                       'р':(1,1), 'ж':(1,2), 'ъ':(1,3), 'с':(1,4),
                       'г':(2,1), 'ц':(2,2), 'х':(2,3), 'ч':(2,4),
                       'к':(3,1), 'ы':(3,2), 'з':(3,3), 'я':(3,4),
                       }
        
        self.alf = ['а','б', 'в', 'г', 'в', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ','ъ','ы','ь', 'э', 'ю', 'я']
        self.mas = []
        self.count = 0    
        
        self.total_expression = 'Нажмите "Создать массив"'
        self.current_expression = ''
        
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        self.total_label, self.label = self.create_display_labels()
        
        self.create_threat_buttons()
        self.create_mas_button()
        self.create_found_button()
        self.create_clear_button()
        
        for i in range(1,5):
            self.buttons_frame.rowconfigure(i, weight = 1)
            self.buttons_frame.columnconfigure(i, weight = 1)
    
    def create_threat_buttons(self):
        for threat, grid_value in self.threat.items():
            button = tk.Button(self.buttons_frame, text = str(threat), bg='white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = lambda x=threat: self.add_to_expression(x))
            button.grid(row=grid_value[0], column = grid_value[1], sticky=tk.NSEW)
     
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg='#F5F5F5')
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
            
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.update_total_label()
        self.mas = []
         
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='Очистить', bg = '#F5F5F5', fg = 'black', font=('Arial', 16, 'bold'), borderwidth = 0, command = self.clear)
        button.grid(row=5, column = 1,columnspan = 4,  sticky = tk.NSEW, ipady=15)
           
    def create_mas(self):
        
        for i in range(rnd.randint(8,50)):
            self.mas.append(rnd.choice(self.alf)+rnd.choice(self.alf)+rnd.choice(self.alf)+rnd.choice(self.alf))
        print(self.mas)
        self.current_expression = 'Введите угрозу'
        self.total_expression = 'Массив сформирован!'

        self.update_label()
        self.update_total_label()
        
        self.current_expression = ''
        self.total_expression = ''
    
    def create_mas_button(self):
        button = tk.Button(self.buttons_frame, text='Создать массив', bg = '#F5F5F5', fg = 'black', font=('Arial', 16, 'bold'), borderwidth = 0, command= self.create_mas)
        button.grid(row=4, column = 3, columnspan = 2, sticky = tk.NSEW)
            
    def found(self):
        
        self.total_expression += str(self.current_expression)
        self.update_total_label()
        self.count = 0
        
        for i in self.mas:
            if self.total_expression in i:
                self.count += 1
        print(f' "{self.total_expression}": {self.count}')
        
        if self.count == 0 and len(self.mas)!= 0:
            self.total_expression = 'Введите др.угрозу:'
            self.current_expression = 'Угроз не обнаружено'
        elif len(self.mas)== 0:
            self.total_expression = 'Сформируйте массив'
            self.current_expression = ''
        else:
            self.total_expression = 'Количество угроз: ' + str(self.count)
            self.current_expression = 'Введите новую угрозу'
            
        self.count = 0
    
        self.update_label()
        self.update_total_label()
        
        self.current_expression = ''
        self.total_expression = ''
         
    def create_found_button(self):
        button = tk.Button(self.buttons_frame, text='Найти кол-во угроз', bg = '#F5F5F5', fg = 'black', font=('Arial', 16, 'bold'), borderwidth = 0, command= self.found)
        button.grid(row=4, column = 1, columnspan = 2 ,sticky = tk.NSEW)
     
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = '#F5F5F5', fg = 'black', padx = 24, font=('Arial', 16, 'bold'))
        total_label.pack(expand = True, fill = 'both')
        
        label = tk.Label(self.display_frame, text = self.current_expression,anchor = tk.E, bg='#F5F5F5', fg = 'black',padx = 24, font = ('Arial', 16, 'bold'))
        label.pack(expand = True, fill = 'both')
        return total_label, label
    
    def add_to_expression(self, value):
        
        self.current_expression += str(value)
        self.update_label()
        
    def update_total_label(self):
        self.total_label.config(text = self.total_expression)
        
    def update_label(self):
        self.label.config(text = self.current_expression)
     
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":    
    calc = Finding_threats()
    calc.run()



