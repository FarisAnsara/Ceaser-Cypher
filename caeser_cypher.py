#%% input data
def main():    
    import time    
    import string
    import random
    import re 
    
    alph = list(string.ascii_uppercase)                                             #list of all upper case letters in the alphabet
    punc = list(string.punctuation)                                                 #list of all punctuation
    length = len(alph)
    list_enc = ["Encrypt" , "encrypt", "ENCRYPT"]
    list_dec = ["Decrypt" , "decrypt", "DECRYPT"]
    list_enc_dec = list_enc + list_dec
    list_manual = ["manually", "Manually", "MANUALLY"]                                          
    list_auto = ["read" , "Read" , "READ"]    
    list_auto_manual = list_auto + list_manual
    list_autodec = ["autodecrypt" , "Autodecrypt", "AutoDecrypt", "AUTODECRYPT"]                                  
    list_enc_dec_autodec = list_enc_dec + list_autodec
                    #we asl the user whether to encrypt decrypt or autodecrypt               
    enc_or_dec = str( input( "would you like to encrypt, decrypt or use the autodecryption process (if so, please enter autodecrypt)? "))
    if enc_or_dec not in list_enc_dec_autodec: 
        print("\nplease input the correct values for the mechanism the program should run \n\n   ---- restarting program ----") 
        time.sleep(5)
        main()                 
                    #we let the user input whether they would like to use manual entry of sentence or automatic from a .txt file
    manual_or_automatic = input("would you like to manually enter the sentence (if so please enter manually) \nor read from a text file (if so please enter read)? ")
    
    if manual_or_automatic not in list_auto_manual :                                #if the user inputs wrong (input not manually or read), we restrart the program
        print("\nplease input the correct values for reading or manually inputing a message \n\n   ---- restarting program ----") 
        time.sleep(5)                                                               #extra!# here, we restart the program after 5 secs
        main()
                                                                                    
    if manual_or_automatic in list_manual:                                          #if user chooses manual input                
        if enc_or_dec in list_enc_dec:                                              #if user choses to encrypt or decrypt
                    #we let the use input the sentence they wish to encrypt or decrypt         
            sentence_input = str( input( "please add the sentence you wish to " + enc_or_dec + " using the caeser cipher: ")).upper()
                    #we let the user input their chosen rotation value             
            rotation_value =  input( "how much would you like the rotation value to be? (enter an interger value, or random if you want the program to choose a random number for you): ")
            
            if rotation_value == "random":                                          #if the user does not wish to choose a rotation value, they input random and the program randomises a value for them
                rotation_value =  random.randint(1 , 26)                            #randomise a rotation value
                print("Random value is : " + str(rotation_value))                   #we print the randomised rotation value

            try:
                rotation_value = int(rotation_value)                                #we try int() function on the rotation value 
            except ValueError :                                                     #if it doesnt work, we restart the progarm
                print("\nplease input the correct value for the rotation value \n\n  ---- restarting program ----")
                time.sleep(5)
                main()                                                              
                
        elif enc_or_dec in list_autodec :                                           
                    #if the user chooses the autodecrypt, we let them input the sentence they wish to autodecrypt        
            sentence_input = str( input( "please add the sentence you wish to " + enc_or_dec + " using the caeser cipher: ")).upper()
                                                                             
    
    elif manual_or_automatic in list_auto:                                          #if the user chooses to use a .txt file to input the sentence they wish

        if enc_or_dec in list_enc_dec:                                                     #if the user chooses to encrypt of decrypt
                    #open a file from which to input the message, we let the user input the file name and path
            text_file_auto = str(input("Please input the filename (if in this folder) or the filepath (if not in this folder): "))
            
            try:                                                                     #if the file input cannot be found, we restart the program
                file_auto_dec = open(text_file_auto , "r+")
            except FileNotFoundError:
                print("\nPlease input a valid file name and path... \n\n  ---- restarting program ----" )
                time.sleep(5)
                main()
            
            file_auto = open(text_file_auto, "r+")
            sentence_input =""                  
            
            for sentence in file_auto:   
                sentence_input += sentence                                           #we add each sentence to the empty string
            sentence_input = sentence_input.upper()                                  #we make the sentence all uppercase letters
        
            rotation_value =  input( "how much would you like the rotation value to be? (enter an interger value, or random if you want the program to choose a random number for you): ")
                                                                                     
            if rotation_value == "random":
                rotation_value =  random.randint(1 , 26)   
                print("Random value is : " + str(rotation_value))                    
            
            try:
                rotation_value = int(rotation_value)                                 
            except ValueError :
                print("\nplease input the correct value for the rotation value... \n\n  ---- restarting program ----")
                time.sleep(5)                                                        
                main()
        
        elif enc_or_dec in list_autodec :                                            #if the user chooses to autodecrypt, we let them input the file name and path of which to get the message to autodecrypt from
            text_file_auto_dec = str(input("Please input the filename (if in this folder) or the filepath (if not in this folder): "))
            
            try:                                                                     #if the file input cannot be found, we restart the program
                file_auto_dec = open(text_file_auto_dec , "r+")
            except FileNotFoundError:
                print("\nPlease input a valid file name and path... \n\n  ---- restarting program ----" )
                time.sleep(5)
                main()
                
            file_auto_dec = open(text_file_auto_dec , "r+")
            sentence_input =""
            
            for sentence in file_auto_dec:   
                sentence_input += sentence                                            #we add each sentence to the empty string   
            sentence_input = sentence_input.upper()
            file_auto_dec.close()                                                                    
            
#%%    
    
    def decrypt(sentence_input, rotation):
        s = ""                                                                        #s is an empty string that letters are added to.
        while rotation >= 26:                                                         #if the rotation value is greater than 26, we subract that by 26 to get a number less than 26
            rotation = rotation - 26
        s = ""
        for letter in list(sentence_input):                                           #for loop to decrypt each letter in the input sentence.
            if letter in alph:                                                        #if function for letters ONLY.
                i = alph.index(letter)               
                count = i - rotation
                if count >= length:
                    count = count - length
                s = s + str(alph[count])
            elif letter in punc:                                                      #if func to add any punctiation.
                s = s + letter
            elif letter in string.whitespace:                                         #if func to add whitepaces to the string 
                s = s + letter
        
        file = open("Decrypted.txt", "w")                                     #open a new file called decrypted.txt
        if enc_or_dec in list_dec:                                                    #make sure to not add the autodecrypted message to the file
            file.write(s)                                                             #add the decrypted message to the file
            file.close()
            time.sleep(2)
        decrypt.variable = s                                                          #call (s) decrypt.variable to be called in the analysis func
        return s                                                                      
    
    def encrypt():        
        s = ""               
        for letter in list(sentence_input):                                           #for loop for each letter in the input sentence.    
            if letter in alph:                                                        #if function for letters ONLY.
                i = alph.index(letter)
                count = i + rotation_value
                if count >= length:                                                   #if func to not exceed length
                    count = count - length
                s = s + str(alph[count])
            elif letter in punc:                                                      #if func to add any punctiation
                s = s + letter
            elif letter in string.whitespace:                                         #add whitespaces to the string
                s = s + letter
        file = open("Encrypted.txt", "w")                                             #open a new file called encrypted.txt to add the encrypted sentence to
        file.write(s)
        file.close()                                                                  
        time.sleep(2)
        return s
                                                                                      
        
#%% auto decryption
    
    def autodec(sentence_input):
        list_yes = ["yes" , "Yes"]                                                    #create a list of yes's
        list_no = ["no", "No"]                                                        #create a list of nos'
        words_check = []                                                              #empty list to append the words in words.txt in to cross refrence later with
        file_words = open("words.txt", "r+")                                              
        for wrd in file_words:                                                        #for loop to add the words to the list
            wrd = wrd.upper()
            t = list(wrd)
            ltr_str = ""
            for ltr in t:
                if ltr in alph:                                                       #if letter in alphabets, we add it to the string
                    ltr_str += ltr
            words_check.append(ltr_str)
        file_words.close()
        
        rotation_val = 1                                                              #set rotation value as 1
        sentence = sentence_input
        answer = "no"                                                                 #set answer as no so while loop starts
        while answer in list_no:                                                      #while loop to autodecrypt          
            sen = decrypt(sentence, rotation_val)
            se = re.split("\s|\n", sen)                                               #split sentence using spaces or returns 
            for word in se:
                if word in words_check:
                    print("\n" + se[0] + " " + se[1] + " " + " " + se[2] + " " + se[3])   #return 4 words from the autodecrypted message
                    answer = input("is the above a decrypted phrase from the message? ")  #let user input if the autodecryption to a phrase is correct
                    if answer in list_yes:                                                       
                        autodec.variable = sen                                            #if its right, create a vriable to be called for the analysis
                        while rotation_val >= 26:                                         #if the rotation value is greater than 26, we subract that by 26 to get a number less than 26 to be returned with the autodecrypted sentence
                            rotation_val = rotation_val - 26
                        file_autodec = open("Autodecrypted.txt" , "w")
                        file_autodec.write(sen)                                           #add the autodecrypted message to a .txt file
                        file_autodec.close()
                        print("\nbelow is the " + enc_or_dec + "ed message: ")            
                        time.sleep(2)                                                     #return the autodecrypted message after 2 secs
                        return sen + ("\n\nRotation value is: " + str(rotation_val - 1))
                      
                    elif answer in list_no:                                               #if the use inputs no, try again with another rotation value
                        rotation_val += 1
                        continue
                    
                    else:                                                                 #restarting the program due to incorrect inputs
                        print("\nerror: please input a yes or no value \n     ----- restarting autodecryption -----")
                        time.sleep(3)
                        print(autodec(sentence_input))
                        return " "
                        break
              
                else:
                    rotation_val += 1
        

               
                
                    
#%%analysis
   
    def analytics(sentence_input):
        
        time.sleep(2)
        print("\n      ---analysing data---     ")
        time.sleep(4)
        if enc_or_dec in list_enc :                                                       #if we're encrypting, to analyze the unencryptic massage                        
            sentence_in = list(sentence_input)            
        elif enc_or_dec in list_dec :                                                     #if we're dencrypting, to analyze the dencrypted massage 
            sentence_in = list(decrypt.variable)
        elif enc_or_dec in list_autodec:
            sentence_in = list(autodec.variable)
        
        sentence = ""                                                                     #sentence is an empty string to be added to later for top ten, unique words and total num of words
        letters_input = []                                                                #an empty list to be added to for most common letter
        for letter in sentence_in :                  
            if letter in alph:
                sentence += letter                                                        #add normal letters into the empty string
                letters_input.append(letter)                                              #add normal letters to the empty list to be analyzed as letters
            elif letter in string.whitespace:
                sentence += letter
        
        letters_dict = {}                                                                 #dict for letters with their repititions(empty)
        for l in letters_input:
            counter_of_letters = letters_input.count(l)                                   #count no of occurences
            letters_dict[l] = counter_of_letters                                          #add them as a dict with the key being the letter and the value to be the no of occurences
        
        letters_keys = list(letters_dict.keys())                                          #list for the no of occurences
        letter_num_of_rep = list(letters_dict.values())                                   #list for the letters 
    
        most_rep_letter_ind = letter_num_of_rep.index(max(letter_num_of_rep))             #index the max number of repetitions in the list letter_num_of_rep
        
        sentence = re.split( "\s|\n" , sentence)                                          #split sentence into list through the use of white space
        time.sleep(2)
        text1 = "Total number of words is : " + str(len(sentence))
        print("\n" + text1)                                                               #number of words is the length of the list
        file = open("analysis.txt" , "w")                                                     #open a new txt file called analysis
        file.write(text1)                                                                 #enter tot no of words
        file.close()
        g = {}                                                                            #set g as an empty dict to be added to later
        lengths = []                                                                      #lengths is an empty list to add lengths of words to
        for word in sentence:         
            counter = sentence.count(word)                                                #counter increases with the occurence of identical words
            g[word] = counter                                                             #add the word as key in dict and no of occurences as the value
            lengths.append(len(word))
        
        time.sleep(2)
        text2 = "\nNumber of unique words is : " + str(len(g))    
        print(text2)                                                                      #no of unique words is the lenght of the dict g
        file = open("analysis.txt" , "a")                                                     #reopen txt file to append
        file.write("\n" + text2)                                                          #add the no of unique words to file
        
        values = sorted(list(g.values()))                                                 #sort the values of g as a list
        values.reverse()                                                                  #sort it to be in decending order
    
        nom = list(g.values())                                                            #nom is a list of the number of occurences to
        keys = list(g.keys())                                                             #keys is a list of the words      
        
        print(" ")
        count = 0                                                                         #set initial count to 0 so that not to over exceed 10 words
        for y in values:
            ind = 0                                                                       #set index of number of occurences to 0
            if y in nom:
                ind = nom.index(y)                                                        #ind is the index of the number of occurences
                count += 1                                                                #count increases by 1 each time a number is indexed
                time.sleep(2)
                print("The word '" + str(keys[ind]) + "' has been found " + str(y) + " times" )           #print the word with its no of ocuurences
                nom.remove(nom[ind])                                                                      #remove the number of occurences from list to index it right
                keys.remove(keys[ind])                                                                    #remove the word so that not to be printed twice
                if count > 9:                                                                             #if count exceeds 9
                    break                                                                                 #we break at 9 to not exceed the 10 word counts  
        time.sleep(2)
        text3 = "\nThe maximum word length is : " + str(max(lengths))
        print(text3)        
        file.write("\n" + text3)                                                                          #add max word length to txt file
        text4 ="\nThe minimum word length is : " + str(min(lengths))
        print(text4) 
        file.write("\n" + text4)                                                                          #add max word length to txt file
        time.sleep(2)
        print("\nThe most common letter used is : " + str(letters_keys[most_rep_letter_ind]))             #using index most_rep_letter_ind, index the most repeated letter
        file.close()                  
        time.sleep(4)                                                                                     
        
        print("\n       ---------------------     \n\nThe " + enc_or_dec + "ed message and it's analysis have been saved into seperate text files " + enc_or_dec  + "ed.txt and analysis.txt")
        
        return "       ---------------------     "
                                                                                                          
    #%%
    
    if enc_or_dec in list_enc:                                                                            #call encrypt and analysis functions when enc_or_dec is encrypt
        print("\nbelow is the " + enc_or_dec + "ed message: ")
        print(encrypt())
        print("\n" + analytics(sentence_input))    
    
    elif enc_or_dec in list_dec:                                                                          #call decrypt and analysis functions when enc_or_dec is decrypt
        print("\nbelow is the " + enc_or_dec + "ed message: ")
        print(decrypt(sentence_input, rotation_value))
        print("\n" + analytics(sentence_input))
        
    elif enc_or_dec in list_autodec:                                                                      #call autodecrypt and analysis functions when enc_or_dec is autodecrypt
        print(autodec(sentence_input))
        print("\n" + analytics(sentence_input))
        
    
main()