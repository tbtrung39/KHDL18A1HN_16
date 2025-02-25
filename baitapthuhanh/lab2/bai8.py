experience = int(input("Nhập số tháng làm việc: "))
basic_salary = 1350000
if experience < 12:
    coefficient = 2.34
elif experience < 36:
    coefficient = 3.33
elif experience < 60:
    coefficient = 3.66
else:
    coefficient = 3.99
salary = coefficient * basic_salary
print(f"Lương nhận được: {salary} đồng")