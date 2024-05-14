from tkinter import *


root = Tk()
root.geometry("800x700")
root.title("Map Book")


ramka_lista_uzytkownikow=Frame(root)
ramka_formulaz= Frame(root)
ramka_szczegoly_obiektu=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formulaz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0)

#ramka_lista_obiektów
label_lista_obiektow=Label(ramka_lista_uzytkownikow, text="Lista znajomych:")
listbox_lista_obiektow=Listbox(ramka_lista_uzytkownikow, width=30)

button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text="Pokaz szczegóły:")
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow, text="Usuń:")
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow, text="Edytuj:")

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytuj_uzytkownika.grid(row=2, column=2)


#ramka_formularz

label_formularz=Label(ramka_formulaz, text="Formularz edycji dodawania:")
label_formularz.grid(row=0, column=0, columnspan=3)






root.mainloop()
