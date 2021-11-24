decimal = int(input("Enter a decimal number: "))
hex_letters = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
hexadecimal = ""

while decimal > 0:
    remainder = decimal%16
    if remainder <= 9:
        hexadecimal = str(remainder) + hexadecimal

    elif remainder >= 10 and remainder < 16:
        hexadecimal = hex_letters[remainder] + hexadecimal

    else:
        decimal = decimal // 16

print(hexadecimal)