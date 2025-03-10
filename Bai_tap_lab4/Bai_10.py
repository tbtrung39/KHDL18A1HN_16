number = input("Nhập một số thập phân: ")  
digits = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]    
result = ""  
for digit in number:  
    if digit.isdigit():   
        result += digits[int(digit)] + " "  
print(result.strip())  