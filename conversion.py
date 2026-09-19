def main():
    while True:
        choose = input("Do you want to convert from binary number or from decimal number: ").strip().capitalize()
        print(f"you will choose diffrent {choose} numbers, but if you want to change to the other type ckick \"change\" or if you want to exit click \"stop\"")
        if choose == "Binary":
            while True:
                binaryToDecimal = input("what is your binary number: ")
                if binaryToDecimal == "stop":
                    return
                elif binaryToDecimal == "change":
                    break

                if "2" in binaryToDecimal or "3" in binaryToDecimal or "4" in binaryToDecimal or "5" in binaryToDecimal or "6" in binaryToDecimal or "7" in binaryToDecimal or "8" in binaryToDecimal or "9" in binaryToDecimal:
                    print("Enter a valid Binary number")

                else: 
                    print("-----------------------------------------------------------")
                    print(f"your binary number {binaryToDecimal} is equal to", binary(binaryToDecimal), "as a decimal number")
                    print("-----------------------------------------------------------")
                    print(f"binary number: {binaryToDecimal}")
                    print("decimal number:", binary(binaryToDecimal))
                    print("-----------------------------------------------------------")

        elif choose == "Decimal":
            while True:
                decimalNumber = input("what is your decimal number: ")

                if decimalNumber == "stop":
                    return
                elif decimalNumber == "change":
                    break

                if "-" in decimalNumber or "." in decimalNumber or " " in decimalNumber:
                    print("Enter a vailed decimal number")

                else:
                    decimalToBinary = int(decimalNumber)
                    print("-----------------------------------------------------------")
                    print(f"your decimal number {decimalToBinary} is equal to", decimal(decimalToBinary), "as a binary number")
                    print("-----------------------------------------------------------")
                    print(f"decimal number: {decimalToBinary}")
                    print("binary number:", decimal(decimalToBinary))
                    print("-----------------------------------------------------------")


def decimal(n):
    if n == 0:
        return "0"
    
    b = ""

    while n > 0:
        rem = n % 2
        b = str(rem) + b
        n = n // 2
        
    return b


def binary(n): 
    number = 0

    for digits in n:
        number = (number * 2) + int(digits)
    return number 


main()
