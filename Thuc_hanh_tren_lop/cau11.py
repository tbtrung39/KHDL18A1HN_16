n = int(input("Nhập số lượng sinh viên: "))
a = set(map(int, input("Nhập danh sách sinh viên thi C++ (các số cách nhau bởi dấu cách): ").split()))
b = set(map(int, input("Nhập danh sách sinh viên thi Java (các số cách nhau bởi dấu cách): ").split()))
c = set(map(int, input("Nhập danh sách sinh viên thi Python (các số cách nhau bởi dấu cách): ").split()))
only_cplusplus = a - (b | c)
only_java = b - (a | c)
only_python = c - (a | b)
cpp_and_java = a & b - c
cpp_and_python = a & c - b
java_and_python = b & c - a
all_three = a & b & c

print("Sinh viên chỉ thi C++:", sorted(only_cplusplus))
print("Sinh viên chỉ thi Java:", sorted(only_java))
print("Sinh viên chỉ thi Python:", sorted(only_python))
print("Sinh viên thi cả C++ và Java (không thi Python):", sorted(cpp_and_java))
print("Sinh viên thi cả C++ và Python (không thi Java):", sorted(cpp_and_python))
print("Sinh viên thi cả Java và Python (không thi C++):", sorted(java_and_python))
print("Sinh viên thi cả ba ngôn ngữ:", sorted(all_three))