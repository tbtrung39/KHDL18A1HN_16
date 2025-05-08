with open("Bài_tập_thực_Hành/Inp.txt","r") as f_in:
    line = f_in.readline()
    numbers = list(map(int, line.strip().split()))

numbers.sort()

with open("Bài_tập_thực_Hành/out.dat", "w") as f_out:
    for num in numbers :
        f_out.write(str(num)+"\n")