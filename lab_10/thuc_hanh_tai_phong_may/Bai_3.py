from sohoc import Ucln, Bcnn, SumDivisor

def main():
    print("=== SỐ HỌC ===")
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    print(f"Ước chung lớn nhất của {a} và {b}: {Ucln(a, b)}")
    print(f"Bội chung nhỏ nhất của {a} và {b}: {Bcnn(a, b)}")

    n = int(input("Nhập số nguyên n để tính tổng các ước: "))
    print(f"Tổng các ước của {n} là: {SumDivisor(n)}")

if __name__ == "__main__":
    main()