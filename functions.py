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

def someBoxOccupied(b, x, y, o):
    
