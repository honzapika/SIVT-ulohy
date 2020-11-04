from tkinter import *
class app:
  def __init__(self):
    self.okno=Tk()
    self.platno=Canvas(width=400, height=400, bg="dimgrey")
    self.platno.pack()
    self.pole1=0
    self.pole2=0
    self.pracovnipole=0
    self.i=0
    
    self.cislo1=Entry(self.okno)  # policko pro zadani prvniho čísla
    self.cislo1.pack()
    
    self.cislo2=Entry(self.okno)  # policko pro zadani druheho cisla
    self.cislo2.pack()
    
    self.plus=Button(self.okno,text="+", command=self.secist)
    self.plus.pack()
    self.minus=Button(self.okno,text="-", command=self.odecist)
    self.minus.pack()
    self.krat=Button(self.okno,text="*", command=self.vynasobit)
    self.krat.pack()
    self.deleno=Button(self.okno,text="/", command=self.vydelit)
    self.deleno.pack()

    
    
  
    
  def secist(self):
    if self.i==1:       
        self.platno.delete(self.vysledek) 
        self.pole1=self.cislo1.get()
        self.cislo1.delete(0,END)
        self.pole2=self.cislo2.get()
        self.cislo2.delete(0,END)
        self.pracovnipole=float(self.pole1)+float(self.pole2)
        self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole))
    if self.i==0:
       self.pole1=self.cislo1.get()
       self.cislo1.delete(0,END)
       self.pole2=self.cislo2.get()
       self.cislo2.delete(0,END)
       self.pracovnipole=float(self.pole1)+float(self.pole2)
       self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole)) 
       self.i=1  
       print("výsledek je ",self.pracovnipole)
  def odecist(self):
    if self.i==1: 
      self.platno.delete(self.vysledek) 
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END)  
      self.pracovnipole=(float(self.pole1)-float(self.pole2))  
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole))
      print("výsledek je ",self.pracovnipole)
    if self.i==0:
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END)  
      self.pracovnipole=(float(self.pole1)-float(self.pole2))  
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole))
      self.i=1
      print("výsledek je ",self.pracovnipole) 
  def vynasobit(self):
    if self.i==1:
      self.platno.delete(self.vysledek) 
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END)  
      self.pracovnipole=(float(self.pole1)*float(self.pole2)) 
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole)) 
      print("výsledek je ",self.pracovnipole)
    if self.i==0:
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END)  
      self.pracovnipole=(float(self.pole1)*float(self.pole2)) 
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole)) 
      self.i=1
      print("výsledek je ",self.pracovnipole)
  def vydelit(self):
    if self.i==1:
      self.platno.delete(self.vysledek) 
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END) 
      self.pracovnipole=(float(self.pole1)/float(self.pole2)) 
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole)) 
      print("výsledek je ",self.pracovnipole)  
    if self.i==0:
      self.pole1=self.cislo1.get()
      self.cislo1.delete(0,END)
      self.pole2=self.cislo2.get()
      self.cislo2.delete(0,END)
      self.pracovnipole=(float(self.pole1)/float(self.pole2)) 
      self.vysledek=self.platno.create_text(200,100,font="Times",text=str(self.pracovnipole)) 
      self.i=1
      print("výsledek je ",self.pracovnipole)  



a=app()
mainloop()
