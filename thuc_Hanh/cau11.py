c = input("Ngôn ngữ lập trình (C++ / Java / Python): ")
students = {
    "C++": ["t1", "t2", "t3"],
    "Java": ["k1", "k2"],
    "Python": ["h1", "h2", "h3"]
}
print("Danh sách sinh viên:", students.get(c, []))
