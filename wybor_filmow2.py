#wybór filmów 2
#demonstracja przycisków opcji

from tkinter import *


class Application(Frame):
    """Aplikacja GUI służąca do wyboru ulubionego filmu"""
    def __init__(self, master):
        """Inicjalizacja ramki"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):    
        """ Utwórz widżety umożliwiające wybór gatunku filmowego. """
        #istrukcje dla użytkowników
        #etykieta z opisem
        Label(self,
              text = "Wybierz swój ulubiony gatunek filmowy"
              ).grid(row = 0, column = 0, sticky = W)

        #utwórz etykietę z instrukcją
        Label(self,
              text = "Wybierz jeden gatunek: "
              ).grid(row = 1, column = 0, sticky = W)

        #zmienna, która reprezentuje pojedynczy , ulubiony gatunek filmu
        self.favorite = StringVar()
        self.favorite.set(None)

        #przycisk opcji do wyboru komedii
        Radiobutton(self,
                    text = "komedia",
                    variable = self.favorite,
                    value = "komedia",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        #przycisk opcji draamatu
        Radiobutton(self,
                    text = "draamat",
                    variable = self.favorite,
                    value = "dramat",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        #przycsk opcji romansu
        Radiobutton(self,
                   text = "romans",
                   variable = self.favorite,
                   value = "romans",
                   command = self.update_text
                   ).grid(row = 4, column = 0, sticky = W)

        #utwórz pole tekstowe do wyświetlania wyników
        self.results_txt = Text(self, width = 20, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Zaktualizuj pole tekstowe i wyświet ulubioony gatunek użytkownika"""
        message = "Twoim ulubionym gatunkiem filmowym jest "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)



#czesc główna

root = Tk()
root.title("Wybór filmów 2 ")

app = Application(root)
root.mainloop()







































    
    
                  

                
