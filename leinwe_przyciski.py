# Leniwe przyciski
# Demonstacja tworzenia przycisków

from tkinter import *

#okno główne
root = Tk()
root.title("Leniwe przyciski")
root.geometry("200x85")


#ramka na widgety
app = Frame(root)
app.grid()

#tworzenie przycisków w ramce
bttn1 = Button(app, text = "Nic nie robię")
bttn1 .grid()

#tworzenie drugiego przycisku w ramce
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Ja również")


# przycisk numer trzy
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "To samo mnie dotyczy"

#pętla zdarzeń okna głównego
root.mainloop()
