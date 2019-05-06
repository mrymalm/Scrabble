numRow=8
numCol=8
board=[]
letters=["A","B","C","D","E","F",
         "G","H","I", "J", "K","L", "M",
         "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W","X", "Y", "Z"]
def create_board():
        for row in range(numRow):
                rowlist=[]
                for col in range(numCol):
                        rowlist.append(' ')
                board.append(rowlist)
##print board properly and use numCol and numRow to make
##the process of changing the board dimentions easy
def print_board():
    line1 = ' '+' '
    for l in range(numCol):
##use of str to show the column numbers as a string 
        line1=line1+' '+str(l+1)
    print(line1)
    line2= ' '+ ' '+'+-'*numCol+ '+'
    for l in range(numRow):
        line3=letters[l]
        if len(letters[l])==1:
            line3=line3+' '
        for n in range(numCol):
                line3=line3+'|'+board[l][n]
        line3=line3+ '|'
        print(line2)
        print(line3)
    print(line2)
	
create_board()
print_board()
