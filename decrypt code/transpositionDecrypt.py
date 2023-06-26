# transpositionDecrypt

import math

def main():
    data = str(input("Ingrese datos -> "))
    key= int(input('Ingrese key ->'))
    text=fn(data, key)
    print(data,text+'|',sep='\n')

def fn(message, key):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key) 
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    
    plaintext = [''] * numOfColumns
    
    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    
    col=0
    row=0
    
    for symbol in message:
        plaintext[col]+=symbol
        col+=1 #point to next column
        
        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >=numOfRows - numOfShadedBoxes):
            col=0
            row+=1
    return ''.join(plaintext)        
        
        
if __name__=='__main__':
    main() 
    
    
  