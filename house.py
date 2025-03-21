import bpy
import math

# Xóa tất cả đối tượng trong cảnh để bắt đầu từ đầu
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Tạo thân nhà (hình lập phương)
bpy.ops.mesh.primitive_cube_add(
    size=2,  # Kích thước của căn nhà
    location=(0, 0, 1)  # Nâng lên để không bị chìm dưới mặt phẳng
)
house_body = bpy.context.object
house_body.name = "HouseBody"

# Tạo mái nhà (hình chóp)
bpy.ops.mesh.primitive_cone_add(
    vertices=4,  # 4 đỉnh tạo thành mái nhà hình chóp
    radius1=1.5,  # Bán kính đáy của mái
    depth=1.5,  # Chiều cao của mái
    location=(0, 0, 2.25)  # Đặt lên trên thân nhà
)
roof = bpy.context.object
roof.name = "HouseRoof"
roof.rotation_euler.z = math.radians(45)  # Xoay mái 45 độ để trông đẹp hơn

# Gán màu sắc cho thân nhà và mái nhà
def create_material(obj, color):
    mat = bpy.data.materials.new(name=obj.name + "_Material")
    mat.diffuse_color = (*color, 1)  # Thêm kênh alpha (1 = không trong suốt)
    obj.data.materials.append(mat)

create_material(house_body, (0.8, 0.3, 0.2))  # Màu đỏ cho thân nhà
create_material(roof, (0.5, 0.2, 0.1))  # Màu nâu cho mái nhà
