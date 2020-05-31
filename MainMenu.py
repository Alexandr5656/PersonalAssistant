import tkinter as tk
import Stocks
class MainMenu:
    def __init__(self,master):
        self.master = master
        self.master.geometry("400x400")
        self.frame=tk.Frame(self.master)     

        #####################           FullScreen           ###################
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        self.master.overrideredirect(1)
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.focus_set() # <-- move focus to this widget
        self.master.bind("<Escape>", lambda e: e.widget.quit())#Quits when escape is pressed
        
        for i in range(3):
            self.master.columnconfigure(i, weight=1, minsize=75)
            self.master.rowconfigure(i, weight=1, minsize=50)
    
            for j in range(0, 3):
                self.butnew("ji","g",Stocks.StockWindow,i,j)
        self.frame.pack()

    def butnew(self,text,number,_class,i,j):
        sizeWidth = int(self.master.winfo_screenwidth()/3)
        sizeHeight = int(self.master.winfo_screenheight()/3)
        pixel = tk.PhotoImage(width=1, height=1)
        btn = tk.Button(self.frame,
                  text = text,
                  image=pixel,#If i comment out this line it works
                  width=sizeWidth,
                  height=sizeHeight,
                  compound="center",
                  command= lambda: self.new_window(number,_class))
        btn.grid(row=i,
                 column=j,
                 padx =0,
                 pady=0)
        btn.photo = pixel

    def new_window(self,number,_class):
        self.new = tk.Toplevel(self.master)
        _class(self.new,number)




root = tk.Tk()
app = MainMenu(root)
root.mainloop()