# Hàm tạo từ điển nhân viên
def create_employee_dict(n):
    employees = {}
    for _ in range(n):
        emp_id = input("Nhập mã nhân viên (4 ký tự số): ")
        name = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
        birth_year = int(input("Nhập năm sinh của nhân viên: "))
        salary = float(input("Nhập lương của nhân viên: "))

        # Thêm nhân viên vào từ điển
        employees[emp_id] = {"name": name, "birth_year": birth_year, "salary": salary}
    
    return employees

# Hàm thêm nhân viên vào từ điển
def add_employee(employees):
    emp_id = input("Nhập mã nhân viên (4 ký tự số): ")
    name = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
    birth_year = int(input("Nhập năm sinh của nhân viên: "))
    salary = float(input("Nhập lương của nhân viên: "))

    employees[emp_id] = {"name": name, "birth_year": birth_year, "salary": salary}
    print("Nhân viên đã được thêm thành công.")

# Hàm tìm kiếm nhân viên theo mã nhân viên
def search_employee(employees, emp_id):
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"Mã nhân viên: {emp_id}, Họ tên: {emp['name']}, Năm sinh: {emp['birth_year']}, Lương: {emp['salary']}")
    else:
        print("Không tìm thấy nhân viên với mã số này.")

# Hàm tăng lương cho nhân viên
def increase_salary(employees, emp_id, increase_amount):
    if emp_id in employees:
        employees[emp_id]['salary'] += increase_amount
        print(f"Lương của nhân viên mã {emp_id} đã được tăng lên {employees[emp_id]['salary']}.")
    else:
        print("Không tìm thấy nhân viên với mã số này.")

# Hàm xóa nhân viên theo mã
def delete_employee(employees, emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print(f"Nhân viên mã {emp_id} đã được xóa.")
    else:
        print("Không tìm thấy nhân viên với mã số này.")

# Hàm sắp xếp từ điển theo năm sinh giảm dần
def sort_employees_by_birth_year(employees):
    sorted_employees = sorted(employees.items(), key=lambda x: x[1]['birth_year'], reverse=True)
    print("\nDanh sách nhân viên sắp xếp theo năm sinh giảm dần:")
    for emp_id, emp in sorted_employees:
        print(f"Mã nhân viên: {emp_id}, Họ tên: {emp['name']}, Năm sinh: {emp['birth_year']}, Lương: {emp['salary']}")

# Main program
n = int(input("Nhập số lượng nhân viên: "))
employees = create_employee_dict(n)

# Menu chọn thao tác
while True:
    print("\nMenu:")
    print("1. Thêm nhân viên")
    print("2. Tìm kiếm nhân viên theo mã")
    print("3. Tăng lương cho nhân viên")
    print("4. Xóa nhân viên")
    print("5. Sắp xếp nhân viên theo năm sinh giảm dần")
    print("6. Thoát")

    choice = input("Chọn một thao tác (1-6): ")

    if choice == '1':
        add_employee(employees)
    elif choice == '2':
        emp_id = input("Nhập mã nhân viên cần tìm: ")
        search_employee(employees, emp_id)
    elif choice == '3':
        emp_id = input("Nhập mã nhân viên để tăng lương: ")
        increase_salary(employees, emp_id, 1000000)
    elif choice == '4':
        emp_id = input("Nhập mã nhân viên cần xóa: ")
        delete_employee(employees, emp_id)
    elif choice == '5':
        sort_employees_by_birth_year(employees)
    elif choice == '6':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")