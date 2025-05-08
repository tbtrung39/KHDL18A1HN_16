def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

with open("Bài_tập_thực_Hành/f_in.dat2", "r") as f_in:
    lines = f_in.readlines()

with open("Bài_tập_thực_Hành/f_out.dat2", "w") as f_out:
    for line in lines:
        num = int(line.strip())
        uoc_nt = []

        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                uoc_nt.append(i)

        f_out.write(" ".join(map(str, uoc_nt)) + "\n")