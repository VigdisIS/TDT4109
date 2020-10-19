#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving6.ipynb">Øving 6</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Generelt%20om%20lister.ipynb">Generelt om lister</a></li>
#     <li ><a href="Lett%20og%20blandet.ipynb">Lett og blandet</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li ><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li ><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li class="active"><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li ><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Lotto
# 
# **Læringsmål:**
# 
# * Lister
# * Tilfeldige tall
# 
# **Starting Out with Python:**
# 
# * Kap. 7
# 
# I denne oppgaven lage du lage en lottosimulator. 
# 
# Reglene er som følger:
# 
# * Det trekkes ut 7 lottotall og 3 tilleggstall fra og med 1 til og med 34. Alle tallene som trekkes skal være unike.
# * Premier deles ut basert på følgende tabell:
# 
# Premiergruppe|Premie (kr)
# :---|---
# 7 rette	|2 749 455
# 6 rette + 1 tilleggstall	|102 110
# 6 rette	|3 385
# 5 rette	|95
# 4 rette + 1 tilleggstall	|45

# ### a)

# Lag en liste som heter `numbers` og som inneholder alle heltall fra og med 1 til og med 34.
# 
# ***Skriv koden din i boksen under.***

# In[1]:


numbers = list(range(1, 35))


# ### b)

# Lag en liste som heter `myGuess` med 7 tall. Denne listen inneholder tallene som du tipper.
# 
# ***Skriv koden din i boksen under.***

# In[2]:


import random

myGuess = [4,19,28,32,1,11,14]

print(myGuess)


# ### c) 

# Lag en funksjon som tar inn `n` som argument og som trekker ut `n` tall ut av listen `numbers` og legger de i en egen liste.  
# For å gjøre ting tilfeldig: `import random` og `random.randint(n,N)` gir tilfeldige tall fra og med n til og med N.
# 
# Eksempel på kjøring:
# 
# ```python
# >>>print(drawNumbers(numbers, 7))
# [16, 33, 5, 20, 7, 4, 8]
# ```
# 
# ***Skriv koden din i boksen under.***

# In[3]:


import random

lottoTall = []
tilleggsTall = []

def drawNumbers(numbers,n):
    while len(lottoTall) != n:
        tilf_tall = random.choice(numbers)
        while tilf_tall not in lottoTall:
            lottoTall.append(tilf_tall)
    return lottoTall

def drawTillegg(numbers,n):
    while len(tilleggsTall) != n:
        tilf_tall = random.choice(numbers)
        while tilf_tall not in tilleggsTall and tilf_tall not in lottoTall:
            tilleggsTall.append(tilf_tall)
    return tilleggsTall

print(drawNumbers(numbers, 7))
print(drawTillegg(numbers, 3))


# #### Hint

# Hint: Bruk funksjonene `pop()` og `append()` for å fjerne og legge til elementer i en liste. Husk at pop fjerner et element i en indeks i lista, den fjerner ikke tallet. Så numbers.pop(rand_num) fjerner elementet på indeks rand_num - altså hvis rand_num er 13 fjernes tallet på indeks 13, ikke tallet 13!

# ### d)

# Lag funksjonen `compList` som sammenligner to lister med tall. Antall like tall i listene skal returneres.
# 
# Eksempel på kjøring:
# 
# ```python
# >>>print(compList(drawNumbers(numbers,7),myGuess))
# 1
# ```
# 
# ***Skriv koden din i boksen under.***

# In[6]:


def compList(liste1,liste2):
    antall_like = 0
    for i in liste2:
        for y in liste1:
            if i == y:
                antall_like +=1
    return antall_like

lotto_tall = drawNumbers(numbers, 7)
tilleggs_tall = drawTillegg(numbers, 3)

print(myGuess)
print(lotto_tall)
print(compList(lotto_tall,myGuess))
print (tilleggs_tall)
print(compList(tilleggs_tall,myGuess))


# ### e)

# Lag en funksjon som tar inn antall like tall og like tilleggstall, og returnerer premien du har vunnet.
# 
# Eksempel på kjøring:
# 
# ```python
# >>>print(Winnings(7,1))
# 2749455
# >>>print(Winnings(5,2))
# 95
# >>>print(Winnings(3,1))
# 0
# ```
# 
# ***Skriv koden din i boksen under.***

# In[12]:


def winnings(like_tall,like_tilleggstall):
    if like_tall == 7:
        return 2749455
    elif like_tall == 6 and like_tilleggstall >= 1:
        return 102110
    elif like_tall == 6 and like_tilleggstall == 0:
        return 3385
    elif like_tall == 5:
        return 95
    elif like_tall == 4 and like_tilleggstall >= 1:
        return 45
    else:
        return 0

print(winnings(7,1))   
print(winnings(5,2))  
print(winnings(3,1))  


# ### f)

# Funksjonene skal settes sammen i main() slik at dette blir en fullverdig lottosimulator (for en lottorekke). Tallene du skal trekke ut (både lottotallene og tilleggstallene) kan legges i samme liste. Funksjonen `compList` kan da sammenligne de første 7 tallene, og så de siste 3 tallene, for å finne ut hvor mange like tall du har. main() skal returnere hvor mye du har tjent eller mest sannsynlig tapt på denne lottorekken. Dersom en lottorekke kosten 5 kroner, vil -5 returneres dersom Winnings() er 0. Hvis du er heldig og Winnings() blir 95 skal 90 returneres fra main(). 
# 
# **Husk at du kan bruke alle funksjoner du har definert over!**
# 
# ***Skriv koden din i boksen under.***

# In[25]:


def main():
    print("Du har gjettet tallene: {0}".format(myGuess))
    lottoTall = drawNumbers(numbers, 7)
    tilleggsTall = drawTillegg(numbers, 3)
    print("De 7 lottotallene er {0}, i tillegg til tre trukkede tilleggstall: {1}".format(lottoTall, tilleggsTall))
    like_lottoTall= compList(lottoTall,myGuess)
    like_tilleggsTall= compList(tilleggsTall,myGuess)
    print("Du har {0} like lottotall og {1} like tilleggstall.".format(like_lottoTall, like_tilleggsTall))
    penger_vunnet = int(winnings(like_lottoTall,like_tilleggsTall))
    return (penger_vunnet - 5)

main()

    


# ### g) frivillig

# Finn ut hvor mye man har vunnet etter å ha tippet en million ganger. Anta at premiepotten er det samme hver uke, og at en lottorekke koster 5 kroner.
# 
# ***Skriv koden din i boksen under.***

# In[ ]:




