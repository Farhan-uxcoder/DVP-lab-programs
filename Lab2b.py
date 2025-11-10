def binary_to_decimal(bin_str):
    dec = int(bin_str, 2)
    return dec

def octal_to_hexadecimal(oct_str):
    dec = int(oct_str, 8)
    hex_val = hex(dec).upper().replace("0X", "")
    return hex_val

choice = input("Enter the choice (1 for binary to decimal, 2 for octal to hexadecimal): ")

if choice == '1':
    binary = input("Enter a binary number: ")
    decimal = binary_to_decimal(binary)
    print(f"Decimal equivalent: {decimal}")
elif choice == '2':
    octal = input("Enter an octal number: ")
    hexadecimal = octal_to_hexadecimal(octal)
    print(f"Hexadecimal equivalent: {hexadecimal}")
else:
    print("Invalid choice!")