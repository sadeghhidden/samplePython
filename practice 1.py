from typing_extensions import Self
l=[]

class Student:
   
    
    def __init__(self,name,score) -> None:
        
        self.name=name
        self.score=score
        self.lst={self.name:self.score}
        l.append(self.lst)
      
    def get(self):
        
        return l   
    
while True:
        
    namedaneshjo=input("name daneshjo: ")
    score=int(input("nomre deneshjo: "))
    if not score >20 or score<0:
            
            

            nemone=Student(namedaneshjo,score)
            print(nemone.get())
            print("cantinu? anyKey/n: ")    
            cantinu=input()
            if cantinu=='n':
                break
    else:

        print("score not in 20 - 0 ")            