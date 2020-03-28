#libraries and modules
from tkinter import *
import os

#functions
x = ('Arial Narrow', 11)
def gameStart ():
    menu.destroy()
    os.system("python loop.py")



#initialisers
menu = Tk(className= "Pong Game -- By ZMamba")
menu.geometry("400x400")
menu.configure(background="black")

#widgets
mainText = Label( menu,text="PONG \n THE GAME",
                        bg="black",
                        fg= 'green',
                        font=("Algerian", 20),
                        pady = "10"
                         )
mainText.pack()
startButton = Button(menu, text="Start Game",
                            height = "3",
                            width = "30",
                            activebackground="black",
                            activeforeground = "white",
                            background = "black",
                            font = x,
                            fg = "green",
                            command = gameStart)

startButton.pack()
optionButton = Button(menu, text="Option",
                            height = "3",
                            width = "30",
                            activebackground="black",
                            activeforeground = "white",
                            background = "black",
                            font = x,
                            fg= "green")
optionButton.pack()
quitButton = Button(menu, text="Quit",
                            height = "3",
                            width = "30",
                            activebackground="black",
                            activeforeground = "white",
                            background = "black",
                            font = x,
                            fg = "green",
                            command = menu.destroy)
quitButton.pack()
#conditions

#mainloop
menu.mainloop()

