import sohoc
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
n = int(input("Nhập số nguyên n để tính tổng các ước: "))

print("Ước chung lớn nhất của", a, "và", b, "là:", sohoc.Ucln(a, b))
print("Bội chung nhỏ nhất của", a, "và", b, "là:", sohoc.Bcnn(a, b))
print("Tổng các ước của", n, "là:", sohoc.SumDivisor(n))
def calculate_and_print(a, b, n):
    print("Ước chung lớn nhất của", a, "và", b, "là:", sohoc.Ucln(a, b))
    print("Bội chung nhỏ nhất của", a, "và", b, "là:", sohoc.Bcnn(a, b))
    print("Tổng các ước của", n, "là:", sohoc.SumDivisor(n))

def main():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    n = int(input("Nhập số nguyên n để tính tổng các ước: "))
    calculate_and_print(a, b, n)

if __name__ == "__main__":
    main()