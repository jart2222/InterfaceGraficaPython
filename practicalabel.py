from tkinter import Tk, Frame, Label, PhotoImage

root=Tk()
miFrame=Frame(root,width=1000,height=2000)
miFrame.pack()
miImagen=PhotoImage(file="celluloid_minimal.gif")
miLabel=Label(miFrame,image=miImagen,text="Hola Alumnos de python",fg="blue",font=("Arial 20"))
miLabel.place(x=100,y=200)
root.mainloop()
