with open("dayso.dat", "r") as f:
    numbers = []
    for line in f:
        numbers += list(map(int, line.split()))
    odd_sum = sum(x for x in numbers if x % 2 == 1)
    print("Tổng các số lẻ:", odd_sum)