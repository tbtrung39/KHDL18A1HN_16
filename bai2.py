with open("Inp.txt", "r") as f_in, open("Out.dat", "w") as f_out:
    for line in f_in:
        cac_so = list(map(int, line.split()))
        cac_so.sort()
        dong_moi = ' '.join(str(so) for so in cac_so)
        f_out.write(dong_moi + '\n')

