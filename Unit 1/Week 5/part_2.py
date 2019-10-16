def caesar(phrase,shift): 
    result = '' 
    #Step through phrase
    for i in range(len(phrase)): 
        char = phrase[i]
        #Retrieve the ordinal value of the character, add the shift, and retrieve character value of the new ordinal 
        result = result + chr((ord(char) + shift - 97) % 26 + 97) 
  
    return result 
  
phrase = 'thequickbrownfoxjumpsoverthelazydog'
shift = 13
print ('Caesar Cipher: ' + caesar(phrase,shift))
