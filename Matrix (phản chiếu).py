import numpy as np

# Nhập số hàng và cột của ma trận
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []

print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

# Chuyển đổi danh sách thành ma trận numpy
A = np.array(A)

# Tạo ma trận phản chiếu
A_reflected = np.fliplr(A)

print("Ma trận phản chiếu của A là:")
print(A_reflected)
