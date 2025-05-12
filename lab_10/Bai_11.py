from doicoso.doicoso1 import dec_to_bin, dec_to_oct, dec_to_hex
from doicoso.doicoso2 import binary_to_dec, oct_to_dec, hex_to_dec, is_binary_string

n = 42
print("Binary:", dec_to_bin(n))
print("Octal:", dec_to_oct(n))
print("Hex:", dec_to_hex(n))

s = "101010"
if is_binary_string(s):
    print("Binary to decimal:", binary_to_dec(s))

print("Octal to decimal:", oct_to_dec("52"))
print("Hex to decimal:", hex_to_dec("2A"))