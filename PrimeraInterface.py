from tkinter import *

raiz=Tk()
raiz.title("Ventana de prubea")#nombre de la ventana
raiz.resizable(True,True) #permitir width o heigt
# raiz.geometry("500x500")
# raiz.config(bg="black")
miFrame=Frame()
miFrame.pack() #metemos el frame en la ventana


miFrame.config(bg="red",width="650",height="400",bd=30,relief="sunken",cursor="hand2")
raiz.config(bg="blue",bd=30,relief="sunken")
# miFrame.config(width="650",height="400")
# miFrame.config(bd=30)
# miFrame.config(relief="sunken")
# miFrame.config(cursor="hand2")


raiz.mainloop()#crear ventana
