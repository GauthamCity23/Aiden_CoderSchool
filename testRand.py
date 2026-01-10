import random
a = random.randint(1,100)
p11 = int(input("P1: Plz enter the first number that is between 1 amd 100: "))
while p11 > 100 or p11 < 1:
    p11 = int(input("P1: Plz enter the first number that is between 1 amd 100: "))
p21 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
while p21 > 100 or p21 < 1:
    p21 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
p12 = int(input("P1: Plz enter the third number that is between 1 amd 100: "))
while p12 > 100 or p12 < 1:
    p12 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
p22 = int(input("P1: Plz enter the first number that is between 1 amd 100: "))
while p22> 100 or p22 < 1:
    p22 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
p13 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
while p13 > 100 or p13 < 1:
    p13 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))
p23 = int(input("P1: Plz enter the third number that is between 1 amd 100: "))
while p23 > 100 or p23 < 1:
    p23 = int(input("P2: Plz enter the second number that is between 1 amd 100: "))




p1_guess = abs((p11+p12+p13)/3.0)
p2_guess = abs((p21+p22+p23)/3.0)
if abs(p1_guess - a) < abs(p2_guess - a):
    print ("P1 wins!")
    print("computer guess:"+str(a))
    print("The averege was:"+str(p1_guess))
elif abs(p1_guess - a)  > abs(p2_guess -a):
    print("P2 wins!")
    print("computer guess:"+str(a))
    print("The averege was:"+str(p2_guess))
else:
    print ("Tie")
    print("computer guess:"+str(a))
