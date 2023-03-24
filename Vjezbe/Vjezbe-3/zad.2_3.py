
def mat(N):
    zbroj=5
    količnik=5
    for n in range(N):
        zbroj+=1/3
        količnik-=1/3
    return zbroj, količnik

print(mat(200))

print(mat(2000))

print(mat(20000))

#razlika u broju iteracija trebala je utjecati samo na pomak tocke u desno jer se radi o deseticama
#umjesto toga vidi se i razlika u zadnjim decimalama
#kako se vise brojeva pomaknulo ispred decimalne tocke, to oslobodi mjesto u memoriji za decimale i poveca preciznost

