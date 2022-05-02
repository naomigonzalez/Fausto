"""
un programa que pida al usuario su fecha de nacimiento 
dia, mes y año 
deducir cuantos años tiene 

año bisiesto 

subirlo a git 
comentarlo 
"""

from datetime import date

born = input("Ingresa tu fecha de cumpleaños con este formato: (2002 4 28): ")


today = date.today()
age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
print(age)

"""
resources: 
https://www.codingem.com/how-to-calculate-age-in-python/
"""