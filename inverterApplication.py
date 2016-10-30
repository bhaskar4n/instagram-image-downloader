import wx
from math import*

class inverter(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"inverter",size=(700,750))
        self.panel=wx.Panel(self,-1)
        self.SetBackgroundColour("#b0e0e7")
        menu=wx.MenuBar()
        file_menu=wx.Menu()
        file_menu.Append(300,"Quit")
        self.Bind(wx.EVT_MENU,self.Quit,id=300)
        help_menu=wx.Menu()
        help_menu.Append(302,"About")
        self.Bind(wx.EVT_MENU,self.about,id=302)
        menu.Append(file_menu,"File")
        menu.Append(help_menu,"Help")
        self.SetMenuBar(menu)
        self.y=25
        self.i=0
        self.values=[]
        self.values2=[]
        self.total=0
        for i in range(20):
            self.y=self.y+30
            self.i=self.i+1
            inverter=wx.StaticText(self.panel,-1,"INVERTER SELECTION FOR YOUR HOME",pos=(240,10))
            watts=wx.StaticText(self.panel,-1,"watts",pos=(80,35))
            Nos=wx.StaticText(self.panel,-1,"Nos",pos=(150,35))
            load=wx.StaticText(self.panel,-1,"load",pos=(10,self.y))
            load1=wx.TextCtrl(self.panel,-1,"0",pos=(60,self.y),size=(60,20))
            load2=wx.StaticText(self.panel,-1,str(self.i),pos=(40,self.y))
            load3=wx.TextCtrl(self.panel,-1,"1",pos=(130,self.y),size=(60,20))
            self.values.append(load1)
            self.values2.append(load3)

        load4=wx.StaticText(self.panel,-1,"power factor",pos=(200,55))
        self.load5=wx.TextCtrl(self.panel,-1,"0.7",pos=(280,55),size=(50,20))
        load6=wx.StaticText(self.panel,-1,"battery volt",pos=(200,85))
        self.load7=wx.TextCtrl(self.panel,-1,"12",pos=(280,85),size=(50,20))
        self.load8=wx.StaticText(self.panel,-1,"backup time",pos=(200,115))
        self.load9=wx.TextCtrl(self.panel,-1,"3",pos=(280,115),size=(50,20))
        self.load10=wx.StaticText(self.panel,-1,"total power you need",pos=(200,175))
        self.load11=wx.TextCtrl(self.panel,-1,"0",pos=(330,175),size=(50,20))
        self.load12=wx.StaticText(self.panel,-1,"watts",pos=(390,175))
        self.load13=wx.StaticText(self.panel,-1,"Required VA of inverter",pos=(200,205))
        self.load14=wx.TextCtrl(self.panel,-1,"0",pos=(330,205),size=(70,20))
        self.load15=wx.StaticText(self.panel,-1,"battery capacity",pos=(200,235))
        self.load16=wx.TextCtrl(self.panel,-1,"0",pos=(330,235),size=(50,20))
        self.load17=wx.StaticText(self.panel,-1,"Ampere Hrs",pos=(390,235))
        self.load18=wx.StaticText(self.panel,-1,"VA",pos=(410,205))
        default="Note: default values must be load = 0 Watts and Nos = 1,\n don't empty the text box"
        self.load19=wx.StaticText(self.panel,-1,str(default),pos=(200,300))
        self.load20=wx.StaticText(self.panel,-1,"Hrs",pos=(340,115))
        self.load21=wx.StaticText(self.panel,-1,"V",pos=(340,85))
        wx.Button(self.panel,201,"Enter",pos=(240,145),size=(70,30))
        self.Bind(wx.EVT_BUTTON,self.Enter,id=201)
        # reference table
        self.reference_table=wx.StaticText(self.panel,-1,"LOAD REFERENCE TABLE",pos=(350,350))
        self.ln = wx.StaticLine(self.panel, -1, style=wx.LI_HORIZONTAL,pos=(250,368))
       
       # print self.ln.IsVertical()
        self.reference_table=wx.StaticText(self.panel,-1,"DEVICE",pos=(250,375))
        self.reference_table=wx.StaticText(self.panel,-1,"WATTS",pos=(450,375))
        self.ln1 = wx.StaticLine(self.panel, -1, style=wx.LI_HORIZONTAL,pos=(250,395))
        self.ln2 = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL,pos=(400,350))
        self.ln3 = wx.StaticLine(self.panel, -1, style=wx.LI_HORIZONTAL,pos=(250,575))

        self.reference_table=wx.StaticText(self.panel,-1,"Coffee maker",pos=(250,400))
        self.reference_table=wx.StaticText(self.panel,-1,"Ceiling fan",pos=(250,425))
        self.reference_table=wx.StaticText(self.panel,-1,"Window fan",pos=(250,450))
        self.reference_table=wx.StaticText(self.panel,-1,"Heater(portable)",pos=(250,475))
        self.reference_table=wx.StaticText(self.panel,-1,"CPU(awake/asleep)",pos=(250,500))
        self.reference_table=wx.StaticText(self.panel,-1,"Monitor(awake/asleep)",pos=(250,525))
        self.reference_table=wx.StaticText(self.panel,-1,"Laptop",pos=(250,550))

        self.reference_table=wx.StaticText(self.panel,-1,"900-1200",pos=(450,400))
        self.reference_table=wx.StaticText(self.panel,-1,"65-175",pos=(450,425))
        self.reference_table=wx.StaticText(self.panel,-1,"55-250",pos=(450,450))
        self.reference_table=wx.StaticText(self.panel,-1,"750-1500",pos=(450,475))
        self.reference_table=wx.StaticText(self.panel,-1,"120/30 or less",pos=(450,500))
        self.reference_table=wx.StaticText(self.panel,-1,"150/30 or less",pos=(450,525))
        self.reference_table=wx.StaticText(self.panel,-1,"50-100",pos=(450,550))

        self.ln.SetSize((300,2))
        self.ln1.SetSize((300,2))
        self.ln2.SetSize((2,225))
        self.ln3.SetSize((300,2))


    def Enter(self,event):
        self.a=[]
        for i in range(20):
            # total power you need caculation
            self.power=(float(self.values[i].GetValue())*float(self.values2[i].GetValue()))
            self.a.append(self.power)
            self.total=self.total+self.a[i]
            # required VA of inverter calculation
        self.required_VA_of_inverter=(self.total)/(float(self.load5.GetValue()))
        # battery capacity calculation
        self.battery=(float(self.load7.GetValue()))
        self.backup=(float(self.load9.GetValue()))
        self.battery_capacity=((self.total)*(self.backup))/(self.battery)
        # output display
        self.load11.SetValue(str(self.total))
        self.load14.SetValue(str(round(self.required_VA_of_inverter)))
        self.load16.SetValue(str(self.battery_capacity))
        self.total=0
        self.battery_capacity=0
        self.require_VA_of_inverter=0
        
    def Quit(self,event):
        self.Close()
    def about(self,event):
        self.about=wx.AboutDialogInfo()
        self.about.SetName("INVERTER SELECTION")
        self.about.SetCopyright("(c) 2014 baskar")
        self.about.SetWebSite("email: baskar4n@gmail.com")
        self.about.AddDeveloper("BASKAR")
        wx.AboutBox(self.about)
            
                
            
app=wx.App()
frame=inverter()
frame.Centre()
frame.Show()
app.MainLoop()
