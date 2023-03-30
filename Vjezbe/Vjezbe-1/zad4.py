def pravac(točka1,točka2):
    k=(int(točka2[1])-int(točka1[1]))/(int(točka2[0])-int(točka1[0]))
    return "y={}*x+l".format(k)

T1=input("upišite x,y koordinate za prvu točku: ").split(",")
T2=input("upišite x,y koordinate za drugu točku: ").split(",")


if len(T1)<2:
       T1=input("pogrešan upis. upišite koordinate prve točke obliku x,y: ")

if len(T2)<2:
       T2=input("pogrešan upis. upišite koordinate druge točke obliku x,y:")

print(pravac(T1,T2))
