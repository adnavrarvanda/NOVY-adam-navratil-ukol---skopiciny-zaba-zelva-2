import turtle
import random
import time

# --- ČÁST 1: VIZUÁLNÍ VYKRESLENÍ PASTVINY (Turtle) ---

# Nastavení obrazovky pro kreslení
okno = turtle.Screen()
okno.bgcolor("lightgreen")  # Pastvina je zelená a svěží
okno.title("Průzkum neznámého koutu pastviny")

# Vytvoření "želvy" (našeho berana), která bude kreslit
lod = turtle.Turtle()
lod.speed(0)  # Nejrychlejší kreslení, abychom na ovečky nečekali moc dlouho
lod.hideturtle()  # Schováme samotnou ikonu berana, chceme vidět jen ovečky

# Seznam možných barev oveček, ze kterých budeme náhodně vybírat
# Zvolila jsem barvy vlny.
barvy_hvezd = ["white", "lightgray", "ivory", "mistyrose"]

def nakresli_hvezdu(velikost):
    """
    Funkce pro vykreslení jedné "ovečky".
    Kód pro kreslení pěticípého tvaru zůstává STEJNÝ, 
    takže budeme mít hvězdicovité ovečky!
    Zvolil jsem funkci, abychom kód nemuseli psát neustále dokola.
    """
    lod.begin_fill()
    # Cyklus pro 5 "končetin/cípů". Používáme pevný počet opakování (for cyklus).
    for _ in range(5):
        lod.forward(velikost)
        lod.right(144) # Úhel 144 stupňů vytváří klasický hvězdicovitý tvar
    lod.end_fill()

print("Začínáme dovádět a dělání neplechy na pastvině...")
# Malá pauza před začátkem skopičin pro efekt
time.sleep(1)

# Chceme vykreslit přesně 40 oveček. Cyklus for je ideální, když známe přesný počet opakování.
for i in range(40):
    # Generování náhodných souřadnic na obrazovce
    # Zvolil jsem rozmezí -300 až 300, aby se ovečky vešly do standardního okna
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    # Náhodný výběr barvy ze seznamu
    barva = random.choice(barvy_hvezd)
    
    # Náhodná velikost ovečky (jehňátka i starší berani)
    velikost = random.randint(5, 15)
    
    # Přesun berana (bez kreslení čáry) na novou náhodnou pozici
    lod.penup()
    lod.goto(x, y)
    lod.pendown()
    
    # Nastavení barvy a vykreslení "ovečky" pomocí naší funkce
    lod.color(barva)
    nakresli_hvezdu(velikost)

print("Pastvina se jen hemží ovečkami a je připravena na skopičiny.")
# Počkáme 2 sekundy, aby si uživatel mohl prohlédnout pastvinu, než se posuneme dál
time.sleep(2)


# --- ČÁST 2: DRAMATICKÁ TEXTOVÁ ČÁST S ASCII ARTEM ---

print("\n--- POZOR, PŘICHÁZÍ SKOPIČINA! ---")
time.sleep(1.5) # Zde používám time.sleep pro budování napětí v textové konzoli
print("Plánujeme velkou neplechu z nedalekého koutu...")
time.sleep(2)
print("Realizujeme naši skopičinu", end="") # end="" zajistí, že další print bude na stejném řádku

# Cyklus pro simulaci načítání (vypíše tři tečky s pauzami)
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(1)

print("\nSkopičina v plném proudu!\n")
time.sleep(1)

# Tři různé ASCII obrázky oveček dělajících skopičiny, uložené jako víceřádkové textové řetězce
# Ponechávám názvy proměnných identical k původnímu kódu pro naplnění tvého zadání.
mimozemstan_1 = """
   ( @ @ )
    V   V   - / \\ -
    ( _ )   (  .  )
    U U    /(  :  )\\
             \\_^_/
    "Jen tak, píp bíp! Právě jsem vypustil všem traktorům pneumatiky."
"""

mimozemstan_2 = """
   ,-'~~~`-.
  (  o o  )
   \\  -  /
    U--U'
     | |
    "Béééé! Změnila jsem cedulky s názvy polí a nikdo teď neví, kde je jetel."
"""

mimozemstan_3 = """
     _  _
    (o  o)
     V  V
    ( -- )
    "Tchá! Namaloval jsem farmáři na stodolu obří knír!"
"""

# Uložení do seznamu, ze kterého budeme vybírat
databaze_mimozemstanu = [mimozemstan_1, mimozemstan_2, mimozemstan_3]

# Pomocí random.choice náhodně vybereme jednu skopičinu a vypíšeme ji
nahodny_kontakt = random.choice(databaze_mimozemstanu)
print(nahodny_kontakt)

# Aby se grafické okno ihned nezavřelo a uživatel si mohl vše prohlédnout
turtle.done()