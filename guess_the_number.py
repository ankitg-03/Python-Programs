import random
m=random.randrange(1,10)
print("\nWELCOME!\nIn this game you have to guess the correct number in between 1 to 10\nYou will be having 6 guesses to guess the correct number")

def game():
    for i in range(3,0,-1):

            print("\nTries Left :",i)
            if i==1:
                print("LAST TRY... GOOD LUCK")
            x = int(input("Enter any number between 1-10 : "))
            if x<m:
                print("Low input..Try a bigger number")
            elif x>m:
                print("High input..Try a smaller number")
            elif x==m:
                print("Player Wins and Computer Loose")
                break


game()
c=int(input("press '1' to continue"))

while c==1:
    b=input("If you want to play again type 'YES' otherwise type 'NO' : ")
    if b=="YES":
        game()
    elif b=="NO":
        print("Thanks for playing !!")
        c=0
        break




