def is_valid_char(c):
    return c.isalpha()

def main():
    nhap = []
    while True:
        try:
            s = input("Nhập ký tự hoặc chuỗi: ")
            if not all(is_valid_char(c) for c in s):
                raise ValueError("Lỗi ký tự !!!")
            if any(s[i] == s[i+1] for i in range(len(s) - 1)):
                raise Exception("Lỗi nhập liệu !!!")
            if len(s) >= 4 and all(ch == s[0] for ch in s):
                raise Exception("Lỗi nhập lặp lại !!!")
            nhap.append(s)
            if len(nhap) >= 5 and all(nhap[-1] == x for x in nhap[-5:]):
                raise Exception("Lỗi nhập trùng lặp!!!")
        except Exception as e:
            print("Lỗi:", e)