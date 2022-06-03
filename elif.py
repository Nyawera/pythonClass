
from unicodedata import name
from paramiko import Agent


x = range(0,20)
for y in x:
    if y % 3 == 0:
        print(f"{y} is divisible by 3")
    elif y % 5 == 0:
        print("f{y} is divisible by 5")
    elif y % 7 == 0:
        print("f{y} is divisible by 7")
    else:
         print("f{y} is not divisible by 3,5 and 7")
    
    # def greeting(name,age)
    # year=2022-age
    #   return f"hello{name}you were born in{year}"
     
    #   greeting("susan",21)
    #   greeting("Effence",20)
    #   greeting(22,Effence)
#    from unicodedata import name

#      greeting(name="susan",age=21)
#      greeting(age=21,name="susan")
#      greeting(age=22,name="Alice")