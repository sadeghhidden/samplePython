
class Ostadha:
    def __init__(self,shomare_ostad,name_ostad,saatKari_ostad,mablaghDaryafti_ostad) -> None:
        self.shomare_ostad=shomare_ostad
        self.name_ostad=name_ostad
        self.saatKari_ostad=saatKari_ostad
        self.mablaghDaryafti_ostad=mablaghDaryafti_ostad
        self.lstOstad+=[self.shomare_ostad,self.name_ostad,self.saatKari_ostad,self.mablaghDaryafti_ostad]
    def getShomare(self):
        return shomare_ostad
    def setShomare(self,value:any):
        self.shomare_ostad=value
    def getName(self):
        return self.name_ostad
    def setName(self,value:any):
        self.name_ostad=value
    def getSaat(self):
        return self.saatKari_ostad
    def setSaat(self,value:any):
        self.saatKari_ostad=value 
    def getMablagh(self):
        return self.mablaghDaryafti_ostad
    def setMablagh(self,value:any):
        self.mablaghDaryafti_ostad=value           
    
        
        

shomare_ostad=input("shomare ostad ra vared konid: ")
name_ostad=input("name ostad ra vared konid: ")
saatKari_ostad=input("saat kari ostad ra vared konid: ")
mablaghDaryafti_ostad=input("mablagh daryafti dar har saat: ")
ostad=Ostadha(shomare_ostad,name_ostad,saatKari_ostad,mablaghDaryafti_ostad)
print(ostad.getName())
ostad.setName("ali rezaee")
print(ostad.getName())



    # while True:
    # sh=input('shomare ostad: ')
    # n=input('name ostad: ')
    # s=input('saat kari  ostad: ')
    # m=input('mablagh daryafti dar har saat ostad: ')

    # listAsatid=[sh, n, s, m]
    # exitapp=input('exit==0')
    # if exitapp=='0':
    #     break
    # obj[count]=listAsatid
    # count+=1

# for i in obj:    
#     print(obj)
    
