def find_animals(g=0, total=36, legs=100):
    c = total - g  # Số con chó
    if g > total:
        return  # Điều kiện dừng
    
    # Kiểm tra tổng số chân
    if 2 * g + 4 * c == legs:
        print(f"Số gà: {g}, Số chó: {c}")
        return
    else:
        find_animals(g + 1, total, legs)  # Gọi đệ quy với gà tăng dần

# Gọi hàm
find_animals()