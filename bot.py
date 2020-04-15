#-------13 04 2020------#
#librerias :)
import webbrowser
import random
import time

#-------definimos variables------#

nav1=webbrowser.get("firefox")
print("comienza a ejecutarse :)")
cantidad_opciones = 25
p=0

#------ funciones ------#
def valor(p):#funcion que da un valor aleatorio
    if p == 1:
        value = 1
        value=(random.randint(2,26))
        print(value)
        switch(value)
    else: 
        return "Mal hecho :( p vale 0"
#--------funcion para acceder a las paginas web------#
def switch(value):
    print(value) #corroboramos que el valor se extrapolo bien
    if value == 2:
        nav1.open("elpais.com")
    elif value == 3:
        nav1.open("google.com")
    elif value == 4:
        nav1.open("wikipedia.org")
    elif value == 5:
        nav1.open("amazon.com")
    elif value == 6:
        nav1.open("apple.com")
    elif value == 7:
        nav1.open("microsoft.com")
    elif value == 8:
        nav1.open("ebay.com")
    elif value == 9:
        nav1.open("youtube.com")
    elif value == 10:
        nav1.open("spotify.com")
    elif value == 11:
        nav1.open("netflix.com")
    elif value == 12:
        nav1.open("facebook.com")
    elif value == 13:
        nav1.open("instagram.com")
    elif value == 14:
        nav1.open("twitter.com")
    elif value == 15:
        nav1.open("Live.com")
    elif value == 16:
        nav1.open("Marca.com")
    elif value == 17:
        nav1.open("elmundo.es")
    elif value == 18:
        nav1.open("linkedin.com")
    elif value == 19:
        nav1.open("wordpress.com")
    elif value == 20:
        nav1.open("bet365.es")
    elif value == 21:
        nav1.open("pinterest.com")
    elif value == 22:
        nav1.open("lavanguardia.com")
    elif value == 23:
        nav1.open("booking.com")
    elif value == 24:
        nav1.open("tumblr.com")
    elif value == 25:
        nav1.open("wordreference.com")
    elif value == 26:
        nav1.open("dropbox.com")
#------- se invocan la funcion dar valor y se asocia un tiempo de latencia-------#
p = 1
for i in range(cantidad_opciones):
    valor(p)    
    time.sleep(10)


