n = int(input("Nhập số sinh viên n: "))

cpp = set(map(int, input("Nhập số thứ tự SV thi C++: ").split()))
java = set(map(int, input("Nhập số thứ tự SV thi Java: ").split()))
python = set(map(int, input("Nhập số thứ tự SV thi Python: ").split()))

only_one = (cpp - java - python) | (java - cpp - python) | (python - cpp - java)
two_langs = ((cpp & java) - python) | ((cpp & python) - java) | ((java & python) - cpp)
all_three = cpp & java & python

print("Sinh viên chỉ thi 1 ngôn ngữ:", sorted(only_one))
print("Sinh viên thi 2 ngôn ngữ:", sorted(two_langs))
print("Sinh viên thi cả 3 ngôn ngữ:", sorted(all_three))