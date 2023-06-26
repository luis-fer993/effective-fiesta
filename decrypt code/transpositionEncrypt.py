#transposition

def main():
    message='Common sense is not so common.'
    message = str(input('Ingrese datos -> '))
    key=8
    key=int(input('Ingrese Key -> '))
    text = encryptMessage(message, key)
    print(text+'|')
    
def encryptMessage(message,key):
    ciphertext=['']*key
    # Loop through each column in ciphertext.
    for col in range(key):
        # 1 - 8 
        pointer = col 
        
        while pointer< len(message): 
            
            #agregamos datos a la lista 
            ciphertext[col]+=message[pointer]
            
            pointer+=key #sumamos 0 + n, 8 + n, 16 + n, and 24 + n ..... 
    return ''.join(ciphertext)

if __name__=='__main__':
    main()