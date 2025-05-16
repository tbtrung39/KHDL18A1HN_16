def run_input_checker():
    history = []

    while True:
        try:
            s = input("Nhập chuỗi: ").strip()
            if not s.isalpha():
                raise ValueError("Lỗi ký tự !!!")

            # Kiểm tra 2 ký tự liên tiếp giống nhau
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    raise Exception("Lỗi nhập liệu !!!")

            # Kiểm tra 4 ký tự liên tiếp giống nhau
            for i in range(len(s) - 3):
                if s[i] == s[i+1] == s[i+2] == s[i+3]:
                    raise Exception("Lỗi nhập lặp lại !!!")

            # Kiểm tra 5 từ giống nhau liên tiếp
            history.append(s)
            if len(history) >= 5 and all(word == history[-1] for word in history[-5:]):
                raise Exception("Lỗi nhập trùng lặp!!!")

            print("Nhập hợp lệ.")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

run_input_checker()
