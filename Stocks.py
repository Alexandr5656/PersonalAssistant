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
        self.highestChangedStock = tk.Label(self.master,text = "Amzn")
        self.highestChangedStock.place(x=w/2+10,y=h/2+40)
        self.lowestChangedStock = tk.Label(self.master,text = "this one")
        self.stockTips = tk.Label(self.master,text = "Buy some")
        self.stockTips.place(x=2,y=777)
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
        self.createStock("afdhsfdhsfhsfghsgfhsdg",3,300)
        self.createStock("afdhsfdhsfhsfghsgfhsdg",3,300)
        #########
    def createStock(self,name,pricechange,placement):
        stockframe = tk.LabelFrame(self.frame,text='')
        #stockframe.size(200)
        #stockframe.place(x=400,y=400,height=10,width=10) 
        stockframe.pack(expand='yes',fill='both')
        tempLabel = tk.Label(stockframe,text=name)
        
        tempLabel.pack()
    def close_windows(self):
        self.master.destroy()

