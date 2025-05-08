def dao_so(n, ket_qua=0):
    if n == 0:
        return ket_qua
    return dao_so(n // 10, ket_qua * 10 + n % 10)
a = 12345
so_dao = dao_so(a)
print("Số đảo ngược là:", so_dao)
