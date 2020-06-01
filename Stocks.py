import tkinter as tk
import yfinance

class StockWindow:
    def __init__(self,master,number):
        
        self.master = master
        self.frame=tk.Frame(self.master)
        self.frame.pack()
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        self.master.overrideredirect(1)
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.focus_set() # <-- move focus to this widget
        self.master.bind("<Escape>", lambda e: e.widget.quit())
        #################################################
        ## Labels
        self.amountChanged = tk.Label(self.master,text = "$1000")
        self.amountChanged.place(x=w/2,y=h/2)
       
        
        self.marketChange = tk.Label(self.master,text = "Alot!")
        self.marketChange.place(x=23,y=66)
        self.stockNews = tk.Label(self.master,text = "News Here!")
        self.stockNews.place(x=23,y=234)
        self.stockNewds = tk.Label(self.master,text = "News Hewewere!")
        self.stockNewds.place(x=300,y=300)
        ## Buttons
        self.seeAllStocks = tk.Button(self.master,text ="do you wanna see more stocks?")
        self.seeAllStocks.place(x=0,y=0)
        self.goBack =tk.Button(self.master,text = "Go back",command=self.close_windows)
        self.goBack.place(x=100,y=100)
        
        
        ## LabelFrame
        self.newsLabelFrame = tk.LabelFrame(self.master)
        self.newsLabelFrame.place(relx=.4,rely=.3,height,width)
        for x in range(3):
            createNews("Justin Bieber Straight?", "Is he straight? find out!")


        #########
    def createNews(self,articleName,description):
        newsLabel = tk.Label(self.newsLabelFrame,text=articleName+" "+description)
        newsLabel.pack()
    def createStock(self,name,pricechange,placement):
        stockframe = tk.LabelFrame(self.master,text='')
        #stockframe.size(200)
        stockframe.place(relx=.5,rely=.5,height=10,width=10) 
        #stockframe.pack(expand='yes',fill='both')
        #stockframe.grid(column=5,row=5)
        tempLabel = tk.Label(stockframe,text=name)
    
        tempLabel.pack()
    def close_windows(self):
        self.master.destroy()

