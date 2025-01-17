#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li class="active"><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Generelt om filbehandling
# 
# **Læringsmål:**
# - Filbehandling
# - Betingelser
# - Løkker
# 
# **Starting Out with Python:**
# - Kap. 6: Files and Exceptions
# 
# I denne oppgaven skal vi skrive til en fil og lese fra en fil.

# ## Generelt om filer
# Det kan være lurt å lese dette før du går videre

# Det er ofte nyttig å kunne lagre data til en fil, eller lese data fra en fil når man skriver et program i Python. De mest brukte funksjonene er for åpning, redigering og lukking av eksterne filer. 
# 
# Når du åpner filen må du spesifisere hvordan du skal bruke filen. Det er derfor viktig å åpne filen på riktig måte. Måten dette gjøres på er som inn-parameter i `open()`-funksjonen, noen eksempler er:
# 
# - **'r'** - for lesing av filen (default)
# - **'w'** - for skriving til filen
# - **'a'** - for å legge til data (**a**ppend) til den eksisterende filen
# 
# I denne oppgaven skal vi bli bedre kjent med hvordan dette fungerer:
# 
# - For å åpne en fil i Python kan vi skrive: `f = open('filename', Bruksmåte)`. Bruksmåte er enten `'r'`, `'w'` eller `'a'` avhengig av hva hvordan filen skal brukes.
# - For å lese data fra en fil kan vi bruke: `innhold = f.read()`
# - For å legge til data til en fil kan vi skrive: `f.write(data)`
# 
# Filer lukkes på følgende måte: `f.close()`

# ### Lesing av fil

# Eksempelet under viser lesing av en fil. **Kjør koden under og test det ut da vel!**

# In[1]:


# LESING AV FIL
f = open('example_file1.txt','r') #r spesifiserer at man skal lese fra en fil
innhold = f.read()
print(innhold)
f.close()


# Når man leser en fil slik som over, må man lagre innholdet i en variabel (her bruker vi `innhold`). **Husk alltid å lukke filen!**
# 
# Den filen som ble lest fra finner dere her: [example_file1.txt](../../../../edit/itgk-2019-vinger/Ovinger/Oving09/example_file1.txt). Prøv å endre på filen, lagre den med `file -> save` i toppmenyen for så å kjøre kodeblokken over på nytt. Kodeblokken burde da skrive ut det nye innholdet i filen!

# ### Skriving av fil

# For å skrive til en fil kan man gjøre slik som under. **Kjør koden under og test!**

# In[2]:


f = open('example_file1.txt','w')  #w spesifiserer at filen skal skrives til
f.write('En hatefull ytring')
f.close()


# Etter at du har kjørt koden over vil du kunne se at innholdet i [example_file1.txt](../../../../edit/itgk-2019-vinger/Ovinger/Oving09/example_file1.txt) har endret seg. Hvis du vil kan du bytte ut `'w'` over med `'a'` og se hva som da skjer.

# ## a)

# Lag en funksjon `write_to_file(data)` som tar inn strengen `data` og legger denne inn i en fil **my_file.txt**
# 
# ***Skriv din kode i kodeblokken under***

# In[3]:


def write_to_file(data):
    f = open('my_file.txt','w')
    f.write(data)
    f.close()

write_to_file("Epstein did not commit suicide")


# In[ ]:





# Hvis du lurer på om du gjorde riktig kan du kalle på funksjonen og sjekke innholdet i filen her:
# [my_file.txt](../../../../edit/itgk-2019-vinger/Ovinger/Oving09/my_file.txt)

# #### Hint

# Her skal du skrive til fil og må derfor benytte deg av
# 
# ```python
# f = open('my_file.txt', 'w')
# ```

# ## b)

# Lag en funksjon `read_from_file(filename)` som tar inn strengen `filename` med filnavnet og skriver ut innholdet.
# 
# ***Skriv koden i kodeblokken under***

# In[4]:


def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    print(innhold)
    f.close()

read_from_file("my_file.txt")


# Du kan teste ut funksjonen ved å kalle den med `'my_file.txt'` som argument.

# #### Hint

# Her skal du lese fra fil og må derfor benytte deg av
# ```python
# f = open('my_file.txt', 'r')
# ```

# # c)

# Lag en funksjon `main()` hvor bruker får valget mellom å skrive til fil eller lese fra fil. Funksjonen skal kjøre så lenge brukeren ikke svarer `'done'`. (Se eksempelkjøring)
# 
# - Hvis brukeren velger **write** skal du bruke **a)** til å skrive data til **my_file.txt**
# - Hvis brukeren velger **read** skal du skrive ut innholdet (dersom det er noe) i **my_file.txt** vha. **b)**
# 
# **Eksempel på kjøring:**
# ```
# Do you want to read or write? write
# What do you want to write to file? hei allan
# hei allan was written to file.
# Do you want to read or write? read
# hei allan
# Do you want to read or write? done
# You are done.
# ```
# 
# ***Skriv koden din i kodeblokken under***

# In[5]:


def main():
    svar = ""
    while svar != "done":
        svar = input("Do you want to read or write? ")
        if svar == "write":
            svar = input("What do you want to write to file? ")
            write_to_file(svar)
            print(svar, "was written to file.")
        elif svar =="read":
            read_from_file("my_file.txt")
    return "You are done"

main()
            


# Du kan når som helst sjekke innholdet i [my_file.txt](../../../../edit/itgk-2019-vinger/Ovinger/Oving09/my_file.txt)
