def solve_chicken_dog(total_animals, total_legs, chickens=0):
    dogs = total_animals - chickens
    if chickens * 2 + dogs * 4 == total_legs:
        return (chickens, dogs)
    if chickens > total_animals:
        return None
    return solve_chicken_dog(total_animals, total_legs, chickens + 1)
solution = solve_chicken_dog(36, 100)
if solution:
    chickens, dogs = solution
    print(f"Số gà: {chickens}, số chó: {dogs}")
else:
    print("Không có nghiệm thỏa mãn")