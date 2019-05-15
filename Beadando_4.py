import datetime
def mikulas(date):
    d=datetime.datetime(2019,12,6)
    x = lambda a, b : ((b.year*365)+(b.month*30)+(b.day*1))-((a.year*365)+(a.month*30)+(a.day*1))
    return x(date,d)
year=int(input('Add meg az évet: '))
month=int(input('Add meg a hónapot: '))
day=int(input('Add meg a napot: '))
date=datetime.date(year,month,day)
print(date)
print(mikulas(date),"napot kell aludni mikulásig.")