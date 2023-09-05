import random as r

uwicket=0
pwicket=0
uball=0
uover=0
pball=0
pover=0
uscore=0
pcscore=0
innings=0
def batting(over=5):
    global uwicket
    global uball
    global uover
    global uscore
    global innings
    print("You can hit anything between 0 to 6. Hit hard!")
    input("Press enter to continue...")
    while uwicket<11 and innings==0:
        for i in range(over):
            for j in range(6):
                userbat=int(input("HIT->"))
                if userbat>6 or userbat<0 or userbat=='':
                    print("Error buddy! try to play safe next time.")
                    batting()
                cpubowl=r.randint(0,6)
                if userbat==cpubowl:
                    print("OUT!")
                    uwicket+=1
                else:
                    uscore+=userbat
                    print(f"You have scored {userbat}. Now, {5-uball} balls left.")
                uball+=1
            uball=0
            uover+=1
            print(f"The over has ended. Your current score: {uscore}/{uwicket} in {uover} overs")
        print("Final score of the innings is ", uscore, 'by', uwicket, 'wickets')
        if innings==0:
            innings+=1
            bowling(over)
        else:
            print(uscore)
            #MORE TO BE ADDED
def bowling(over):
    print("Under maintenance!")

def toss():
    #head tail and bat or ball choosing function
    try:
        headtail=int(input("Choose 1 for head and 0 for tail. Skip to quit.\n->"))
        tossresult=r.randint(0,1)
        if headtail==tossresult:
            print('Congratulations you won the toss!')
            userchoose=int(input("Now choose batting or bowling. 1 for bat and 0 for bowl :"))
        elif headtail not in (0,1):
            quit()
        else:
            userchoose=r.randint(0,1)
            print("Sorry you lost the toss.")
    except:
        print("Thanks for playing!")
        quit()
    def choosebattingorbowling():
        try:
            n = int(input("How many overs do you want to play?->"))
            if userchoose==1:
                batting(n)
            elif userchoose==0:
                bowling(n)
            else:
                print("You messed up buddy! Choose again.")
                choosebattingorbowling()
        except:
            print("Please donot mess again!")
            choosebattingorbowling()
    choosebattingorbowling()
toss()