#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving10.ipynb">Øving 10</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li class="active"><a href="Rekursjon.ipynb">Rekursjon (Obligatorisk TDT4109)</a></li>
#     <li ><a href="Matplotlib.ipynb">Matplotlib (Obligatorisk TDT4110)</a></li>
#     <li ><a href="Eksamen%202012.ipynb">Eksamen Python 2012</a></li>
#     <li ><a href="Sudoku.ipynb">Sudoku</a></li>
#     <li ><a href="numpy-arrays%20og%20matplotlib.ipynb">Numpy-arrays og matplotlib (TDT4110)</a></li>
#     <li ><a href="Bokanalyse%20med%20plotting.ipynb">Bokanalyse med plotting (TDT4110)</a></li>
#     <li ><a href="Sjakk.ipynb">Sjakk</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Rekursjon
# 
# **Læringsmål:**
# 
# * Rekursjon
# * Algoritmer
# 
# **Starting Out with Python:**
# 
# * Kap. 12: Recursion

# ### Rekursjon, hva er det?

# Dersom en funksjon kaller på seg selv kaller vi dette for rekursjon. Rekursjon er et viktig konsept innenfor datateknologi, og det er en mye brukt teknikk for å løse problemer som kan deles opp i mindre tilsvarende subproblemer. For eksempel bygger en rekke søkealgoritmer på konseptet rekursjon.
# 
# ![img](./../../Resources/Images/fixing_problems.webp)
# 
# La oss begynne å se på en veldig enkel funksjon som benytter seg av rekursjon, som nevnt betyr dette bare at funksjonen kaller seg selv.
# 
# **Eksempel:**

# In[1]:


def teller(nummer=0):
    print("Nå har vi kommet til: ", nummer)
    teller(nummer + 1)
    
teller()


# Her ser vi en teller implementert rekursivt. Funksjonen begynner å telle fra null, siden det er standardverdien vi har gitt, før den kaller seg selv på nytt, men denne gangen med økt verdi. Vi kan også lage en funksjon med samme funksjonalitet iterativt, ved hjelp av løkker. Funksjonen under vil gjøre akkurat det samme som vår rekursive teller.

# In[ ]:


def teller2():
    nummer = 0
    while True:
        print("Nå har vi kommet til: ", nummer)
        nummer += 1
        
teller()


# Men, som du kanskje har lagt merke til, har vår rekursive funksjon en stor svakhet, den slutter aldri. Funksjonen vår vil fortsette å telle helt til vi får en RecursionError, hvor vi får beskjed om at maksimum rekursjons dybde er nådd. Vi kan se på det som at hver gang vi kaller en rekursiv funksjon graver vi oss lengre ned i et hull, og Python setter en grense for hvor langt ned vi kan grave, forhåpentligvis ønsker vi å komme oss opp igjen av hullet også, men det ser vi på litt senere. Først la oss fokusere på at funksjonen vår aldri avslutter.
# 
# Rekursive funksjoner trenger det vi kaller vi et **grunntilfelle**, et sted hvor koden innser at det er på tide å slutte. La oss prøve å endre telleren slik at den slutter å telle når den kommer til 10.

# In[3]:


def teller(nummer=0):
    print("Nå har vi kommet til: ", nummer)
    if(nummer<10):
        teller(nummer + 1)
        
teller()


# Som du nå selv kan teste, vil funksjonen vår telle til 10, før den gir seg. Vi har et tilfelle hvor funksjonen finner ut at den skal stoppe, og vi slipper at Python skal gi oss en streng beskjed om at vi må slutte å kalle funksjonen vår. Tidligere nevnte vi også ambisjoner om å klatre opp igjen fra hullet vi har laget oss, så la oss først ta en kikk på en klassiskt bruksområde når det kommer til rekursjon, nemlig hvordan vi kan regne fakultet:

# In[4]:


def fakultet(tall):
    if tall==0:
        return 1
    else:
        return tall*fakultet(tall-1)

fakultet(5)


# Her baserer vi oss på grunntilfellet hvor null fakultet er lik 1. Ellers vet vi at fakultet av et tall er lik tallet selv gange fakultet av tallet selv minus en. Altså f.eks. er 5! = 5 * 4!. Det kan vi enkelt løse rekursivt, som vi allerede har gjort. Det som er nytt for dette eksempelet er at vi faktisk benytter oss av resultatet av funksjonskallene våre. Når vi kaller funksjonen med tallet 3 vil følgende skje:
# 
# > Vi prøver å regne ut 3! men siden vi trenger 2! kaller vi funksjonen på nytt.  
# Vi prøver å regne ut 2! men siden vi trenger 1! kaller vi funksjonen på nytt.  
# Vi prøver å regne ut 1! men siden vi trenger 0! kaller vi funksjonen på nytt.  
# Vi prøver å regne ut 0!, det vet vi er 1.   
# Vi benytter oss av resultatet over, finner ut at 1! er 1.  
# Vi benytter oss av resultatet over, finner ut at 2! er 2.  
# Vi benytter oss av resultatet over, finner ut at 3! er 6.  
# 
# Hvis vi fortsetter å tenke på grave-eksempelet kan vi se at vi over har to faser, en hvor vi kaller funksjonen på nytt og graver oss ned, før vi omsider finner bunnen og klatrer opp igjen. Ved å trykke [her](http://pythontutor.com/visualize.html#code=def%20fakultet%28tall%29%3A%0A%20%20%20%20if%20tall%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20tall*fakultet%28tall-1%29%0A%0Afakultet%285%29&cumulative=false&curInstr=26&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) kan du få visualisert hvordan vi regner ut fakultet av fem steg for steg.
# 

# La oss ta en kikk på en nytt eksempel men denne gangen skal vi bruke en liste, hvor vi ønsker å summere alle elementene rekursivt. Som nevnt introduksjonsmessig er rekursivitet brukt mye i sorteringsalgoritmer, og selv om det ofte kan virke som om det vi gjør rekursivt alltid kan gjøres iterativt, er ikke det alltid tilfelle. Rekursjon er derfor viktig å forstå, selv om det også er vanskelig.

# In[5]:


def liste_sum(liste):
    if(len(liste)==1):
        return liste[0] #dersom listen kun har et element er summen vår bare det ene elementet
    else:
        return liste[0]+liste_sum(liste[1:]) #ellers tar vi det første elementet og legger til summen av resten av lista
    
liste_sum([1,2,3])


# Det er kanskje ikke så mye nytt her med unntak av at vi denne gangen fokuserer på en liste, men la oss også nå se steg for seg hva som skjer.
# 
# > Vi vil ha summen av [1,2,3], vi vet dette er 1 + summen av [2,3], vi kaller funksjonen på nytt  
# Vi vil ha summen av [2,3], vi vet dette er 2 + summen av [3], vi kaller funksjonen på nytt  
# Vi vet at summen av [3] er 3, så vi gir verdien til funksjons-kallet over.  
# Siden summen av [3] var 3, er summen [2,3] = 2 + 3 = 5  
# Siden summen av [2,3] var 5, er summen av [1,2,3] = 1 + 5 = 6.   
# 
# Det ligner mye på det vi gjorde når vi implementerte fakultet, vi jobber oss nedover, når bunnen, og går tilbake opp. Trykk [her](http://pythontutor.com/visualize.html#code=def%20liste_sum%28liste%29%3A%0A%20%20%20%20if%28len%28liste%29%3D%3D1%29%3A%0A%20%20%20%20%20%20%20%20return%20liste%5B0%5D%20%23dersom%20listen%20kun%20har%20et%20element%20er%20summen%20v%C3%A5r%20bare%20det%20ene%20elementet%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20liste%5B0%5D%2Bliste_sum%28liste%5B1%3A%5D%29%20%23ellers%20tar%20vi%20det%20f%C3%B8rste%20elementet%20og%20legger%20til%20summen%20av%20resten%20av%20lista%0A%20%20%20%20%0Aliste_sum%28%5B1,2,3%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) for en visualisering.
# 
# Nå har du fått en rask innføring i hvordan programmere rekursivt. Hvis du vil ha en litt annen innføring i temaet kan du sjekke ut [denne linken](https://realpython.com/python-thinking-recursively/). 

# ### a) Rekursiv sum

# Skriv en funksjon `recursive_sum(n)` som tar inn et heltall n og regner summen av  1+2+...+n ved hjelp av rekursjon. 
# 
# **Eksempel på kjøring:**
# ```python
# >>>print(recursive_sum(53))
# 1431
# ```

# In[9]:


def recursive_sum(n):
    while n >= 1:
        return n+recursive_sum(n-1)
    return n

print(recursive_sum(53))
    


# #### Hint

# Se på eksempelet med fakultet i tutorialen.

# ### b) Merge sum

# Skriv en funksjon `merge_sum(liste)` som summerer alle elementene i en liste men på en litt annen måte enn i tutorialen. 
# 
# * Anta et partall antall elementer i lista.
# * Når du skal summere elementene skal det gjøres ved å dele lista i to, og så addere summen av hver halvdel av listen. 

# In[5]:


def merge_sum(liste):
    half = len(liste)//2
    halv_1 = liste[half:]
    halv_2 = liste[:half]
    if len(liste) == 1:
        return liste[0]
    else:
        return merge_sum(halv_1) + merge_sum(halv_2)

merge_sum([1,2,3,4])
    


# #### Hint

# Tenk på grunntilfellet og hva funksjonen skal returnere.  
# Hvor skal vi dele lista?

# ### c) Minste element

# Skriv en rekursiv funksjon `find_smallest_element(numbers)` som tar inn en liste numbers med heltall og finner det minste elementet i listen. 
# *Merk: Du kan ikke bruke innebygde funksjoner i Python som min(liste), for å løse denne oppgaven.*
# 
# ```python
# >>>print(find_smallest_element([5,3,2,6]))
# 2
# ```

# In[25]:


def find_smallest_element(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return min(numbers[0], find_smallest_element(numbers[1:]))

print(find_smallest_element([5,3,2,6]))


# #### Hint

# Ta en kikk på eksempelet med listesum i tutorialen. Her vil du kunne buke en lignende framgangsmåte, men med en litt annen logikk.

# ### d) Binærsøk

# Skriv en rekursiv funksjon `binary_search(numbers, element)` som tar inn en sortert liste **numbers** med heltall og et heltall **element** og returnerer posisjonen(indeksen) til elementet dersom det finnes i listen. Hvis det ikke finnes skal funksjonen returnere minus uendelig (**-float('inf')**). Dette skal du gjøre ved å benytte deg av [binærsøk-algoritmen](https://en.wikipedia.org/wiki/Binary_search_algorithm). 
# 
# Du kan også implementere funksjonen `binary_search(numbers, element, minimum, maximum)`, altså samme funksjon, med samme funksjonalitet, men med parameterene **minimum** og **maximum**, som vi kan bruke til å angi indeksene vi søker på i lista.
# 
# *Merk: I denne oppgaven er det ikke lov til å bruke innebygde funksjoner i Python som liste.index(element).* 
# 
# **BONUS**: Hvis listen numbers inneholder n elementer, hvor mange funksjonskall vil binærsøk-algoritmen i worst case trenge for å finne posisjonen til elementet i listen? (eller at elementet ikke er i listen)

# In[31]:


def binary_search(numbers, minimum, maximum, element): 
  
    # Sjekker base case
    if maximum >= minimum: 
  
        mid = int(minimum + (maximum - minimum)/2)
  
        # Hvis elementet er i midten
        if numbers[mid] == element: 
            return mid 
          
        # Hvis elementet er mindre enn mid, må det være på venstre side i lista 
        elif numbers[mid] > element: 
            return binary_search(numbers, minimum, mid-1, element) 
  
        # Hvis elementet er større enn min, må det være på høyre side i lista
        else: 
            return binary_search(numbers, mid+1, maximum, element) 
  
    else: 
        # Hvis elementet ikke er i arrayen 
        return -float('inf')

numbers = [ 2, 3, 4, 10, 40 ] 
element = 10
  
result = binary_search(numbers, 0, len(arr)-1, element) 
print(result)


# #### Hint

# Tenk på midterste element.
