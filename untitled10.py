#Manan shah in collab with Allu

Allu_Ka_Tokri= input() 
Allu= Allu_Ka_Tokri.split(',')
for Tamatar in Allu:
    if Tamatar.isalpha():
        Allu.remove(Tamatar)
Kacha= 0
Pakka= 0
Kitne_allu= 0 
for i in Allu:
    i = int(i)
    Kitne_allu+=1
    if i > Pakka:
        Pakka , Kacha = i , Pakka
    if i < Pakka and i > Kacha:
        Kacha = i
    if Kitne_allu==len(Allu) and Kacha == 0:
        Kacha = Pakka 
print(Kacha)