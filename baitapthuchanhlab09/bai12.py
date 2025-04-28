def giai_bai_toan_ga_cho():
  print("Bài toán cổ: Vừa gà vừa chó")
  print("Bó lại cho tròn")
  print("Ba mươi sáu con")
  print("Một trăm chân chẵn")
  print("Hỏi có bao nhiêu con gà và bao nhiêu con chó?")
  for so_ga in range(37):  
    so_cho = 36 - so_ga
    so_chan_ga = so_ga * 2
    so_chan_cho = so_cho * 4
    tong_so_chan = so_chan_ga + so_chan_cho
    if tong_so_chan == 100:
      print(f"Số gà là: {so_ga}")
      print(f"Số chó là: {so_cho}")
      return
  print("Không tìm thấy nghiệm phù hợp.")
giai_bai_toan_ga_cho()