"""
un programa que pida al usuario su fecha de nacimiento 
dia, mes y año 
deducir cuantos años tiene 

año bisiesto 

subirlo a git 
comentarlo 
"""
# se importa la libreria para saber el día de hoy 
# from datetime import date

# #función llamada age con un parametro llamado birthdate
# def age(birthdate):
#     # ejemplo de como se imprime la fecha de hoy "2022-05-11"
#     # print(date.today())
#     today = date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age

# born = input("Ingresa tu fecha de cumpleaños con este formato: (2002-04-28): ")

# # print(age(date(2000, 1, 1)))
# print(age(date(born)))

"""
resources: 
https://www.codingem.com/how-to-calculate-age-in-python/
"""

# libreria para la fecha de hoy 
from datetime import datetime

# función para calcular la edad 
# parametros para 
def ageCalculator(years, months, days, year, month, date):
    # por qué se necesita importar de nuevo? 
    import datetime
    # se guarda la fecha de hoy en la variable de today 
    today = datetime.date(years, months, days) 
    dob = datetime.date(year, month, date)
    # total_seconds? 
    years = ((today-dob).total_seconds()/(365.242*24*3600))
    yearsInt = int(years)
    months = (years - yearsInt) * 12
    monthsInt = int(months)
    days = (months - monthsInt) * (365.242/12)
    daysInt = int(days)
    print("You are {0}, {1} months, {2} days old".format(yearsInt, monthsInt, daysInt))

birthdate = input("Enter your birthdate (yyyy-mm-dd): ")
#La función strptime() en Python se usa para formatear y devolver una representación de cadena de fecha y hora.
my_date = datetime.strptime(birthdate, "%Y-%m-%d")
b_year = my_date.year
b_month = my_date.month
b_date = my_date.day
now = datetime.now()
c_year = int(now.strftime("%Y"))
c_month = int(now.strftime("%m"))
c_date = int(now.strftime("%d"))
ageCalculator(c_year, c_month, c_date, b_year, b_month, b_date)


"""
resource: https://technocrash.online/python-projects/python-program-to-calculate-age-in-yearsmonths-and-days/ 
"""





