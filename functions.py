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
    
