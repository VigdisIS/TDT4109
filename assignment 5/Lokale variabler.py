#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li class="active"><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Lokale variabler
# 
# **Læringsmål:**
# - Kodeforståelse
# - Funksjoner
# 
# **Starting Out with Python:**
# - Kap. 5.4

# ## Generelt om lokale variabler
# Dette er ikke en del av øvingen, men kan være lurt å lese før du går videre.

# En lokal variabel er en variabel som blir lagd inne i en funksjons kodeblokk, og som ikke kan benyttes av kall utenfor funksjonen. Koden under viser et eksempel på dette. Prøv å kjøre koden og se hva som skjer. Hva tror du er galt?

# In[1]:


def getName():
    name = input("Hva heter du? ")  

getName()
print("Hei,",name)


# Her er `name` en lokal variabel for funksjonen `getName()`. Dette medfører at koden i linje 5 ikke kan aksessere variabelen `name` slik den prøver, og at programmet krasjer. Vi får her feilmeldingen "NameError: name 'name' is not defined", som rett og slett betyr at programmet ikke har kjennskap til noen variabel eller funksjon ved navnet 'name'.
# 
# For å få koden til å fungere slik vi ønsker kan vi returnere name-variabelen og tilordne denne til en egen variabel - som kan kalles name eller noe helt annet - som linje 5 har tilgang til. Koden kan da se ut som under. Test gjerne koden og se at den virker.

# In[2]:


def getName():
    name = input("Hva heter du? ")
    return name
  
name = getName()
print("Hei,",name)


# Koder kan også inneholde parametere som også fungerer som lokale variabler. Eksempelvis.

# In[4]:


def printName(name):
    print("Hei", name)
  
 
printName("Ola")


# Her vil "Ola" bli til **name**-variabelen og kun være tilgjengelig innenfor funksjonen.

# ## a)

# Alle kodesnuttene under inneholder en feil, men en av dem vil fortsatt kjøre uten å krasje; hvilken og hvorfor? **Prøv å finne feilen i hver kodesnutt.**

# In[6]:


#Kodesnutt 1:
def cupcakes():
    cupcakes = 24
    print("Jeg har laget",cupcakes,"cupcakes")

def cakes():
    cake = 1
    print("Men jeg har bare bakt",cake,"kake")

cupcakes()
cakes()


# In[9]:


#Kodesnutt 2:
cupcake = 1

def cupcakes():
    print("Jeg har laget",cupcake,"cupcake")

def cakes():
    print("Og jeg har bakt",cupcake,"kake")

cupcakes()
cakes()


# In[12]:


#Kodesnutt 3:
def cupcakes():
    cupcakes = 24
    print("Jeg har laget",cupcakes,"cupcakes")

def cakes():
    cake = 10
    print("Men jeg har bare bakt",cake,"kake")

cupcakes()
cakes()


#Denne kjørte på tross av feilen fordi cakes-funksjonen aldri ble hentet (cakes() fantes ikke).
#'cake' var heller ikke definert.


# ***Dobbelklikk på teksten under og skriv svaret ditt i boksen som kommer opp***

# Svar: < dobbeltklikk her>

# #### Hint

# Feilen i hver kode befinner seg i cakes()-funksjonen. Tenk på plassering av variabelen brukt i cakes-funksjonen.
# 
# For å finne ut hvilken kodesnutt som ikke vil krasje ved kjøring av koden, tenk på funksjonskall. Er det et tilfelle der koden med feil i ikke vil bli utført?

# ## b)

# I denne oppgaven skal du skrive to funksjoner. Den første skal ta inn to argumenter `x` og `y`, lage en variabel `num` = `x//y`, og returnere resultatet slik at programmet kan skrive til skjerm "Heltallsdivisjon av `x` over `y` gir `num`".
# 
# Den andre funksjonen skal ta inn ett argument x, lage en varibel num = x\*\*2, og returnere resultatet slik at programmet kan skrive til skjerm "Kvadratet av `x` er `num`".
# 
# ***Skriv koden din i kodeblokken under***

# In[26]:


x = int(23)
y = int(4)

def heltallsdivisjon(x, y):
    num=x//y
    print("Heltallsdivisjon av", x, "over", y, "gir", num)

heltallsdivisjon(x, y)
    
x = int(3)
    
def kvadrat(x):
    num = x**2
    print("Kvadratet av", x, "er", num)

kvadrat(x)
    


# Eksempel på kjøring:
# ```python
# Heltallsdivisjon av 23 over 4 gir 5
# Kvadratet av 3 er 9
# ```

# ## c)

# Begge funksjonene i b) har en variabel kalt num. Kan dette føre til noen problemer i koden? Hvorfor/Hvorfor ikke?
# 
# ***Dobbelklikk på teksten under og skriv svaret ditt i boksen som kommer opp***

# Svar: Variabelen endres i hvert av funksjonene. Dersom den første funksjonen blir callet før den andre bruker num og endrer på den, vil dette ikke skape problemer. Dersom begge funksjonene utføres samtidig uten å endre på variablene som skal gi num, vil det føre til problemer.
