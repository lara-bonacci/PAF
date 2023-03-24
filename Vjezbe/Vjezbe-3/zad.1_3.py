print(5.0-4.935)
#ocekivani rezultat bio je 0.065, no output nije precizan u decimali. 
#python procesira brojeve u binarnom sustavu, te decimalni dio broja prikazuje kao beskonacan niz 0 i 1.
#ipak, memorija za pohranu brojeva je ogranicena tako da se pohranjuje samo npr 64 bita za float i time ogranicava broj jedinica i nula tj. preciznost u decimali
#samo brojevi koji se mogu zapisati kao 1/2^n imaju konacan broj 0 i 1

a= 0.1+0.2+0.3
print(a)
if a==0.6:
    print(True)
else:
    print(False)

#broj 0.6 nije točno 6/10 i zato se ne može zapisati kao 0.6 u binarnom vec zaokruziti na nesto najblize iznad 0.6
