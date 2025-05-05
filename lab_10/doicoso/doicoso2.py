#Bước 1(Bài 6 ):
def loc_chuoi(input_string):
    valid_chars = "0123456789ABCDEF"
    result = ''.join(char for char in input_string.upper() if char in valid_chars)
    return result
def xac_dinh_co_so(input_string):
    valid_binary = "01"
    valid_octal = "01234567"
    valid_decimal = "0123456789"
    valid_hexadecimal = "0123456789ABCDEF"

    input_string = input_string.upper()

    is_binary = all(char in valid_binary for char in input_string)
    is_octal = all(char in valid_octal for char in input_string)
    is_decimal = all(char in valid_decimal for char in input_string)
    is_hexadecimal = all(char in valid_hexadecimal for char in input_string)

    if is_hexadecimal:
        return 16
    elif is_octal:
        return 8
    elif is_decimal:
        return 10
    elif is_binary:
        return 2
    else:
        return None
def chuyen_doi_sang_co_so_10(input_string, base):
    try:
        decimal_value = int(input_string, base)
        return decimal_value
    except ValueError:
        return None