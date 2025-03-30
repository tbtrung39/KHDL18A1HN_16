nhật_ký = input("Nhập nhật ký giao dịch: ")
số_tiền = 0
loại = ""
tiền_chuoi = ""
các_chữ_số = "0123456789"
for ký_tự in nhật_ký:
  if ký_tự == 'D' or ký_tự == 'W':
    loại = ký_tự
  elif ký_tự in các_chữ_số:
    tiền_chuoi += ký_tự
  elif ký_tự == '\n':
    if loại and tiền_chuoi:
      tiền = int(tiền_chuoi)
      if loại == 'D':
        số_tiền += tiền
      elif loại == 'W':
        số_tiền -= tiền
      loại = ""
      tiền_chuoi = ""
if loại and tiền_chuoi:
  tiền = int(tiền_chuoi)
  if loại == 'D':
    số_tiền += tiền
  elif loại == 'W':
    số_tiền -= tiền
print(số_tiền)