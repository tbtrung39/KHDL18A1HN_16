employees = {}
n = int(input("Nhập số lượng nhân viên: "))

for _ in range(n):
    employee_id = input("Nhập mã nhân viên (4 ký tự số): ")
    name = input("Nhập họ tên nhân viên: ")
    birth_year = int(input("Nhập năm sinh: "))
    salary = float(input("Nhập lương: "))
    employees[employee_id] = {"name": name, "birth_year": birth_year, "salary": salary}
new_employee_id = input("\nNhập mã nhân viên mới: ")
name = input("Nhập họ tên nhân viên mới: ")
birth_year = int(input("Nhập năm sinh nhân viên mới: "))
salary = float(input("Nhập lương nhân viên mới: "))
employees[new_employee_id] = {"name": name, "birth_year": birth_year, "salary": salary}
x = input("\nNhập mã nhân viên cần tìm: ")
if x in employees:
    print(f"Thông tin nhân viên: Tên: {employees[x]['name']}, Năm sinh: {employees[x]['birth_year']}, Lương: {employees[x]['salary']}")
else:
    print("Không tìm thấy nhân viên.")
y = input("\nNhập mã nhân viên cần tăng lương: ")
if y in employees:
    employees[y]["salary"] += 1000000
    print(f"Đã tăng lương cho nhân viên {y}. Lương mới: {employees[y]['salary']}")
else:
    print("Không tìm thấy nhân viên.")
z = input("\nNhập mã nhân viên cần xóa: ")
if z in employees:
    del employees[z]
    print(f"Đã xóa nhân viên {z}.")
else:
    print("Không tìm thấy nhân viên.")
sorted_employees = sorted(employees.items(), key=lambda item: item[1]["birth_year"], reverse=True)

print("\nDanh sách nhân viên sắp xếp giảm dần theo năm sinh:")
for emp_id, info in sorted_employees:
    print(f"Mã: {emp_id}, Tên: {info['name']}, Năm sinh: {info['birth_year']}, Lương: {info['salary']}")