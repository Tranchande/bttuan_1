def calculate_body_fat(weight, wrist_size, waist_size, hip_size, arm_size, is_female=True):
    if is_female:
        # Calculate body fat for females
        A1 = (weight * 0.732) + 8.987
        A2 = wrist_size / 3.140
        A3 = waist_size * 0.157
        A4 = hip_size * 0.249
        A5 = arm_size * 0.434
        B = A1 + A2 - A3 - A4 + A5
        body_fat = weight - B
        body_fat_percentage = (body_fat * 100) / weight
        return body_fat, body_fat_percentage
    else:
        # Calculate body fat for males
        A1 = (weight * 1.082) + 9.442
        A2 = wrist_size * 4.15
        B = A1 - A2
        body_fat = weight - B
        body_fat_percentage = (body_fat * 100) / weight
        return body_fat, body_fat_percentage

weight_kg = float(input("Nhập cân nặng (kg): "))
wrist_cm = float(input("Nhập kích thước cổ tay (cm): "))
waist_cm = float(input("Nhập kích thước eo (cm): "))
hip_cm = float(input("Nhập kích thước hông (cm): "))
arm_cm = float(input("Nhập kích thước cánh tay (cm): "))
is_female = input("Bạn là nam hay nữ? (Nam: nam, Nữ: bất kỳ): ").lower() != "nam"
body_fat, body_fat_percentage = calculate_body_fat(weight_kg, wrist_cm, waist_cm, hip_cm, arm_cm, is_female)
print(f"Lượng mỡ: {body_fat:.2f} kg")
print(f"Phần trăm lượng mỡ: {body_fat_percentage:.2f}%")
