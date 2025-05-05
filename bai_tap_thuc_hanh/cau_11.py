import sys
sys.path.append("C://KHDL18A1HN_16//bai_tap_thuc_hanh//cau_11.py")
# main_doicoso.py

from cau_5_doicoso1 import dec_to_bin,dec_to_hex,dec_to_oct
from cau_6_doicoso2 import hex_to_dec,oct_to_dec,binary_to_dec 

print(dec_to_bin(25))
print(binary_to_dec("11001"))
print(dec_to_hex(7))
print(dec_to_oct(4))
print(hex_to_dec("3"))
print(oct_to_dec("5"))