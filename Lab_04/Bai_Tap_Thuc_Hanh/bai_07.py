a = int(input("nhập số  nguyên thứ nhất:"))
b = int(input("nhập sô nguyên thứ hai:"))
x =a 
y=b
while b!= 0:
  temp = b
  b=a%b
  a=temp
bcnn = (x*y)//a
print("Bội chung nhỏ nhất là :", bcnn)