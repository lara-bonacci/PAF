

import matplotlib.pyplot as plt


def pravac(točka1,točka2):
    k=(int(točka2[1])-int(točka1[1]))/(int(točka2[0])-int(točka1[0]))
    out=input("prikazati graf na ekranu (napisati e) ili spremiti u pdf (napisati p): ")
    x=[int(točka2[0]),int(točka1[0])]
    y=[int(točka2[1]),int(točka1[1])]
    if out=="e":
          plt.plot(x,y)
          plt.figure()
          plt.show()
    else: 
          plt.plot(x,y)
          plt.savefig("pravac.pdf")
          plt.show()

          
    

T1=input("upišite x,y koordinate za prvu točku: ").split(",")
T2=input("upišite x,y koordinate za drugu točku: ").split(",")


if len(T1)<2:
       T1=input("pogrešan upis. upišite koordinate prve točke obliku x,y: ")

if len(T2)<2:
       T2=input("pogrešan upis. upišite koordinate druge točke obliku x,y:")


pravac(T1,T2)
