import bpy

# Xóa tất cả đối tượng trong cảnh để bắt đầu từ đầu
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Tạo hình torus (donut)
bpy.ops.mesh.primitive_torus_add(
    align='WORLD',
    location=(0, 0, 0),  # Vị trí
    major_radius=2,      # Bán kính lớn (khoảng cách từ tâm đến giữa thân donut)
    minor_radius=0.5,    # Bán kính nhỏ (bán kính thân donut)
    major_segments=48,   # Số phân đoạn vòng lớn
    minor_segments=12    # Số phân đoạn vòng nhỏ (càng nhiều càng mượt)
)

# Lấy đối tượng hình torus vừa tạo
donut = bpy.context.object
donut.name = "MyDonut"
