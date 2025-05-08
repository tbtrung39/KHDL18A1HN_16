def permutation(dang_co, con_lai):
    if not con_lai:
        print(dang_co)
        return
    for i in range(len(con_lai)):
        permutation(dang_co + [con_lai[i]], con_lai[:i] + con_lai[i+1:])
def main():
    n = int(input("Nhập n: "))
    day = list(range(1, n + 1))
    permutation([], day)

main()
