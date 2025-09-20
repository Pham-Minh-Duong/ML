import math

print("Tính chu vi và diện tích hình tròn")

# Nhập bán kính r từ bàn phím
r = float(input("Nhập bán kính r: "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r ** 2

# In kết quả
print("Chu vi = 2 * π * %.2f = %.4f" % (r, cv))
print("Diện tích = π * %.2f^2 = %.4f" % (r, dt))
