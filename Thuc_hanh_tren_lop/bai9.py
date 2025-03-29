numbers = list(map(int, input("Nhập một danh sách các số cách nhau bởi dấu cách: ").split()))
try:
    assert all(num % 2 == 0 for num in numbers), "Không phải tất cả các số đều là chẵn"
    print("Tất cả các số trong danh sách đều là chẵn.")
except AssertionError as e:
    print(e)  

