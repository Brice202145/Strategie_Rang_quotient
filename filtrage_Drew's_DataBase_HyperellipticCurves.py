mport os
#import ast

result=[]
with open("H3.txt", "r") as shubaFile:
    lines=shubaFile.readlines()
for line in lines:
    try:
        result.append(line[line.index("[")+1:line.index("]")])
    except:
        pass
L=print('[%s]'%', '.join(map(str, result)))
H=[]
for i in range(0,len(L),2):
    try:
        f=4*L[i]+(L[i+1])**2
        H.append(f)
    except:
        pass
H
def terms(poly:str)->list:
    try:
        poly=poly.replace(" ","")
    except:
        pass
    rep, s =[], poly.split("+")
    for term in s:
        if '-' in term:
            rep+=term.split("-")
    for term in s:
        if not '-' in term:
            rep.append(term)
    try:
        rep.remove("")
    except:
        pass
        
    return rep

def degre(monom:str)->int:
    m=monom[monom.index("x")+2:]
    if m=="":
        return 1
    return int(m)

def validation(poly:str)->bool:
    if terms(poly)[-1]=='1':
        for term in terms(poly)[:-1]:
            #print(poly, terms(poly)[:-1])
            if not degre(term)%2==0: return False
        return True
    return False

def poly_deg_pair(L:list)->list:
    rep=[]
    for polynome in L:
        if validation(polynome):
            rep.append(polynome)
    return rep

liste=[str(i) for i in H]
k=poly_deg_pair(liste)   