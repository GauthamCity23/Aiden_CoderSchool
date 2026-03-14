a = int(input("Plz enter a number 1-100: "))
q = 25
n = 10
d = 5
p =1
count = 0
r = 0
qused = 0
dused = 0
nused = 0
pused = 0

qused = a//q 
a = a-(q*qused)
nused = a//n
a = a-(n*nused)
dused = a//d
a = a-(d*dused)
pused = a//p
a = a-(p*pused)
count = count+qused+nused+dused+pused
if count > 6:
    print(False)
    print(count)
else:
    print(True)
    print(count)
