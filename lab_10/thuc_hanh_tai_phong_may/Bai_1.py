from my_Triange import is_TamGiac, ChuViTamGiac, S_TamGiac

def main():
    print("=== TAM GIÁC ===")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if is_TamGiac(a, b, c):
        print("=> Đây là tam giác.")
        print(f"Chu vi: {ChuViTamGiac(a, b, c)}")
        print(f"Diện tích: {S_TamGiac(a, b, c):.2f}")
    else:
        print("=> Ba cạnh không tạo thành tam giác.")

if __name__ == "__main__":
    main()