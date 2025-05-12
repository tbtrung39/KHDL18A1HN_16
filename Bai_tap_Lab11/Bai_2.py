def sap_xep_so():
    try:
        with open('Inp.txt', 'r') as inp_file:
            line = inp_file.readline()
            numbers = list(map(int, line.strip().split()))
            numbers.sort()
        
        with open('out.dat', 'w') as out_file:
            out_file.write(' '.join(map(str, numbers)))
        print("Đã sắp xếp và ghi kết quả vào out.dat")
    except FileNotFoundError:
        print("Không tìm thấy file Inp.txt")
    except ValueError:
        print("File chứa dữ liệu không hợp lệ")
sap_xep_so()