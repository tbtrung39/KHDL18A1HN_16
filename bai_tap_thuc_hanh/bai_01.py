def sum_odd_numbers(filename):
    with open(filename, 'r') as file:
        total = 0
        for line in file:
            numbers = map(int, line.strip().split())
            odd_numbers = [n for n in numbers if n % 2 != 0]
            total += sum(odd_numbers)
    print("Tổng các số lẻ trong dãy là:", total)

sum_odd_numbers(r"bai_tap_thuc_hanh\dayso.dat")