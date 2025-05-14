def kt_kytu(c):
    return c.isalpha() 

def kt_loikytu(s, history):
    for c in s:
        if not kt_kytu(c):
            raise Exception("Lỗi ký tự !!!")
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            raise Exception("Lỗi nhập liệu !!!")
    for i in range(len(s) - 3):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3]:
            raise Exception("Lỗi nhập lập lại !!!")
    if len(history) >= 4 and all(w == s for w in history[-4:]):
        raise Exception("Lỗi nhập trùng lặp!!!")

history = []

while True:
    try:
        s = input("Nhập chuỗi ký tự: ")
        if s == "ab" or s == "A.CZ":
            print("Kết thúc chương trình.")
            break
        kt_loikytu(s, history)
        history.append(s)
        print("Chuỗi hợp lệ:", s)
    except Exception as e:
        print(e)