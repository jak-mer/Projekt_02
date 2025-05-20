"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Merta
email: merta.arch@gmail.com
"""
# Import knihoven:
import random
import time

statistiky = []

###################### Funkce POZDRAV:
def pozdrav():
    """
    Funkce pozdraví uživatele a řekne mu, co má dělat.
    """
    print(
"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:"""
    )


###################### Funkce GENERUJ_NÁHODNÉ_4MÍSTNÉ_CÍSLO, které nezačíná nulou:

def generuj_cislo():
    """
    Funkce vygeneruje náhodné 4místné číslo, které nezačíná nulou.
    """
    while True: # Nekonečná smyčka pojede dokud se nevygeneruje číslo, které začíná číslicí jinou než 0.
        cislice = random.sample(range(10), 4) # Fce random.sample generuje 4 unikátní číslice z rozsahu 0-9. Vytvoří list.
        if cislice[0] != 0: # Když se první číslice listu nerovná 0, tak vrať ...
            return int("".join(map(str, cislice))) # ... převede list na číslo a vrátí ho. 
        
# Funkce map v Pythonu aplikuje zadanou funkci na každý prvek z iterovatelného objektu.
# Metoda "".join() v Pythonu spojí prvky iterovatelného objektu (například seznam řetězců) do jednoho řetězce.
# Funkce int() převede řetězec na celé číslo.

""" Převedení listu na číslo pomocí smyčky for nebo list comprehension:
POMOCÍ SMYČKY FOR:
cislo_str = ""
for cifra in cislice:
    cislo_str += str(cifra)
return int(cislo_str)

POMOCÍ LIST COMPREHENSION:
cislo_str = "".join([str(cifra) for cifra in cislice])
return int(cislo_str)
"""

###################### Funkce ZADEJ ČÍSLO:
def zadej_cislo():
    """
    Funkce vyzve uživatele k zadání 4místného čísla.
    """
    while True: # Nekonečná smyčka pojede dokud uživatel nezadá číslo, které splňuje podmínky.
        try: # Zde je použitý try-except blok pro zachycení výjimek. Možná není nutný a trošku předbíhám, ale pro jistotu.
            user_input = input(">>> ")
            if len(user_input) != 4:
                print("The number must have 4 digits.")
            elif user_input[0] == "0":
                print("The number cannot start with zero.")
            elif not user_input.isdigit():
                print("Please enter a valid number.")
            elif len(set(user_input)) != 4:
                print("The number cannot contain duplicate digits.")
            else:
                return int(user_input)
        except ValueError:
            print("Please enter a valid number.")

###################### Funkce POROVNÁNÍ ČÍSEL:
def porovnej_cisla(vygenerovane_cislo, hadane_cislo):
    """
    Funkce porovná vygenerované číslo s uživatelským číslem a vrátí počet "bulls" a "cows".
    """
    bulls = 0
    cows = 0

    # Převod čísel na seznam číslic
    vygenerovane_cislo_list = [int(cislice) for cislice in str(vygenerovane_cislo)] # list comprehension
    hadane_cislo_list = [int(cislice) for cislice in str(hadane_cislo)] # list comprehension

    # Porovnání čísel
    for i in range(4):
        if vygenerovane_cislo_list[i] == hadane_cislo_list[i]:
            bulls += 1
        elif hadane_cislo_list[i] in vygenerovane_cislo_list:
            cows += 1

    return bulls, cows

###################### Funkce VYHODNOCENÍ POKUSU:
def hlavni():
    pozdrav() # Tady voláme funkci pozdrav.
    vygenerovane_cislo = generuj_cislo() # Tady pomocí funkce generuj_cislo vygeneruju náhodné číslo.
    bulls = 0 # Tady si vytvořím proměnnou bulls, která bude počítat kolik je bulls.
    cows = 0 # Tady si vytvořím proměnnou cows, která bude počítat kolik je cows.
    pokusy = 0 # Tady si vytvořím proměnnou pokusy, která bude počítat kolik pokusů uživatel udělal.
    
    pocatecni_cas = time.time()  # Zaznamenání začátku
  
    while bulls != 4: # Smyčka pojede dokud se bulls nerovná 4.
        print("-----------------------------------------------")
        hadane_cislo = zadej_cislo() # Tady volám funkci zadej_cislo, která vyzve uživatele k zadání čísla a uloží ho do proměnné hadane_cislo.
        bulls, cows = porovnej_cisla(vygenerovane_cislo, hadane_cislo) # Tady si do proměnných bulls a cows uložím hodnoty, které vrátí funkce porovnej_cisla.
        pokusy += 1 # Tady si přičítám 1 k počtu pokusů pomocí zkráceného zápisu.
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}") # Tady vypíšu počet bulls a cows, pomocí ternárního operátoru.

    koncovy_cas = time.time()  # Zaznamenání konce
    trvani = koncovy_cas - pocatecni_cas # Výpočet doby trvání 

    statistiky.append({
        "pokusy": pokusy,
        "cas": trvani
})

    print(f"Correct, you've guessed the right number in {pokusy} guesses!")
    print(f"Time elapsed: {trvani:.1f} seconds")

    
########################################################### HLAVNÍ FUNKCE PROGRAMU
if __name__ == "__main__": # Podmínka, která zaručí, že se kód spustí pouze pokud je tento soubor spuštěn jako hlavní program.
    while True: # Nekonečná smyčka pro opakování hry, dokud nenarazí na break.
        hlavni() # Volání funkce hlavni, která spustí hru.
        dalsi_hra = input("Do you want to play again? (yes/no): ") # Tady se ptám uživatele, jestli chce hrát znovu.
        if dalsi_hra.lower() != "yes": # Pokud uživatel nezadá "yes", tak se hra ukončí.
            break

    print("Game statistics:") # Pak to pokračuje vypisem statistik.
    for poradi_hry, hra in enumerate(statistiky, 1): # Vytvořím si očíslovaný seznam statistik.
        print(f"Game {poradi_hry}: {hra['pokusy']} guesses, {hra['cas']:.1f} seconds") # Vytisknu počet pokusů a čas hry.
########################################################### HLAVNÍ FUNKCE PROGRAMU

