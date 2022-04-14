
'''
# class book baraye daryaft dade mibashad
#sdsdsdsd
#sdsdsdsd
a
fgfgdf
sfg
df

'''
class book:
    def __init__(self,title:str,author:str,tarikh:int)->None:#meghdar dehi avalie
        self.title=title
        self.author=author
        self.tarikh=tarikh
        
    def show_books(self)->str:  
        return "title : {}\n author: {}\n published {}\n".format(self.title,self.author,self.tarikh)

tarikh=input("tarikh enteshar: ")#daryafte tarikh enteshare ketab
a=book("java","david jons",tarikh)#nemone az class
res:object=a.show_books()
print(res)

tarikh=input("tarikh enteshar: ")#daryafte tarikh enteshare ketab
a=book("python","aron ramsy",tarikh)#nemone az class
res:object=a.show_books()
print(res)
