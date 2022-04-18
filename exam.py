class Student:
   

    def __init__(self,name,score) -> None:
        self.name=name
        self.score=score
        self.dct={self.name:self.score}
      
    def get(self):
        return self.dct   

namedaneshjo=input("name daneshjo: ")
score=int(input("nomre deneshjo: "))

nemone=Student(namedaneshjo,score)
print(nemone.get())
        