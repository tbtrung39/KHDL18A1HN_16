def tim_cuc_tri_va_ghi_file():
    try:
        with open('f_in.dat', 'r') as file:
            numbers = list(map(int, file.readline().strip().split()))
            cuc_tri = []
            
            for i in range(len(numbers)):
                if i == 0:
                    if len(numbers) > 1 and numbers[i] != numbers[i+1]:
                        if numbers[i] > numbers[i+1]:
                            cuc_tri.append(numbers[i])
                        else:
                            cuc_tri.append(numbers[i])
                elif i == len(numbers) - 1:
                    if numbers[i] != numbers[i-1]:
                        if numbers[i] > numbers[i-1]:
                            cuc_tri.append(numbers[i])
                        else:
                            cuc_tri.append(numbers[i])
                else:
                    if (numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]) or \
                       (numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]):
                        cuc_tri.append(numbers[i])
            
            with open('f_out.dat', 'w') as out_file:
                out_file.write(f"{len(cuc_tri)}\n")
                out_file.write(' '.join(map(str, cuc_tri)))
                
            print("Đã ghi kết quả vào file f_out.dat")
    except FileNotFoundError:
        print("Không tìm thấy file f_in.dat")
    except ValueError:
        print("File chứa dữ liệu không hợp lệ")

tim_cuc_tri_va_ghi_file()