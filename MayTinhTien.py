resource_list = []
gias_list = []
maxs_list = []
n = int(input("Nhập số lượng mặt hàng sẽ có trong hệ thống: "))
for i in range(n):
    resource = input("Nhập tên sản phẩm: ")
    gias = int(input("Nhập giá tiền: "))
    maxs = int(input("Nhập số lượng sản phẩm tối đa trong kho: "))
    resource_list.append(resource)
    gias_list.append(gias)
    maxs_list.append(maxs)
print("Danh sách tài nguyên:")
for i in range(len(resource_list)):
    print(f"{i+1}. {resource_list[i]} ({gias_list[i]} đồng/{resource_list[i]}), {maxs_list[i]} {resource_list[i]}")
total = 0
while True:
    index = int(input("Nhập số của tài nguyên cần lấy (nhập 0 để kết thúc): "))
    if index == 0:
        break
    quantity = int(input("Nhập số lượng cần lấy: "))
    if quantity > maxs_list[index-1]:
        print(f"Số lượng tài nguyên còn lại không đủ ({maxs_list[index-1]} {resource_list[index-1]}).")
    else:
        total += quantity * gias_list[index-1]
        maxs_list[index-1] -= quantity
        print(f"{quantity} {resource_list[index-1]} đã được lấy.")
print(f"Tổng giá trị các món hàng được lấy ra là {total} đồng.")
