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
#     <li class="active"><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Kodeforståelse
# 
# **Læringsmål:**
# 
# * Tolke kode
# 
# Koden under kan ikke kjøres, her skal du tenke deg fram til svarene! Ca. 20% av eksamen er kodeforståelse så se på dette som god trening! 

# **a)** Hva skrives ut i koden under?

# ```python
# a=345
# b=''
# while a or b=='':
#     b=str(a%2)+b
#     a=a//2
# print(b)
# ```

# Svar:
# 
# 345%2 gir 1
# a//2 gir 172
# 
# Deretter vil 172%2 gi 0 og slik vil det fortsette.
# 
# Koden vil derfor til slutt printe:
# 101011001

# **b)** Hva skrives ut i koden under?

# ```python
# for x in range(0, 10, 2):
#     print(x, end='')
#     if x%4==0:
#         print( ": Dette tallet går opp i 4-gangern")
#     else:
#         print()
#      ```
#      
# `end=""` gjør at det neste som printes ikke printes en linje under, men at det fortsetter på samme linje.

# Svar:
# 
# range(0, 10, 2) betyr at vi begynner med 0, neste tallet vil være 0 + 2, deretter 2+2 osv.
# 
# koden vil derfor se noe slik ut:
# 
# 0: Dette tallet går opp i 4-gangern
# 2
# 4: Dette tallet går opp i 4-gangern
# 6
# 8: Dette tallet går opp i 4-gangern
# 

# **c)** Hva skrives ut i koden under?

# ```python
# i = 1
# while i<10:
#     i = i*2
# print(i)
# ```

# Svar: 
# 
# Vil først gange sammen i*2 fram til i > 10.
# Vi får da 2,4,8,16
# i blir 16 når i > 10
# 
# Koden gir derfor:
# 16
# 

# **d)** Hva skrives ut i koden under?

# ```python
# i = 1
# j = 3
# while j>0:
#     i = i*2
#     j = j - 1
# print(i)```

# Svar:
# 
# Første rep vil gi j = 3 - 1 = 2
# Andre rep vil gi j = 2 - 1 = 1
# Tredje rep vil gi j = 1 - 1 = 0
# 
# i ganges med 2 = 2, deretter med 2 = 4, deretter med 2 = 8.
# 
# Programmet printer derfor 8

# **e)** Hva skrives ut i koden under?
# 
# ```python
# i = 5
# for x in range(i):
#     for y in range(x+1):
#         print("*", end="")
#     print()```
#     
# Her er det en dobbel løkke, så dette er nok nytt for mange. Prøv likevel! Hvordan fungerer egentlig en løkke i en løkke? Se side 176 i Starting Out with Python.

# Svar: 
# 
# i = 5 og c in range(i) vil si 5 linjer nedover.
# For hver linje legges til en stjerne (x+1).
# Programmet vil derfor printe:
# 
# *
# **
# ***
# ****
# *****
