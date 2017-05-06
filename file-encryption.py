#Keyword Encryption/Decryption Program
import time                                                                     #Imports the time module, allowing the script to be paused later on.
import tkinter
                                                              #Imports the tkinter module, allowing the creation of GUIs.
print("Welcome to this keyword encryption and decryption program!")
print("Please select the file to encrypt or decrypt: ")
print(" ")

from tkinter.filedialog import askopenfilename                                  #Creates a file dialog to allow the user to select which file that they want to encrypt or decrypt.
root = tkinter.Tk()
root.withdraw()
Filename = askopenfilename()

Keyword = input("Please type in the keyword you want to use: ")                 #Takes a user input for the first keyword to use to encrypt or decrypt the Message.
Keyword2 = input("Please type in a second keyword that you want to use: ")      #Takes a second user input for the second keyword to use to encrypt or decrypt the Message.
UserInput = input("Type E to encrypt or D to decrypt: ")

if UserInput == ("E"):                                                          #Checks if the user wants to encrypt a message.
    print(" ")
    print("Encrypting:", Filename)

    with open (Filename, "r") as file:                                          #Reads the file that the user selected earlier, importing the contents of the file into the Message variable.
        Message = file.read()
    while (len(Keyword)) < (len(Message)):                                      #Creates a while loop so that if the keyword is not equal to the message, the follwing will be executed:
        Keyword = (Keyword + Keyword)                                               #The keyword is stacked over and over until it's equal to the message and the while loop breaks.
        Keyword = (Keyword + Keyword)
    Keyword  = Keyword[0:len(Message)]

    while (len(Keyword2)) < (len(Message)):
        Keyword2 = (Keyword2 + Keyword2)
    Keyword2  = Keyword2[0:len(Message)]
    Message = [ord(i)for i in Message]                                          #Converts the user's message into the according ASCII table values.
    Message = [i - 96 for i in Message]                                         #Subtracts 96 from every character in the message to get the position of the letters in the alphabet.
    Keyword = [ord(i)for i in Keyword]
    Keyword = [i - 96 for i in Keyword]
    Keyword2 = [ord(i)for i in Keyword2]
    Keyword2 = [i - 96 for i in Keyword2]
    Message2 = [x + y + z for x, y, z in zip(Message, Keyword, Keyword2)]       #Combines every character in the message with the according character in the keyword.
    Message2 = [chr(i + 96) for i in Message2]                                  #Converts the encrypted message into the according plaintext characters.
    Message2 = ''.join(Message2)

    print("File encrypted!")
    with open(Filename, 'wb') as file:                                          #Writes the encrypted message to the selected file and closes it.
        file.write(Message2.encode())
        file.close()

elif UserInput == ("D"):                                                        #Checks if the user wants to decrypt if they didn't want to encrypt.
    print(" ")
    print("Decrypting:", Filename)
    file = open(Filename, encoding="utf8")
    Message = file.read()

    while (len(Keyword)) < (len(Message)):
        Keyword = (Keyword + Keyword)
    Keyword  = Keyword[0:len(Message)]
    while (len(Keyword2)) < (len(Message)):
        Keyword2 = (Keyword2 + Keyword2)

    Keyword2  = Keyword2[0:len(Message)]
    Message = [ord(i)for i in Message]
    Message = [i - 96 for i in Message]
    Keyword = [ord(i)for i in Keyword]
    Keyword = [i - 96 for i in Keyword]
    Keyword2 = [ord(i)for i in Keyword2]
    Keyword2 = [i - 96 for i in Keyword2]
    Message2 = [x - y - z for x, y, z in zip(Message, Keyword, Keyword2)]
    Message2 = [chr(i + 96) for i in Message2]
    Message2 = ''.join(Message2)
    
    print("File decrypted!")
    with open(Filename, 'wb') as file:
        file.write(Message2.encode())
        file.close()
else:                                                                           #Checks for any other input, which is counted as invalid and closes the program.
    print("Program closing...")
