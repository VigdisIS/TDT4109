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
#     <li class="active"><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li ><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li ><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li ><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Vektorer
# 
# **Læringsmål:**
# 
# * Lister
# 
# **Starting Out with Python:**
# 
# * Kap. 7.1-7.3
# 
# I denne oppgaven skal vi studere lister bestående av tall, dvs. en vektor. Videre skal vi studere prikkprodukt og skalering av vektorer. 
# 
# En liste kan brukes til å representere en matematisk vektor.
# En av forskjellene mellom lister og vektorer er at lister kan inneholde elementer av forskjellige typer (f.eks både tall og strenger). I denne oppgaven skal du bruke lister til å implementere tredimensjonale vektorer, altså vektorer med tre elementer.
# 
# **En vektor x=(x,y,z) har lengde $\sqrt{x^{2}+y^{2}+z^{2}}$. Den kan multipliseres med tall, og vektormultipliseres med andre vektorer.**
# 
# Multiplikasjon med tall, også kalt skalarmultiplikasjon, ganger hver komponent i vektoren med et tall (skalar).
# 
# Prikkprodukt er multiplikasjon av to vektorer med samme lengde. Prikkprodukt og skalarmultiplikasjon er forklart i Eksempel 1.
# 
# Eksempel 1:
# 
# ```python
# Prikkprodukt:
# u*v = u1*v1 + v2*u2 + v3*u3, hvor v = [v1,v2,v3] og u = [u1,u2,u3]
# Numerisk eksempel:
# [3,7,1]*[2,-4,8]=3*2+7*(-4)+1*8=-14
# ```
# ```python
# Skalarmultiplikasjon:
# c*[v1,v2,v3] = [c*v1,c*v2,c*v3]
# Numerisk eksempel:
# 2*[3,7,1] = [6,14,2]
# ```
# 
# Gjennom oppgave a til f skal du lage et program som bruker forskjellige funksjoner til å gjøre forskjellige beregninger på vektorer.

# ### a)

# Lag en funksjon som lager en liste med 3 elementer, hvor alle elementene er heltall f.o.m. -10 t.o.m. 10, og returnerer denne. Benytt deg av random-biblioteket.
# 
# Eksempel på kjøring
# 
# ```python
# >>>print(make_vec())
# [0, -9, 5]
# ```
# ***Skriv svaret ditt i boksen under.***

# In[10]:


from random import randint

def make_vec():
    return [randint(-10,10),randint(-10,10),randint(-10,10)]

print(make_vec())


# ### b)

# Lag en funksjon som tar inn en liste/vektor og et navn til denne vektoren som argumenter. Funksjonen skal skrive ut vektoren på en vakker måte.
# 
# Eksempel på utskrift:
# ```python
# >>>vector_print([1.20,4.50,4.40],'vec1')
# vec1 = [1.20, 4.50, 4.40]
# ```
# ***Skriv svaret ditt i boksen under.***

# In[19]:


def vector_print(vektor, navn):
    print(navn, "=", vektor)

vector_print([1.20,4.50,4.40],'vec1')


# ### c)

# Lag en funksjon `scalar_mult(liste,skalar)` som tar inn en liste/vektor og en skalar som argumenter. Skalarmultipliserer vektoren og returnerer den nye vektoren, liste2. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[23]:


def scalar_mult(liste,skalar):
    liste2 = [i * skalar for i in liste]
    return liste2
    
    


# Dersom du har gjort det riktig skal kodesnutten under printe lista **[4.8, 18.0, 17.6]**. Trykk `ctrl + enter` for å kjøre testen.

# In[24]:


print(scalar_mult([1.2,4.5,4.4],4))


# ### d)

# Lag en funksjon `vec_len(vektor)` som tar inn en vektor som argument, og regner ut og returnerer dens lengde. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[29]:


from math import sqrt

def vec_len(vektor):
    vektor = [i**2 for i in vektor]
    return sqrt(sum(vektor))

    


# Dersom du har gjort det riktig skal kodesnutten under printe tallet **5.0990195135927845**

# In[30]:


print(vec_len([1,4,3]))


# ### e)

# Lag en funksjon `vector_dot_product(vec1,vec2)` som tar inn to vektorer som argumenter og returnerer indreproduktet/prikkproduktet av de to vektorene. 
# Du kan gå ut ifra at vektorene har lik lengde. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[40]:


def vector_dot_product(vec1,vec2):
    prikkprodukt = [a*b for a,b in zip(vec1,vec2)]
    return sum(prikkprodukt)


# Dersom du har gjort det riktig skal koden under printe **29.400**

# In[41]:


vec1 = [1, 4, 3]
vec2 = [2, 3.1, 5]
print(vector_dot_product(vec1,vec2))


# ### f)

# Lag en main-funksjon som:
# 
# 1. Oppretter en vektor med 3 elementer (vec1).
# 2. Skriver ut vektoren på fin form.
# 3. Tar inn en skalar fra bruker. (Skal kunne ta inn både heltall og flyttall.)
# 4. Skriver ut lengden til vektoren før og etter skalering med to desimaler.
# 5. Skriver ut forholdet mellom de to lengdene. (Forholdet bør være lik skalaren.)
# 6. Skriver ut prikkproduktet mellom vektoren før skalering og vektoren etter skalering. Dvs. prikkproduktet mellom vec1 og (vec1*skalar), altså vec1*(vec1*skalar).
# 
# Eksempel på kjøring:
# 
# ```python
# vec1 = [9, 3, 0]
# Skriv inn en skalar: 2.5
# Lengden før skalering er: 9.49
# Lengden etter skalering er: 23.72
# Forholdet mellom lengden før og etter skalering er: 2.5
# Prikkproduktet av [9, 3, 0] og [22.5, 7.5, 0.0] er: 225.0
# ```
# 
# ***Skriv svaret ditt i boksen under.***

# In[56]:


def main():
    vec1 = make_vec()
    vector_print(vec1,'vec1')
    skalar = float(input("Skriv inn en skalar: "))
    print("Lengden før skalering er: {0:.2f}".format(round(vec_len(vec1),2)))
    print("Lengden etter skalering er: {0:.2f}".format(round(vec_len(scalar_mult(vec1,skalar))),2))
    print("Forholdet mellom lengden før og etter skalering er:", ((vec_len(scalar_mult(vec1,skalar)))/(vec_len(vec1))))
    print("Prikkproduktet av", vec1, "og", scalar_mult(vec1,skalar), "er:", vector_dot_product(vec1,scalar_mult(vec1,skalar)))
    
main()

