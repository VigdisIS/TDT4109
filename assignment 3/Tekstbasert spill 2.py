#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li class="active"><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Tekstbasert spill 2
# 
# **Læringsmål:**
# 
# * Løkker
# * Betingelser
# 
# I denne oppgaven skal vi utvide spillet vi begynte på i øving 2. Du må ikke ha gjort oppgaven i øving for å gjøre denne, men det kan være lurt å ta en kikk [her](link) for å forstå hva oppgaven går ut på. 

# ### a)

# Ved hjelp av en while løkke, la brukeren skrive inn kommando, og gjenta tilstanden dersom brukeren gir inn en ugyldig kommando. Se forrige oppgave for oppførsel ellers. 
# 
# Eksempel:
# ```python
# Du står utenfor en dør.
# >sadasd
# Forstår ikke kommando, prøv noe annet.
# Du står utenfor en dør.
# >Gå inn
# Du går inn døren.
# ```
# 
# ***Skriv koden din i blokka under***

# In[1]:


action = "gå inn"
valg = ""

while valg.lower() is not action.lower() :
    print("Du står utenfor en dør.")
    valg = input("")
    if valg.lower() == action.lower():
        print("Du går inn døren.")
        break
    else:
        print("Forstår ikke kommando, prøv noe annet.")


# ### b)

# Ved hjelp av løkker ønsker vi nå at visse kommandoer skal ta brukeren tilbake til utgangspunktet i spillet.  Dersom en bruker skriver inn en kommando som ikke skal ta brukeren ut av spillet (eller en ugyldig kommando), ønsker vi at den opprinnelige meldingen brukeren får skal gjentas, ellers går spilleren ut av løkken. **Altså, for alle andre kommandoer enn en spesifikk skal løkka gjentas.** I eksempelet under gjentas tilstanden helt til brukeren skriver noe som endrer den.
# 
# Eksempel:
# ```python
# Du står utenfor en dør med en postkasse.
# >bank på
# Du får ingen respons.
# Du står utenfor en dør med en postkasse. #opprinnelig tilstand
# >gå andre veien
# Du snur deg og vandrer hjem igjen. Du hører en skummel lyd og løper tilbake. 
# Du står utenfor en dør med en postkasse. #opprinnelig tilstand
# >åpne døren 
# Du går inn døren. #går ut av løkken
# ```
# 
# ***Skriv koden din i blokka under***

# In[2]:


action1 = "bank på"
action2 = "gå andre veien"
action3 = "åpne døren"
valg = ""

while valg.lower() is not action3.lower() :
    print("Du står utenfor en dør med en postkasse.")
    valg = input("")
    if valg.lower() == action1.lower():
        print("Du får ingen respons")
    elif valg.lower() == action2.lower():
        print("Du snur deg og vandrer hjem igjen. Du hører en skummel lyd og løper tilbake.")
    elif valg.lower() == action3.lower():
        print("Du går inn døren.")
        break
    else:
        print("Forstår ikke kommando, prøv noe annet.")


# ### c)

# Ved hjelp av løkker og variabler skal du nå la visse kommandoer brukeren skriver inn endre tilstanden i spillet (altså variablene) **selv om vi ikke går ut av løkka**. Ved å sjekke tilstanden til disse variablene skal en kommando kunne gjøre to ting, utifra hva tilstanden til en variabel er satt til.
# 
# Eksempel:
# ```python
# Du står utenfor en dør med en postkasse.
# >åpne døren
# Døren er låst.
# 
# Du står utenfor en dør med en postkasse.
# >åpne postkassen
# Du finner en nøkkel. #her må man oppdatere en variabel
# 
# Du står utenfor en dør med en postkasse. #vi printer ut det samme 
# >åpne døren 
# Du låser opp døren og går inn. #her er tilstanden annerledes enn når vi startet og vi går ut av løkka
# ```
# 
# ***Skriv koden din i blokka under***

# In[7]:


action1 = "åpne døren"
action2 = "åpne postkassen"
game_complete = False
valg = ""
nøkkel = False

while game_complete is not True:
    print("Du står utenfor en dør med en postkasse.")
    valg = input("")
    if valg == action1 and nøkkel == False:
        print("Døren er låst.")
    elif valg == action2:
        print("Du finner en nøkkel.")
        nøkkel = True
    elif valg == action1 and nøkkel == True:
        print("Du låser opp døra og går inn.")
        break
    elif valg == "":
        print("Ha en fin dag!")
        break


# ### d)

# Legg til muligheten for brukeren til å gå ut av spillet uansett tilstand vet å kun trykke enter uten å skrive inn noe. Legg inn en avslutningsmelding.
# 
# Eksempel:
# ```python
# Du står utenfor en dør med en postkasse.
# >
# Ha en fin dag!
# ```
# 
# ***Skriv koden din i samme blokk som oppgave c***

# #### Hint

# Du kan bruke break for å hoppe ut av en løkke.
