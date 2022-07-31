from PIL import Image
import random
import os
from pypresence import Presence
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

Layer = [ 
    "./Backgrounds/Pink.png",
    "./Backgrounds/Purple.png",
    "./Backgrounds/Teal.png",
    "./Backgrounds/Green.png",
    "./Backgrounds/Red.png",
    "./Backgrounds/Blue.png",
    "./Backgrounds/Orange.png",
    "./Backgrounds/Gray.png"  
]

Cones = [ 
    "./Cones/Regular.png",
    "./Cones/Waffle.png"
]

Creams = [ 
    "./Cream/Avocado.png",
    "./Cream/Beer.png",
    "./Cream/Bubblegum.png",
    "./Cream/Butterscotch.png",
    "./Cream/CherryRipe.png",
    "./Cream/Caramel.png",
    "./Cream/Cement.png",
    "./Cream/CherryRipe.png",
    "./Cream/ChocMint.png",
    "./Cream/Chocolate.png",
    "./Cream/CookieDough.png",
    "./Cream/CookiesAndCream.png",
    "./Cream/FairyFloss.png",
    "./Cream/Kirby.png",
    "./Cream/LemonSorbet.png",
    "./Cream/Mango.png",
    "./Cream/Neapolitan.png",
    "./Cream/OldEnglishToffee.png",
    "./Cream/Pineapple.png",
    "./Cream/PineappleNumberTwo.png",
    "./Cream/Rainbow.png",
    "./Cream/Spaghetti.png",
    "./Cream/Tomato.png",
    "./Cream/WhiteChocolate.png",
    "./Cream/Vanilla.png"
]

a=[]
b=0
i=1


rpc = Presence("885705446768377946")
rpc.connect()
rpc.update(state="Idling",large_image="highres",large_text="Just Cones",start=time.time())

while True:
    if len(a)==1000:
        print(f'{Fore.GREEN}Successfully exported {i-1} variations.')
        rpc.update(state="Idling",large_image="highres",large_text="Just Cones",start=time.time())
        os.system("read") # will only work on shell
        # put the amount of variations in place of 108 (aka confusing asf for loop that is overcomplicated.)
        break
    background = random.choices(Backgrounds, weights=None)[0] #8
    cone = random.choices(Cones, weights=None)[0] #2 
    cream = random.choices(Creams, weights=None)[0] #25

    if (background,cream,cone) in a: 
        continue
    else:
        a.append((background,cone,cream))
    layer1 = Image.open(background)
    layer2 = Image.open(cream)
    intermediate = Image.alpha_composite(layer1, layer2)
    layer3 = Image.open(cone)
    final = Image.alpha_composite(intermediate, layer3)

    final.save(f'{i}.png')
    print(f'{i}.png was generated')
    rpc.update(state=f"Cone ({i} of 1000)",details="Generating Cones",large_image="highres", large_text="Just Cones")
    i+=1