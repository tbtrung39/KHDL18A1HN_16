number = input("Nhập một số: ")    
result = ""   
number_words = {  
    '0': "không",  
    '1': "một",  
    '2': "hai",  
    '3': "ba",  
    '4': "bốn",  
    '5': "năm",  
    '6': "sáu",  
    '7': "bảy",  
    '8': "tám",  
    '9': "chín"  
}   
for digit in number:  
    if digit in number_words:  
        result += number_words[digit] + " "  
print(result.strip())  