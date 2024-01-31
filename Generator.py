import random #Imports randomizers
import string #Imports string characters

password = '' #Sets a blank password

for i in range(12): #Sets a password length of 12
    
    choice = random.randint(1,4) #Randomly chooses between uppercase, lowercase, numbers, and special characters
    
    #Adds the random character chosen to the password
    
    if choice == 1:
        
        password += random.choice(string.ascii_lowercase)
    
    elif choice == 2:
        
        password += random.choice(string.ascii_uppercase)
    
    elif choice == 3:
        
        password += random.choice(string.digits)
    
    else:
        
        password += random.choice(string.punctuation)

password = list(password) #Converts the password string to a list

random.shuffle(password) #Rearranges the order of the list

password = ''.join(password) #Converts the password back into a string
    
passwordFile = open('passwords.txt', 'w') #Creates and opens a file to store the password

passwordFile.write(password + '\n') #Adds the password to the file

passwordFile.close() #Closes the file
