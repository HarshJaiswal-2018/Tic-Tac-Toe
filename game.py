def drawBoard():
    print("\n\n")
    print("                ",t[0]," | ",t[1]," | ",t[2])
    print("               _____ _____ _____")
    print("                ",t[3]," | ",t[4]," | ",t[5])
    print("               _____ _____ _____")
    print("                ",t[6]," | ",t[7]," | ",t[8])

def wincases(mark):
    if t[0]==mark and t[0]==t[1] and t[1]==t[2]:
        winner(mark)
    if t[3]==mark and t[3]==t[4] and t[4]==t[5]:
        winner(mark)
    if t[6]==mark and t[6]==t[7] and t[7]==t[8]:
        winner(mark)
    if t[0]==mark and t[0]==t[3] and t[3]==t[6]:
        winner(mark)
    if t[1]==mark and t[1]==t[4] and t[4]==t[7]:
        winner(mark)
    if t[2]==mark and t[2]==t[5] and t[5]==t[8]:
        winner(mark)
    if t[0]==mark and t[0]==t[4] and t[4]==t[8]:
        winner(mark)
    if t[2]==mark and t[2]==t[4] and t[4]==t[6]:
        winner(mark)

def winner(m):
    if m=='X':
        print("***Player 1 WON***")
        exit()
    else:
        print("***Player 2 WON***")
        exit()

def maps(p,ch):
    if p==1:
        t[0]=ch
    elif p==2:
        t[1]=ch
    elif p==3:
        t[2]=ch
    elif p==4:
        t[3]=ch
    elif p==5:
        t[4]=ch
    elif p==6:
        t[5]=ch
    elif p==7:
        t[6]=ch
    elif p==8:
        t[7]=ch
    elif p==9:
        t[8]=ch
    drawBoard()
    wincases(ch)

t=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

if __name__ == "__main__":
    drawBoard()
    print("\n\n NOTE : Numbering\n  1  2  3\n  4  5  6\n  7  8  9")

    x=0
    c=[]
    for i in range(9):
        if x%2==0:
            cpos=input("Player 1's turn\nEnter the position : ")
            npos=int(cpos)
            if npos<10 and cpos not in c:
                c.append(cpos)
                maps(npos,'X')
            else:
                print("Position NOT Available\nTry Entering Another Position")
                x-=1
        else:
            cpos=input("Player 2's turn\nEnter the position : ")
            npos=int(cpos)
            if npos<10 and cpos not in c:
                c.append(cpos)
                maps(npos,'O')
            else:
                print("Position NOT Available\nTry Entering Another Position")
                x-=1
        x+=1
