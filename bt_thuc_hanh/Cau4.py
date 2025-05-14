# Cau 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def tim_uoc_nguyen_to():
    try:
        with open('f_in.dat', 'r') as inp_file, open('f_out.dat', 'w') as out_file:
            for line in inp_file:
                num = int(line.strip())
                divisors = [i for i in range(2, num+1) if num % i == 0 and is_prime(i)]
                out_file.write(' '.join(map(str, divisors)) + '\n')
        print("Đã ghi kết quả vào file f_out.dat")
    except FileNotFoundError:
        print("Không tìm thấy file f_in.dat")
    except ValueError:
        print("File chứa dữ liệu không hợp lệ")

tim_uoc_nguyen_to()