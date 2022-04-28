from os import sep


a=0
for ch in range(3):
    for a in range(5):

        if ch==0 or ch ==2:
            print(f"* ",end="")
            
        else:
                if a==0:
                    print()
                    print("*"+(" "*6)+" *") 
                    a+=1 
                    continue
                else:
                    print("*"+(" "*6)+" *")   
                           
print("\n")            