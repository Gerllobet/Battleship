def startBoard():
    row1 = ["W", "W", "W", "W", "W"]
    row2 = ["W", "W", "W", "W", "W"]    
    row3 = ["W", "W", "W", "W", "W"]    
    row4 = ["W", "W", "W", "W", "W"]    
    row5 = ["W", "W", "W", "W", "W"]    
    board = [row1, row2, row3, row4, row5]
    return(board)

def showBoard(b):
    for l in b:
        print("".join(l))

def final(b):
    for l in b:
        for c in l:
            if(c == "S"):
                return False
    return(True)

def thereIsNoNumber(s):
    if(s[0] not in "01234" or s[-1] not in "01234"):
        return True
    else:
        return False

def someBoxOccupied(b, y, x, o):
    if(o == "V"):
        if(y > 2):
            return(True)
        
        i = 0
        for l in b:
            if(i >= y):
                if(l[x] != "W"):
                    return(True)
            i += 1
        return(False)
    
    if(o == "H"):
        if(x > 2):
            return(True)
        
        i = 0
        l = b[y]
        while(i < 3):
            if(l[x+1] != "W"):
                return(True)
            i += 1
        return(False)
    
def applyPlay(b, s):
    l = b[int(s[0])]
    if(l[int(s[-1])] in "XO"):
        print("This box has already been played! You've missed a shot!")
        return(b)
    if(l[int(s[-1])] in "S"):
        print("IMPACT!")
        l[int(s[-1])] = "O"
        b[int(s[0])] = l
        return(b)
    if(l[int(s[-1])] in "W"):
        print("WATER!")
        l[int(s[-1])] = "X"
        b[int(s[0])] = l
        return(b)

def wrongPosition(s):
    if(s[0] not in "01234"):
        return(True)
    if(s[1] != ":"):
        return(True)
    if(s[2] not in "01234"):
        return(True)
    if(len(s) != 3):
        return(True)
    return(False)

def getOrientation():
    opt = input("Would you like to place the boat vertically or horizontally? (v / h) ")
    if(opt in "vV"):
        print("'V'")
        return("V")
    elif(opt in "hH"):
        print("'H'")
        return("H")
    else:
        print("Sorry, this is not a valid option.")
        getOrientation()

def getPosition(o):
    opt = input("Initial box [row:column from 0 to 4]: ")
    if(0 == "H"):
        if((int(opt[0]) in range(0,5)) and (int(opt[2]) in range(0,4)) and (opt[1] == ":") and (len(opt) == 3)):
            return(opt)
        else:
            print("Sorry, this is not a valid position.")
            getPosition(o)
    else:
        if((int(opt[0]) in range(0,4)) and (int(opt[2]) in range(0,5)) and (opt[1] == ":") and (len(opt) == 3)):
            return(opt)
        else:
            print("Sorry, this is not a valid position.")
            getPosition(o)

def updateBoard(b, p, o):
    if(o == "H"):
        l = b[int(p[0])]
        l[int(p[-1])] = "S"
        l[int(p[-1]) + 1] = "S"
        b[int(p[0])] = l
        return b
    else:
        l1 = b[int(p[0])]
        l2 = b[int(p[0])+1]
        l1[int(p[-1])] = "S"
        l2[int(p[-1])] = "S"
        b[int(p[0])] = l1
        b[int(p[0])+1] = l2
        return b
    
def placeShip3(b, i):
    if(str(i) in "123" and len(str(i)) == 1):
        print("Reading the 3 positions ship number " + str(i))
        o = getOrientation()
        p = getPosition(o)
        print(updateBoard(b, p, o))
    else:
        print("Sorry, some of the positions where you want to place this ship is already occupied or des not exist. Try again")
        placeShip3(b, i)


b = startBoard()
placeShip3(b, 1)
