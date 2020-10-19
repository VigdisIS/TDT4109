#!/usr/bin/env python
# coding: utf-8

#  <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving10.ipynb">Øving 10</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Rekursjon.ipynb">Rekursjon (Obligatorisk TDT4109)</a></li>
#     <li ><a href="Matplotlib.ipynb">Matplotlib (Obligatorisk TDT4110)</a></li>
#     <li class="active"><a href="Eksamen%202012.ipynb">Eksamen Python 2012</a></li>
#     <li ><a href="Sudoku.ipynb">Sudoku</a></li>
#     <li ><a href="numpy-arrays%20og%20matplotlib.ipynb">Numpy-arrays og matplotlib (TDT4110)</a></li>
#     <li ><a href="Bokanalyse%20med%20plotting.ipynb">Bokanalyse med plotting (TDT4110)</a></li>
#     <li ><a href="Sjakk.ipynb">Sjakk</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Eksamen 2012

# ## Oppgave 1 - Teori (25%)

# Noen av flervalgsoppgavene som ikke var pensum er fjernet. For å få opp alle flervalgsoppgavene, `trykk på denne boksen, pil ned, og så ctrl + enter`. Merk at dersom du gjør dette igjen etter å startet en besvarelse vil besvarelsen din forsvinne. Dette gjelder kun flervalgsoppgaven. Trykk `Widgets->Save Notebook Widget State` for å lagre flervalgsoppgavene.  Du kan trykke `Cell->All Output->Toggle Scrolling` for å få alle oppgavene i et stort vindu.
# 
# Hvis dette ikke fungerer, kan du finne teoriøvingene her: [eksamen2012teori.txt](eksamen2012teori.txt). Skriv i så fall ned svarene selv og vis dette til studass under demonstrasjonen.

# In[55]:


import os
import ipywidgets as widgets
import sys
import random
from IPython.display import display
from IPython.display import clear_output


def generate_mc(answers,question,answer,custom_feedback=[],shuffle=True):
    out = widgets.Output()
    answer_string = answers[answer-1] #svaret på spørsmålet
    if shuffle:
        if(len(custom_feedback)==len(answers)): #dersom vi har feedback må denne sorteres shuffles sammen med svarene
            mapIndexPosition = list(zip(answers, custom_feedback))
            random.shuffle(mapIndexPosition)
            answers, custom_feedback = zip(*mapIndexPosition)
        else: #ellers shufler vi bare svarene
            random.shuffle(answers)
    alternativ = widgets.RadioButtons(
    options=answers,
    description='',
    layout=widgets.Layout(width='1500px'),
    disabled=False)
    answer=answers.index(answer_string)
    print('\033[1m',question,'\033[0m')
    button = widgets.Button(description="Sjekk svaret")
    display(alternativ)
    display(button)
    def check_answer(b):
        a = alternativ.value
        if(a==answer_string):
            color = '\x1b[6;30;42m' + "Riktig." + '\x1b[0m' +"\n" #fargen blir da grønn
            if(len(custom_feedback)==len(answers)):
                color += custom_feedback[answer]
        else:
            color = '\x1b[5;30;41m' + "Feil. " + '\x1b[0m' +"\n" #ellers blir fargen rød
            if(len(custom_feedback)==len(answers)):
                color += custom_feedback[answer]
        with out:
            clear_output()
            print(color)
            
            
      
    display(out)
    button.on_click(check_answer)
    
def generate_mc_no_answer(answers,question):
    out = widgets.Output()
    alternativ = widgets.RadioButtons(
    options=answers,
    description='',
    layout=widgets.Layout(width='1500px'),
    disabled=False)
    
    print('\033[1m',question,'\033[0m')
    display(alternativ) 
    display(out)
    return alternativ

def generate_multiple_no_answer(filename): #Tar inn tekst med linjer på formatet spørsmål£alternativ1£alternativ2osv
    f = open(filename,"r",encoding="UTF-8")
    lines = f.readlines()
    f.close()
    #buttons = []
    for line in lines:
        line = line.split("£")
        question = line[0]
        answers = line[1:]
        generate_mc_no_answer(answers,question)
        #buttons.append(generate_mc_no_answer(answers,question))
   # button = widgets.Button(description="Lagre svar")
   # display(button)
    """def save_answers(b):
        saved_answers = []
        for radiobutton in buttons:
            saved_answers.append(radiobutton.value)
    button.on_click(save_answers)"""
    
def generate_multiple(filename): #Tar inn tekst på formatet spørsmål, antall alternativer, [alternativer], rett svar (tall)
    f = open(filename,"r",encoding="UTF-8")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split(",")
        question = line[0]
        answers = []
        for answer in line[2:2+int(line[1])]:
            answers.append(answer)
        generate_mc(answers,question,int(line[len(line)-1]))
        
        
def generate_multiple1(filename): #Tar inn tekst på formatet spørsmål, rett svar (streng), [andre alternativer]
    f = open(filename,"r",encoding="UTF-8")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split(",")
        question = line[0]
        answer = line[1]
        answers = line[2:]+[answer]
        generate_mc(answers,question,len(answers))
        
        
def generate_multiple3(filename): #her er førstelinje alle svarene på form f.eks abbcdd...
                                  #neste linjer: spørsmål£alternativ1£alternativ2osv
    f = open(filename,"r",encoding="UTF-8")
    lines = f.readlines()
    f.close()
    correct_answers=[]
    for letter in lines[0]:
        correct_answers.append(ord(letter) - 96)
    for i in range(1,len(lines)-1):
        line = lines[i].split("£")
        question = line[0]
        answers = line[1:]
        generate_mc(answers,question,correct_answers[i-1])

module_path = os.path.abspath(os.path.join('../..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    

generate_multiple_no_answer('eksamen2012teori.txt')


# ## Oppgave 2 -  Grunnleggende programmering (20%)

# ***I denne versjonen har vi fjernet fjervalgsoppgavene som til vanlig teller 25% av eksamen. Topp prosentscore er da altså 75%.***
# 
# Du kan anta at alle fuksjonene mottar gyldige input-verdier.

# ### Oppgave 2 a) (5%)

# Lag funksjonen **summerOlympics** som har inn-parametere **firstYear** og **lastYear**. Funksjonen skal returnere variabelen **years**,som er ei list emed alle OL-årene fra og med **firstYear** til og med **lastYear** (inkludert framtidige planlagte år for sommer-OL). Fra og med OL i London i 1948,har sommer-OL vært arrangert hvert fjerde år. Du kan anta at **firstYear** ≥ 1948.
# 
# Eksempel på kjøring av funksjonen og hva den returnerer:
# 
# ```python
# >>>years = summerOlympics(1999,2012)
# >>> years
# [2000, 2004, 2008, 2012]
# >>>```

# In[2]:


def summerOlympics(firstYear,lastYear):
    liste = []
    for i in range(1948, (lastYear+1), 4):
        if i >= firstYear:
            liste.append(i)
    return liste

    

years = summerOlympics(1999,2012)

print(years)


# ### Oppgave 2b) (7.5%)

# Lag funksjonen **`findAge`** som har inn-parametere **bYear**, **bMonth**, **bDay** som er tre heltall som beskriver dato for en fødselsdag. Funksjonen skal returnere **age** som beskriver hvor gammel en person med oppgitt fødselsdag (**bYear**, **bMonth** og **bDay**) er i dag angitt i hele år.
# 
# For å finne år, måned og dag for i dag ***skal du bruke*** en eksisterende funksjon som heter `current_date()`.Funksjonen returnerer tre heltall på formatet **(yyyy,mm,dd)**. 
# 
# Eksempel på bruk av funksjonen **current_date**:  
# `(yyyy,mm,dd)= current_date()` gir i dag yyyy=2012,mm=12, dd=11.
# 
# Eksempel på kjøring av funksjonen **`findAge`** og hva den returnerer:
# 
# ```python
# >>> age = findAge(2000,12,15)
# >>> age
# 11
# >>>
# ```

# In[39]:


from datetime import datetime
def current_date():
    yyyy = int(datetime.today().strftime('%Y'))
    mm = int(datetime.today().strftime('%m'))
    dd = int(datetime.today().strftime('%d'))
    return yyyy,mm,dd
print(current_date())


# In[42]:


def findAge(bYear,bMonth,bDay):
    age = current_date()[0] - bYear
    
    if current_date()[1] < bMonth:
        age -= 1
    elif current_date()[1] == bMonth and current_date()[2] < bDay:
        age -= 1
    return age

age = findAge(2000,12,15)
print(age)


# ### Oppgave 2c) (7.5 %)

# Lag en funksjon **`printAgeDiff`** som tar en parameter **table**,som er en to-dimensjonal tabell (liste av lister) der hver rekke beskriver personer med fornavn, etternavn, fødselsår, fødselsmåned og fødselsdato. Funksjonen skal bruke funksjonen **`findAge`** fra oppgave 2b til å sammenlikne alderen i hele år på etterfølgende personer i tabellen (rekke for rekke) og gjøre følgende:
# 
# * Hvis person n og person n+1 har samme alder angitt i antall hele år, skal følgende skrives ut til skjerm:  
# ``<fornavnn> <etternavnn> is at the same age as <fornavnn+1> <etternavnn+1>``
# * Hvis person n er eldre enn person n+1 angitt i antall hele år, skal følgende skrives ut til skjerm:  
# ``<fornavnn> <etternavnn> is older than <fornavnn+1> <etternavn n+1>``
# * Hvis person n er yngre enn person n+1 angitt i antall hele år, skal følgende skrives ut til skjerm:  
# ``<fornavnn> <etternavnn> is younger than <fornavnn+1> <etternavnn+1>``
# 
# Eksempel på en to-dimensjonal tabell som beskriver fire kjente personer:

# In[43]:


table=[['Justin','Bieber',1994,3,1],
       ['Donald','Duck',1934,8,1],
       ['George','Clooney',1961,5,6],
       ['Eddie','Murphy',1961,4,3]]


# Eksempel på kjøring av funksjonen **`printAgeDiff`** med tabellen **table**, som inneholder listene for bieber, donald, george og eddie:
# 
# ```python
# >>>printAgeDiff(table)
# Justin Bieber is younger than Donald Duck
# Donald Duck is older than George Clooney
# George Clooney is at the same age as Eddie Murphy
# >>>```

# In[49]:


def printAgeDiff(table):
    i=0
    while i+1 < len(table):
        age = findAge(table[i][2],table[i][3],table[i][4])
        if age == findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
            print("{0} {1} is at the same age as {2} {3}".format(table[i][0],table[i][1],table[i+1][0],table[i+1][1]))
        elif age > findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
            print("{0} {1} is older than {2} {3}".format(table[i][0],table[i][1],table[i+1][0],table[i+1][1]))
        elif age < findAge(table[i+1][2],table[i+1][3],table[i+1][4]):
            print("{0} {1} is younger than {2} {3}".format(table[i][0],table[i][1],table[i+1][0],table[i+1][1]))
        i+=1
        
    
printAgeDiff(table)
    


# ## Oppgave 3 - Kodeforståelse (15%)

# ### Oppgave 3a) (5%)

# Hva returneres hvis funksjonen `fu1(1234)`med kode som vist under kjøres?
# 
# ```python
# def fu1(a):
#     r = 0
#     while(a>0):
#         s = a%10
#         r = r + s
#         a = (a-s)/10
# return r```

# Svar: <dobbeltklikk for å svare>

# ### Oppgave 3b) (5%)

# Hva blir verdiene til a,b,c og d etter kallet  
# `(a, b, c, d) = fu2(’Ut pa tur, aldri sur’)`  
# med koden som vist under?
# 
# ```python
#     def fu2(input):
#         r = 0
#         s = 0
#         t = 0
#         u = 0
#         n = len(input)
#         for c in input:
#             if(c.isalpha()):
#                 r = r + 1
#             elif(c.isdigit()):
#                 s = s + 1
#             elif(c==' '):
#                 t = t + 1
#             else:
#                 u = u + 1
#         r = 100*r/n
#         s = 100*s/n
#         t = 100*t/n
#         u = 100*u/n
#         return(r,s,t,u)
#     ```

# Svar: <dobbeltklikk for å svare>

# ### Oppgave 3c) (5%)

# Hva returneres av kallet `fu3(100)`med koden som vist under?
# ```python
# def fu3(a):
#     if(a<=2):
#         r = 1
#     else:
#         r = 1 + fu3(a/2)
#     return r
#     ```

# Svar: 1 + 100/2 + 1 + 50/2 + 1 + 25/2 + 1 + osv

# ## Oppgave 4 - Programmering (40%)

# Denne oppgaven fokuserer på behandling av data fra fire vær sensorer som måler en verdi per døgn av følgende data:
# 
# * Temperatur: Angis som heltall i Celsius fra -50C til + 50C
# * Nedbør: Angis som heltall i mm nedbør per døgn fra 0 til 2000mm
# * Luftfuktighet. Angis som heltall fra 0 til 100%
# * Vindstyrke: Angis som heltall fra 0 til 50 meter per sekund
# 
# Hvis ikke noe annet er oppgitt kan du anta korrekt input til funksjonene.

# ### Oppgave 4a) (5%)

# Lag en funksjon **`cold_days`** som tar imot parameteren **templist**, som en liste av temperaturer, og returnerer variabelen **days**,som angir antall døgn der temperaturen var under 0 grader.
# 
# Eksempel på kall av funksjonen og hva den returnerer:
# ```python
# >>> days = cold_days([1,-5,3,0,-6,-3,15,0])
# >>> days
# 3
# >>>
# ```

# In[5]:


def cold_days(templist):
    i=0
    days=0
    
    while i < len(templist):
        if templist[i] < 0:
            days += 1
        i += 1
    return days

cold_days([1,-5,3,0,-6,-3,15,0])
        


# ### Oppgave 4 b) (5 %)

# Lag en funksjon **`cap_data`** som har inn-parameterne **array** (liste med data), **min_value** (minimumsverdi) og **max_value** (maksimumsverdi). Funksjonen skal returnere ei ny liste **result** der alle elementer i lista **array** som har verdi mindre enn **min_value** skal settes lik **min_value** og alle elementer i lista **array** som har verdi høyere enn **max_value** skal settes lik **max_value**.
# 
# Eksempel på kall av funksjonen og hva den returnerer:
# ```python
# >>>A=[-70,30,0,90,23,-12,95,12]
# >>>result = cap_data(A,-50,50)
# >>>result
# [-50,30,0,50,23,-12,50,12]
# >>>```
# 
# Legg merke til hvilke verdier som endres.

# In[6]:


def cap_data(array, min_value, max_value):
    i=0
    result = []
    
    while i < len(array):
        if array[i] < min_value:
            array[i] = min_value
        if array[i] > max_value:
            array[i] = max_value
        result.append(array[i])
        i += 1
    
    return result

A=[-70,30,0,90,23,-12,95,12]
result = cap_data(A,-50,50)
print(result)


# ### Oppgave 4c) (10%)

# Lag en funksjon **`generate_testdatasom`** har inn-parameterne **N**, **min_value** (minimumsverdi)og **max_value** (maksimumsverdi). Funksjonen skal returnere tabellen **result** som består av **N** unike *tall* (heltall) som blir trukket tilfeldig der {**min_value** ≤ *tall* ≤ **max_value**}. Unik betyr her at ingen elementer i tabellen **result** skal ha samme verdi. Du kan anta at antall mulige verdier i intervallet tallet blir trukket fra alltid vil være større enn **N**.
# 
# Eksempel på kall av funksjonen og hva den returnerer:
# ```python
# >>> result = generate_testdata(10,-5,10)
# >>> result
# [-5,3,7,9,-3,4,2,0,-1,5]
# >>>```

# In[7]:


from random import randint

def generate_testdata(N, min_value, max_value):
    result=[]
    for i in range(N):
        value = randint(min_value, (max_value))
        result.append(value)
    return result

result = generate_testdata(10,-5,10)
print(result)


# ### Oppgave 4d) (5%)

# Lag en funksjon **`create_db`** som har inn-parameterne **temp**, **rain**, **humidity** og **wind**,som er fire tabeller av samme størrelse (likt antall elementer) med data for temperatur, nedbør, luftfuktighet og vind.
# 
# Funksjonen skal lage og returnere *dictionarien* **weather**,der nøkkelen er ett heltall som starter med verdien 1 og teller oppover (representerer dagen for måling). Hvert innslag i *dictionarien* skal være en liste av verdier for temperatur, nedbør, luftfuktighet og vind. Verdiene for **weather** med nøkkel 1 skal inneholde værdata for dag 1, **weather** med nøkkel2 skal inneholde værdata for dag 2 og så videre.
# 
# Eksempel på kall av funksjonen og hva den returnerer:
# ```python
# >>> temp = [1,5,3]
# >>> rain = [0,30,120]
# >>> humidity = [30,50,65]
# >>> wind = [3,5,7]
# >>> weather = create_db(temp,rain,humidity,wind)
# >>> weather
# {1: [1, 0, 30, 3], 2: [5, 30, 50, 5], 3: [3, 120, 65, 7]}
# >>>
# ``` 

# In[20]:


def create_db(temp,rain,humidity,wind):
    i=0
    weather = {}
    while i < len(temp):
        weather[(i+1)] = [temp[i],rain[i],humidity[i],wind[i]]
        i +=1
    return weather    

temp = [1,5,3]
rain = [0,30,120]
humidity = [30,50,65]
wind = [3,5,7]
weather = create_db(temp,rain,humidity,wind)
print(weather)


# ### Oppgave 4e) (5%)

# Lag en funksjon **`print_db`** som har inn-parameteren **weather**,som er en dictionary som beskrevet i oppgave 4d. Funksjonen skal skrive ut innholdet i **weather** på skjerm etter følgende format og med overskrift som vist på utskriften nederst i deloppgaven:
# * Day(dag) –høyrejustert med 4 tegn
# * Temp (temperatur)–høyrejustert med 6 tegn
# * Rain (nedbør)–høyrejustert med 6 tegn
# * Humidity (luftfuktighet)–høyrejustert med 10 tegn
# * Wind (vind)–høyrejustert med 6 tegn
# 
# Eksempel på kall av funksjonen ved bruk av dictionarien fra oppgave 4d:
# ```p
# >>> print_db(weather)
# Day | Temp | rain | humidity | wind
# ====+======+======+==========+======
#    1      1      0         30      5
#    2      5     30         50      3
#    3      3    120         65      7
# >>>
# ```

# In[38]:


def print_db(weather):
    print("{:<4}|{:^6}|{:^6}|{:^10}|{:>5}".format("Day","Temp","rain","humidity","wind"))
    print("{}+{}+{}+{}+{}".format("====","======","======","==========","======"))
    i=1
    for key,values in weather.items():
        dag = weather[key]
        print("{:>4}{:>7}{:>7}{:>11}{:>7}".format(i,dag[0],dag[1],dag[2],dag[3])) 
        i+=1

        
print_db(weather)


# ### Oppgave 4f) (10%)

# Lag funksjonen **`strange_weather`** som har inn-parameterne **temp** og **rain**,som er to tabeller med data for temperaturer og regn av lik størrelse (samme antall elementer). Funksjonen skal returnere **start** (startdag)og **stop** (sluttdag)for det lengste intervallet der det er minusgrader, samt at temperaturen faller samtidig som nedbørsmengden stiger i etterfølgende dager. Indekseringen av dager starter på 1. Hvis ingen etterfølgende dager har denne karakteristikken, returneres (0,0).
# 
# Eksempel på kall av funksjonen(med intervall som oppfyller kravet uthevet):
# ```python
# >>> temp=[1,3, 4,-5,-6,-7,-8,-9,3,0]
# >>> rain=[0,20,30,0,10,30,50,0,5,2]
# >>> (start, stop) = strange_weather(temp,rain)
# >>> start
# 4
# >>> stop
# 7
# >>>
# ```

# In[39]:


def strange_weather(temp, rain):
    counter_list=[]
    i = 0
    while i < len(temp):
        index_counter = 0
        x = i
        while temp[x] < 0 and temp[x+1] < temp[x] and rain[x+1] > rain[x]:
            index_counter +=1
            x+=1
        counter_list.append(index_counter)
        i+=1
        
    print(counter_list)
    riktig_liste = counter_list[::-1] # Måtte reversere listen for at den skulle bli korrekt med eksempelet?
    print(riktig_liste)
    stop_indeks = max(riktig_liste) # Gir høyeste verdi
    stop = riktig_liste.index(stop_indeks) + 1 # Finner hvor høyeste verdi ligger, legger til +1 til index.
    start = (stop_indeks+1) - index_counter #indeks-verdi - counter-verdi
    return start, stop

temp = [1,3, 4,-5,-6,-7,-8,-9,3,0]
rain = [0,20,30,0,10,30,50,0,5,2]
(start, stop) = strange_weather(temp,rain)
print(start)
print(stop)
        

