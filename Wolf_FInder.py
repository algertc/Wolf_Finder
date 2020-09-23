#  4.10 = {izza
# Charlie Algert
# Sep 23, 2020
'''
A simple program to automatically download
and open a randomly selected 4k wolf pic :)
Different pic every time from a pool of 6
'''

import requests, subprocess, os, platform
from colorama import Fore, Back, Style
from random import seed
from random import randrange
seed()
#################################################################

rand = randrange(5)


def convert(x):
    global wolfNumber
    inter = "wolf" + str(x)
    wolfNumber = str(inter) + ".jpg"
    return wolfNumber



def elseFunc(x = rand):
    global presux
    presux = str(x)
    convert(presux)



def getInput():

    presux = (input("Choose a number 1-5... or just hit enter  ¯\_(ツ)_/¯ : "))
    print("-" + str(presux) + "-")
    if presux == "":
        elseFunc()

    elif int(presux) == 1 or int(presux) == 2 or int(presux) == 3 or int(presux) == 4 or int(presux) == 5:
        convert(presux)




    else:
        getInput()
        #inter = "wolf" + str(presux)
       # wolfNumber = str(inter) + ".jpg"
        #return wolfNumber


getInput()

#print(wolfNumber)
print(Fore.GREEN + "Working...")
#print(str(wolfNumber))
url = "http://charliealgert.com/wolves/" + str(wolfNumber)


def currDir():
    global path
    path = os.getcwd()
    return path


currDir()

r = requests.get(url, allow_redirects=True)
open(str(wolfNumber), 'wb').write(r.content)


def returnFullDir():
    global final
    final = str(path) + "\\" + str(wolfNumber)
    return final


returnFullDir()

if platform.system() == 'Darwin':  # OSX
        subprocess.call(('open', final))
elif platform.system() == 'Windows':  # Windows
        os.startfile(final)
else:                               # SUPPORT LINUX!!
        subprocess.call(('xdg-open', final))

print("\n")
print(Fore.CYAN + 'Here Is Your Wolf, In Stunning 4K!')
