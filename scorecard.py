__author__ = 'Chetan'

from Tkinter import *

# blank window
root = Tk()
# a text on the screen
theLabel1 = Label(root, text="PaintBall Team 1, HU superhuman sports", bg="red",fg="white")
theLabel2 = Label(root, text="PaintBall Team 2, HU superhuman sports", bg="green",fg="white")
theLabel3 = Label(root, text="PaintBall Team 3, HU superhuman sports", bg="blue",fg="white")
theLabel1.pack()
theLabel2.pack(fill=X)
theLabel3.pack(side=LEFT,fill=Y)



# crate frame
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)


button1 = Button(topframe, text="Start Game",fg="red")
button2 = Button(topframe, text="Pause Game",fg="green")
button3 = Button(topframe, text="Stop Game",fg="blue")
button4 = Button(bottomframe, text="Restart Game",fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()

