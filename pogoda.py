#-------------------------------------------------------------------------------
# Name:        pogoda
# Purpose:
#
# Author:      Dmitriy Vygovskiy
#
# Created:     16.09.2023
# Copyright:   (c) Programista 2023
# Licence:     <GNU>
#-------------------------------------------------------------------------------
from tkinter import *
import requests
root = Tk()


#Funkcja sprawdza pogode
def get_weather():
    city = cityField.get()
    if not city:
        info['text'] = 'Wpisz miasto'
    else:
        # dane o pogodzie ze strony openweathermap.org
        #API rlucz, ze strony openweathermap.org
        key = '80263030671c4a75186677b20914d60b'
        #link z danymi z formacie JSON
        url = 'http://api.openweathermap.org/data/2.5/weather'
        # Dodatkowe parametry (Klucz, miasto)
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        # Wysyłam zapytanie do konkretnego URL
        result = requests.get(url, params=params)
        # Otrzymuje odpowiedź JSON z tego adresu URL
        weather = result.json()

        if 'main' in weather:
            temperature = weather['main']['temp']
            info['text'] = f'{city}: {temperature} °C'
        else:
            info['text'] = 'Nie znaleziono danych pogodowych'

root['bg'] = '#fafafa'
root.title('Aktualna pogoda')
root.geometry('300x250')
root.resizable(width=False, height=False)


frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)


frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)


cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()


btn = Button(frame_top, text='Sprawdź pogodę',bg='white', command=get_weather)
btn.pack()


info = Label(frame_bottom, text='Aktualna pogoda na dziś', bg='#ffb700', font=40)
info.pack()


root.mainloop()
