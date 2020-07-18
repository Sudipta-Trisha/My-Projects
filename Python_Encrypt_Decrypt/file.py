# Encryption - Decryption program using python #

chars = "!.@#%^&*()_'+qwertyuiop}{|][/asdfghjklzxcvbnm?/QWERTYUIOPASDFGHJKLZXCVBNM"
l = len(chars)

def find_sum(key):
    sum_digit=0
    for i in key:
       sum_digit = sum_digit + int(i)
    return sum_digit

def encrypt(text,key):
    password = find_sum(key)
    if password == 0:
        password = 5

    encryption = ""
    
    for char in text:
        if char in chars:
            val = chars.find(char) 
            val += int(key)
           # val += password
            encryption += chars[val%l]
        elif char.isspace:
            encryption += "1"   # if found any spaces then replace space with 1
    return encryption

def decrypt(text,key):
    password = find_sum(key)
    if password == 0:
        password = 5
    decryption = ""

    for char in text:
        if char in chars:
            val = chars.find(char)
            val = val - int(key)
           # val -= password
            if(val < 0):
                while(val < 0):
                    val = val + l;
            decryption += chars[val]
        elif char == "1":
            decryption += " "
    return decryption 

def done(operation,text,key):
    if operation == "E":
        print("---------------------------------------------")
        print("Encrypted Text: ",encrypt(text,key))
        print("---------------------------------------------")
    else:
        print("---------------------------------------------")
        print("Decrypted Text: ",decrypt(text,key))
        print("---------------------------------------------")

if __name__ == "__main__":
    text = input(" Enter Your Text Here : ")
    print(" ")
    key = input(" Enter Key in Number : ")
    print(" ")

    print("*** Which type of operation do you want to? If Encryption, then type 'E' else type 'D'.*** ")
    print(" ")
    print("*** If you type 'D' , then you have to fill the text area with encrypted text.***")

    operation = input()
    done(operation,text,key)
 
 ### Scripted By Sudipta Banik Trisha ###
    
