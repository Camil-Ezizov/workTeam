team=[]
class Worker:
      def __init__(self,_ad,_soyad,_salary,_vezife,_isvaxti):
        self.ad=_ad
        self.soyad=_soyad
        self.salary=_salary
        self.vezife=_vezife
        self.isvaxti=_isvaxti
      def showData(self):
         print(f"ad:{self.ad} ,soyad:{self.soyad} ,salary:{self.salary},vezife:{self.vezife},isvaxti:{self.isvaxti}")    

def isciElaveet():      
    ad=input("ad:")
    soyad=input("soyad:")
    salary=int(input("Emekhaqqi:Xahis edirik reqem daxil edin:"))
    vezife=input("vezife:")
    isvaxti=int(input("isvaxti:"))
    work=Worker(ad,soyad,salary,vezife,isvaxti)
    team.append(work)
    

for i in range(2):
    isciElaveet()


#Iscilerin melumatlarini ekran cap edir
def iscileriGoster():
    for worker in team:
        worker.showData()  
teleb1=input("Butun iscileri cap etmek ucun 1 duymesini sixin:")
if int(teleb1)==1:
       iscileriGoster()


#ada gore melumatlari cap et
def adaGoreAxtar(workerName):
    for worker in team:
        if worker.ad==workerName:
            worker.showData()
            break
        else:
            print("bu adda isci movcud deyil")
teleb2=input("Isci adlarini gostermek ucun axtarin:")
adaGoreAxtar(teleb2)

#soyada gore melumatlari cap et
def soyadaGoreAxtar(workerSurname):
    for worker in team:
        if worker.soyad==workerSurname:
            worker.showData()
            break
        else:
            print("Bu soyadda isci movcud deyil")
teleb3=input("Isci soyadlarini gostermek ucun axtarin:")
soyadaGoreAxtar(teleb3)


#artiq saat isleyende iscinin alacagi emek haqqi
def artiqSaat():
    for worker in team:
        if worker.isvaxti > 9:
            print(worker.salary+worker.salary*0.2)
        else:
            print(worker.salary)
artiqSaat()


def isciEmekHaqqi(workerSalary):
    for worker in team:
        if worker.vezife==workerSalary:
           print(worker.salary)
        else:
           print("Bele vezife movcud deyil:")
teleb4=input("Isci vezifesine gore maas:")
soyadaGoreAxtar(teleb4)






