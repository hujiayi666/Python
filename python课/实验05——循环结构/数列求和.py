"""编程求数列                              前30项之和"""
fz = 1
fm = 2
S = 0
for i in range(30):
    # 累加当前项
    S += fz / fm
    # 更新分子分母
    new_fz = fm
    fm = fz + fm
    fz = new_fz
print("数列前30项之和为:", S)