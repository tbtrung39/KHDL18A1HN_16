def tim_ga_cho(ga, cho):
    if ga + cho == 36 and 2*ga + 4*cho == 100:
        print(f"Số gà: {ga}, số chó: {cho}")
        return
    if ga > 36 or cho > 36:
        return
    tim_ga_cho(ga+1, cho)
    tim_ga_cho(ga, cho+1)

tim_ga_cho(0, 0)
