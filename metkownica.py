# Metkownica
# Demonstracja etykiety

from tkinter import *


root = Tk()
root.title("Metkownica")
root.geometry("200x50")


#utwórz w oknie ramkę jako pojemnik na inne widgety
#podłoże pod wszystko

app = Frame(root)
app.grid()

#utwórz w ramce etykietę
lbl = Label(app, text = "jestem etykietą!")
lbl.grid()

# uruchomienie pętli zarzeń okna
root.mainloop()
