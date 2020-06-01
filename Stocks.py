import tkinter as tk
import yfinance
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


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
        
        
        ## News Articles
        self.newsLabelFrame = tk.LabelFrame(self.master)
        self.newsLabelFrame.place(relx=.4,rely=.3,height = int(h/2),width=int(w/3))
        for x in range(3):
            self.createNews("Justin Bieber Straight?", "Is he straight? find out!")
        for y in range(5):
            self.createStock("sg","sg",y)
        ## Graph
        #self.Graph = tk.LabelFrame(self.master)
        #self.Graph.place(relx=.4,rely=.2,height = int(h/6),width=int(w/3))
        #self.stockFigure = Figure(figsize = (5,5),dpi=100)
        #self.plotting = self.stockFigure.add_subplot(111)
        #self.plotting.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        #self.canvas = FigureCanvasTkAgg(self.stockFigure,self)
        #self.canvas.show()
        #self.canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand = True)
        




        #########
    def createNews(self,articleName,description,rowItsIn):
        newsLabel = tk.Label(self.newsLabelFrame,text=articleName+" "+description)
        newsLabel.pack()
    def createStock(self,name,pricechange,placement):
        stockframe = tk.LabelFrame(self.master,text='')
        stockframe.place(relx=.1,y=50+(rowItsIn*10),height=50,width=50) 
        tempLabel = tk.Label(stockframe,text=name)
        tempLabel.pack()
    
        tempLabel.pack()
    def close_windows(self):
        self.master.destroy()

