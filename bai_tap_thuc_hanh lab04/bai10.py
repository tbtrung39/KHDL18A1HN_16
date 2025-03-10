chu_so = ["khong", "mot","hai","ba","bon","nam","sau","bay","tam","chin"]
n = input("nhap so: ")
i = 0
while i < len(n):
    print(chu_so[int(n[i])], end=" ")
    i += 1
    