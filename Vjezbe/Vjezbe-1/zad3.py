

točka1=input("upišite x,y koordinate za prvu točku: ").split(",")
točka2=input("upišite x,y koordinate za drugu točku: ").split(",")


if len(točka1)<2:
       točka1=input("pogrešan upis. upišite koordinate prve točke obliku x,y: ")

if len(točka2)<2:
       točka2=input("pogrešan upis. upišite koordinate druge točke obliku x,y:")

print(točka2)

k=(int(točka2[1])-int(točka1[1]))/(int(točka2[0])-int(točka1[0]))

print("y={}x+l".format(k))








