# This is a mini calculator to operate some operations.
from os import system, name
import math

#define clear funtion
def clear():
    input('Press Enter to continue...')
    if name == 'nt':
        _ = system('cls')
    else :
        _ = system('clear')

def oct_to_dec(num):
    n = num
    dec_value = 0
    base = 1
    keep = n
    while(keep):
        last = keep % 10
        keep = int(keep/10)
        dec_value += last * base
        base = base * 8
    return dec_value

while 1:

    print("\nWhich Operations do you want to do?\n")

    print("1.Addition\n2.subtraction\n3.Multiplication\n4.GCD\n5.LCM\n6.Division")
    print("7.Decimal to Binary\n8.Decimal to Hexadecimal\n9.Decimal to Octal")
    print("10.Binary to Octal\n11.Binary to Hexadecimal\n12.Binary to Decimal")
    print("13.Octal to Decimal\n14.Octal to Binary\n15.Octal to Hexadecimal")
    print("16.Hexadecimal to Decimal\n17.Hexadecimal to Binary\n18.Hexadecimal to Octal")
    print("19.ASCII Value of a character")
    print("20.Exit")

    op = int(input("Please Enter The operation number: "))

    print("\n")
    result = 0

    # Addition , subtraction , multiplication , division

    if op>=1 and op<=5:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        if op == 1:
            result = num1 + num2
        elif op == 2:
            result=num1-num2
        elif op == 3:
            result = num1*num2
        elif op == 4:
            result = math.gcd(num1, num2)
        elif op == 5:
            result = (num1*num2)/(math.gcd(num1, num2))

        print("The result is: ", int(result))
        print("\n")
        clear()

    elif op == 6:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        temp = float(num1)/float(num2)
        print("The result is: ", temp)
        print("\n")
        clear()

    # decimal to bin, hex, oct

    elif op>=7 and op<=9:
        num = int(input("Enter a integer Number: "))
        if op == 7:
            result = bin(num)
        elif op == 8:
            result = hex(num)
        elif op == 9:
            result = oct(num)
        print("The result is: ", result)
        print("\n")
        clear()

    # bin to oct, hex, dec

    elif op>=10 and op<=12:
        if op == 10:
            print("Enter your input in Binary Format: ")
            x = int(input(), 2)
            print("Octal form is: "+ oct(x))
            print("\n")
            clear()
        elif op == 11:
            print("Enter your input in Binary Format: ")
            x = int(input(), 2)
            print("Hexadecimal form is: " + hex(x))
            print("\n")
            clear()
        elif op == 12:
            print("Enter your input in Binary Format: ")
            x = int(input(), 2)
            print("Decimal form is: " + str(x))
            print("\n")
            clear()

    # Octal to dec, bin, hex

    elif op>=13 and op <=15:

        # Octal to decimal

        if op == 13:
            num = int(input("Enter a number in Octal Format: "))
            print("The result is: ", oct_to_dec(num))
            print("\n")
            clear()

        # Octal to Binary

        elif op == 14:
            num = input("Enter a number in Octal Format: ")
            dec = str(int(num, 8))
            dec_num = int(dec)
            print("The result is: ", bin(dec_num))
            print("\n")
            clear()

        # Octal to Hexadecimal

        elif op == 15:
            num = input("Enter a number in Octal Format: ")
            dec = str(int(num, 8))
            dec_num = int(dec)
            print("The Hexadecimal format is: ", hex(dec_num))
            print("\n")
            clear()

    # Hexadecimal to dec, bin, oct

    elif op>=16 and op<=18:

        # Hexa to Decimal

        if op == 16:
            s = input("Enter a Hexadecimal String: ")
            temp = int(s, 16)
            print("The Decimal Format is: ", str(temp))
            print("\n")
            clear()

        # Hexa to Binary

        elif op == 17:
            s = input("Enter a Hexadecimal String: ")
            temp = int(s, 16)
            print("The Binary Format is: ", bin(temp))
            print("\n")
            clear()

        # Hexa to Octal
        elif op == 18:
            s = input("Enter a Hexadecimal String: ")
            temp = int(s, 16)
            print("The Octal Format is: ", oct(temp))
            print("\n")
            clear()

    # ASCII Value

    elif op == 19:
        ch = input("Enter a character: ")
        print("The ASCII Value of this character is: ", ord(ch))
        print("\n")
        clear()

    # Exit portion

    elif op == 20:
        quit()
    else:
        print("Not included in those operations.\nThanks.")
        quit()
