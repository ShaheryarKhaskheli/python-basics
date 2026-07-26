import random
num=random.randint(1,100)
print(num)
i=0
attempt=0
while i !=num:
    i=int(input("enter number "))
    attempt+=1
    if i ==num:
        print("you have guessed",attempt,"attempts")
    elif i<num:
        print("too low")
    elif i>num:
        print("too high")
    



    

