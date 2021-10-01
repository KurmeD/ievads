skaitlis1=13
skailtis2=3

saskaitisana=skaitlis1+skailtis2
print(saskaitisana)#saskaitam
print(skaitlis1,"+",skailtis2,"=",saskaitisana)#parādam vizuāli 13+3=16

atnemsana=skaitlis1-skailtis2
print(atnemsana)#atnemsana rez=10

reizinasana=skaitlis1*skailtis2
print(reizinasana)#reizinasana rez=39

dalisana=skaitlis1/skailtis2
print(dalisana)# dalam rez=4,33(3)

dalisana2=skaitlis1//skailtis2
print(dalisana2)# dalam bez atlikuma rez=4

atlikums=skaitlis1%skailtis2
print(atlikums)# atlikuma noteikšana rez=1

pakape=skaitlis1**skailtis2
print(pakape)# pakāpes noteikšanna ar zīmi **

#salidzinasan
print(10>9)#taisnība
print(2==2)#nav pareizi
a=2
a1="2"
print(a==a1)#nav vienāds, tapec ka viens ir sk.,otrs-teksts
print(1<0)#nav pareizi
#!= nav vienāds
#>= lielāks vai vienāds, būs šādi (=< ši variants nestrādā)
#<= mazāks vai vienāds
# and &&
#jāpasaka ka x mainīgais var atrasties starp 5 un 10, kā pierakstās
#x>5 && x<10 
#or || 
# xor ^
if1=30
if2=2
if if1>if2:
    print("Sk.30 ir liekās nekā sk.2")
else:
    print("Sk.30 nav liekās par sk.2")#tiek izmantot nosacījums if