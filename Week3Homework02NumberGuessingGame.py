"""
Bir degiskene 0-100 arasinda bir deger atayin. Kullanicidan bu sayiyi tahmin etmesini isteyin. Kullaniciyi yaptigi tahminlere gore yonlendirin. 
Kacinci denemede bildigini soyleyin.

Assign a value between 0-100 to a variable. Ask the user to guess this number. Guide the user according to their estimates. 
"""
number = 65
key=1
tryy=0
try:
    while key == 1:
        tryy +=1
        enter = (input("Please Guess a Number From 1 To 100(If You Want To Exit Please Enter 'q':"))
        if enter =='q':
            print("Exiting...")
            key == 0
            break
        enter = int(enter)
        gap = enter - number
        if -99 <= gap <= -45:
            print("You're Very Very Far, You Have To Up More")
        elif -45 < gap <= -25:
            print("You're Far, You Have To Up More")
        elif -25 < gap <= -20:
            print("You're Close, You Have To Up More")
        elif -20 < gap <= -5:
            print("You're Very Close, You Have To Up a Little More")
        elif 0 < gap <= 5:
            print("You're Very Close, You Have To Down a Little More")
        elif 5 < gap <= 20:
            print("You're Close, You Have To Down a Little More")
        elif 20 < gap <= 35:
            print("You're  Far, You Have To Down More")
        elif 35 < gap <= 50:
            print("You're So Far, You Have To Down More")
        elif 50 < gap <= 99:
            print("You're Very Very Far, You Have To Up  More")
        elif  gap == 0:
            print("Congratulations You Won At Your ",tryy,".Try",sep="")
            break
except:
    print("You Can Only Enter Integer")
        
    