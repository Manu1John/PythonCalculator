import datetime
print(datetime.datetime.now())
print(datetime.datetime.today().month)
now=datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
x=datetime.datetime(year=2020,month=6,day=26)
y=datetime.datetime(year=2020,month=5,day=20)
diff=x-y
print(diff)
end=datetime.datetime.now()
comp=end-now
print(comp)



