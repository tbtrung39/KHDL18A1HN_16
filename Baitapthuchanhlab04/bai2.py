n = 5  
s = 0.0
i = 2
while i <= n + 1:
    x = i
    for j in range(10): 
        x = 0.5 * (x + i / x)
    can_i = x
    y = i - 1
    for k in range(10):  
        y = 0.5 * (y + (i - 1) / y)
    can_i_tru_1 = y
    s += can_i - can_i_tru_1
    i += 1
print(s)  