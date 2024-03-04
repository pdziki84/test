#wybór filmów
#pola wyboru

from tkinter import *


class Application(Frame):
    """Aplikacja GUI służąca do wyboru ulubionych gatunków filmów."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utwórz widgety służące do wyboru gatunków filmów"""
        #etykieta z opisem
        Label(self,
              text = "Wybierz swoje ulubione fgatunki filmów."
              ).grid(row = 0, column = 0, sticky = W)
        #etykieta z instrukcją
        Label(self,
             text = "Zaznacz wszystkie, które chciałbyś wybraać:"
             ).grid(row = 1, column = 0, sticky = W)
        
        #utwórz pole wyboru komedii
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = "komedia",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        
        #pole wyboru dramatu filmowego
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "dramat",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        #pole wyboru romansu
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "romans",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        #pole textowe do wyświetlania wynikó
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Zaakceptuj pole textwoe i wyświetl ulubione gatunki ilmowe użytkownika."""
        likes = ""

        if self.likes_comedy.get():
            likes += "Lubisz filmy komediowe\n"
        if self.likes_drama.get():
            likes += "Lubisz dramaty filmowe\n"
        if self.likes_romance.get():
            likes += "Lubisz filmy romantyczne\n"

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

#częśc główna

root = Tk()
root.title("Wybór filmów")

app = Application(root)
root.mainloop()
        







































        

        
        
        
        

        
